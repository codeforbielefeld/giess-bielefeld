import click
import pandas as pd
from filter_geodata import load_geojson, filter_invalid_coordinates
from insert_oids import insert_oids, save_geojson


def filter_properties(gdf, desired_properties):
    """
    Filtert das GeoDataFrame, um nur die gewünschten Eigenschaften und die Geometrie zu behalten.
    
    :param gdf: Eingabe GeoDataFrame
    :param desired_properties: Liste der gewünschten Eigenschaften
    :return: Gefiltertes GeoDataFrame
    """
    available_properties = [prop for prop in desired_properties if prop in gdf.columns]
    filtered_gdf = gdf[available_properties + ['geometry']]
    return filtered_gdf


@click.command(help="Filter GeoJSON file, remove invalid coordinates, and insert OIDs from a CSV file.")
@click.option('-i', '--input_file', required=True, type=str, help="Name of the input GeoJSON file")
@click.option('-c', '--csv_file', required=False, type=str, help="Name of the input CSV file with OIDs")
@click.option('-o', '--output_file', required=True, type=str, help="Name of the output GeoJSON file")
def main(input_file, csv_file, output_file):
    """
    Filter GeoJSON file, remove invalid coordinates, and insert OIDs from a CSV file.
    
    :param input_file: Name of the input GeoJSON file 
    :param csv_file: Name of the input CSV file with OIDs
    :param output_file: Name of the output GeoJSON file
    """

    # Schritt 1: Die GeoJSON laden und Eigenschaften reduzieren
    gdf = load_geojson(input_file)

    # Definiere die gewünschten Eigenschaften
    desired_properties = ['oid', 'Baumart', 'Kronendurc', 'Standort_N', 'Objekt_Bez']
    
    # Filtere die Daten, um nur die gewünschten Eigenschaften und die Geometrie zu behalten
    filtered_gdf = filter_properties(gdf, desired_properties)

    # Schritt 2: Alle ungültigen Koordinaten entfernen
    valid_gdf = filter_invalid_coordinates(filtered_gdf)
    
    # Schritt 3: Wenn csv_file angegeben ist, die OIDs einfügen
    if csv_file:
        df_oids = pd.read_csv(csv_file, sep=";")
        result_gdf = insert_oids(valid_gdf, df_oids)
    else:
        result_gdf = valid_gdf

    # Schritt 4: Speichern des endgültigen GeoDataFrame
    save_geojson(result_gdf, output_file)
    print(f"Final GeoJSON file with OIDs was saved to: {output_file}")

if __name__:
    main()