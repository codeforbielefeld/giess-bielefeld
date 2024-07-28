import click
import geopandas as gpd
import os

def load_geojson(file_path):
    """
    Lädt eine GeoJSON-Datei und gibt ein GeoDataFrame zurück.
    """
    return gpd.read_file(file_path)

def filter_invalid_coordinates(gdf):
    """
    Filtert fehlerhafte Werte in den X- und Y-Koordinaten (negative Werte).
    """
    valid_gdf = gdf[(gdf.geometry.x > 0) & (gdf.geometry.y > 0)]
    return valid_gdf

def save_geojson(gdf, output_path):
    """
    Speichert das GeoDataFrame als GeoJSON-Datei.
    """
    gdf.to_file(output_path, driver='GeoJSON')
   
@click.command(help="Filter GeoJSON file and remove invalid coordinates.")
@click.option('-i', '--input_file', required=True, type=str, help="Name of the input GeoJSON file")
@click.option('-o', '--output_file', required=False, type=str, help="Name of the output GeoJSON file")
def main(input_file, output_file):
    """
    Filter GeoJSON file and remove invalid coordinates.

    :param input_file: Name of the input GeoJSON file 
    :param output_file: Name of the output GeoJSON file
    """
    
    # Lade die GeoJSON-Datei
    gdf = load_geojson(input_file)

    # Filtere fehlerhafte Koordinaten
    valid_gdf = filter_invalid_coordinates(gdf)

    # Wenn der Ausgabe-Pfad angegeben ist, speichere die bereinigte GeoJSON-Datei
    if output_file:
        # Speichere die bereinigte GeoJSON-Datei
        save_geojson(valid_gdf, output_file)
        print(f"Bereinigte GeoJSON-Datei wurde gespeichert unter: {output_file}")
    else:
        # Ansonsten gib das bereinigte GeoDataFrame zurück
        return valid_gdf

if __name__ == '__main__':
    main()