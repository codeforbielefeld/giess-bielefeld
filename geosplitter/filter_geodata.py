import geopandas as gpd
import os

# Definiert die Grenzwerte
MIN_X = 400000
MIN_Y = 5000000

# Basispfad und Pfad zur GeoJSON-Datei
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, 'data', 'trees.geojson')
CLEAN_DATA_PATH = os.path.join(BASE_DIR, 'data', 'clean_trees.geojson')

def filter_data(gdf):
    """
    Filtert Einträge, deren Koordinaten unterhalb der definierten Grenzen liegen,
    und gibt diese Einträge im Terminal aus.
    """
    # Filtere Einträge basierend auf den Grenzwerten
    outliers = gdf[(gdf.geometry.x < MIN_X) | (gdf.geometry.y < MIN_Y)]
    clean_data = gdf[~((gdf.geometry.x < MIN_X) | (gdf.geometry.y < MIN_Y))]
    
    # Gib die Ausreißer im Terminal aus
    print("Ausreißer gefunden:")
    for index, row in outliers.iterrows():
        print(f"Index: {index}, X: {row.geometry.x}, Y: {row.geometry.y}")
    
    # Speichere die bereinigten Daten als neue GeoJSON-Datei
    clean_data.to_file(CLEAN_DATA_PATH, driver='GeoJSON')
    
    print(f"\nBereinigte Daten wurden gespeichert unter: {CLEAN_DATA_PATH}")

def main():
    # Lade die GeoJSON-Daten
    gdf = gpd.read_file(DATA_PATH)

    # Filtere die Daten und verarbeite die Ausreißer
    filter_data(gdf)

if __name__ == '__main__':
    main()