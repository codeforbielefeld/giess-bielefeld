import pandas as pd
import geopandas as gpd
from shapely import wkt
from shapely.geometry import Point
import click

def round_coordinates(geometry, decimal_places):
    """
    Rundet die Koordinaten eines Punktes auf eine bestimmte Anzahl von Nachkommastellen.
    
    :param geometry: Shapely-Objekt (Punkt)
    :param decimal_places: Anzahl der Nachkommastellen, auf die gerundet werden soll
    :return: Gerundetes Shapely-Objekt (Punkt)
    """
    if isinstance(geometry, Point):
        return Point(round(geometry.x, decimal_places), round(geometry.y, decimal_places))
    return geometry

def save_geojson(gdf, output_path):
    """
    Speichert das GeoDataFrame als GeoJSON-Datei.
    """
    gdf.to_file(output_path, driver='GeoJSON')

def prepare_gdf(df, decimal_places, is_wkt=False):
    """
    Rundet die Koordinaten eines GeoDataFrame oder DataFrame mit WKT-Spalte.
    
    :param df: GeoDataFrame oder DataFrame mit WKT-Spalte
    :param decimal_places: Anzahl der Nachkommastellen, auf die die Koordinaten gerundet werden sollen
    :param is_wkt: Boolean, der angibt, ob der DataFrame eine WKT-Spalte hat
    :return: GeoDataFrame mit gerundeten Koordinaten
    """
    if is_wkt:
        # Wandelt WKT in Geometrie um und rundet die Koordinaten
        df.loc[:, 'geometry'] = df['WKT'].apply(wkt.loads).apply(lambda geom: round_coordinates(geom, decimal_places))
        df = df.drop(columns=['WKT'])
    else:
        # Rundet die Koordinaten in der GeoDataFrame
        df.loc[:, 'geometry'] = df['geometry'].apply(lambda geom: round_coordinates(geom, decimal_places))
    
    return gpd.GeoDataFrame(df, geometry='geometry')

def assign_missing_oids(gdf_merged, max_oid):
    """
    Weist OIDs für nicht übereinstimmende Geometrien zu.
    
    :param gdf_merged: Zusammengeführtes GeoDataFrame
    :param max_oid: Maximale vorhandene OID zur Bestimmung der neuen OIDs
    :return: GeoDataFrame mit zugewiesenen OIDs
    """
    non_matching_gdf = gdf_merged[gdf_merged['oid'].isna()]
    non_matching_gdf = non_matching_gdf.reset_index(drop=True)
    non_matching_gdf.loc[:, 'oid'] = non_matching_gdf.index + max_oid + 1

    gdf_merged.loc[gdf_merged['oid'].isna(), 'oid'] = non_matching_gdf['oid'].values
    
    return gdf_merged

def insert_oids(gdf, df_oids, decimal_places=3):
    """
    Führt das Einfügen von OIDs in ein gefiltertes GeoDataFrame durch.
    
    :param gdf: Eingabe GeoDataFrame
    :param df_oids: DataFrame mit OIDs
    :param decimal_places: Anzahl der Nachkommastellen, auf die die Koordinaten gerundet werden sollen
    :return: GeoDataFrame mit OIDs
    """
    gdf = prepare_gdf(gdf, decimal_places)
    df_oids = df_oids[['WKT', 'oid']].copy()
    gdf_oids = prepare_gdf(df_oids, decimal_places, is_wkt=True)

    # Zusammenführen der beiden GeoDataFrames basierend auf den gerundeten Geometrien
    gdf_merged = gdf.merge(gdf_oids, on='geometry', how='left')

    # OIDs für nicht übereinstimmende Geometrien zuweisen
    max_oid = gdf_oids['oid'].max()
    gdf_merged = assign_missing_oids(gdf_merged, max_oid)

    # Setzen der `oid`-Spalte als erste Spalte
    cols = ['oid'] + [col for col in gdf_merged.columns if col != 'oid']
    gdf_merged = gdf_merged.loc[:, cols]

    # Konvertieren der OID-Spalte in Ganzzahl, um Dezimalstellen zu vermeiden
    gdf_merged.loc[:, 'oid'] = gdf_merged['oid'].astype(int)   

    return gdf_merged

@click.command(help="Insert OIDs into GeoJSON file using data from a CSV file.")
@click.option('-g', '--geojson_file', required=False, type=str, help="Name of the input GeoJSON file")
@click.option('-c', '--csv_file', required=False, type=str, help="Name of the input CSV file with OIDs")
@click.option('-o', '--output_file', required=False, type=str, help="Name of the optional output GeoJSON file")
def main(geojson_file, csv_file, output_file):
    if geojson_file:
        gdf = gpd.read_file(geojson_file)
    else:
        raise ValueError("geojson_file muss angegeben werden.")
        
    if csv_file:
        df_oids = pd.read_csv(csv_file, sep=";")
    else:
        raise ValueError("csv_file muss angegeben werden.")

    result_gdf = insert_oids(gdf, df_oids)

    # Wenn der Ausgabe-Pfad angegeben ist, speichere die bereinigte GeoJSON-Datei
    if output_file:
        save_geojson(result_gdf, output_file)
        print(f"Bereinigte GeoJSON-Datei wurde gespeichert unter: {output_file}")
    else:
        # Ansonsten gib das bereinigte GeoDataFrame zurück
        return result_gdf
    
if __name__ == '__main__':
    main()
