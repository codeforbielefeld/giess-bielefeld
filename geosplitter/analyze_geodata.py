import geopandas as gpd
import os

def filter_outliers(gdf):
    """Filtert Ausreißer basierend auf unrealistischen Koordinatenwerten."""
    MIN_X = 400000  # Angenommener realistischer minimaler X-Wert
    MIN_Y = 5000000  # Angenommener realistischer minimaler Y-Wert

    # Filtere die GeoDataFrame basierend auf realistischen minimalen Koordinaten
    filtered_gdf = gdf[(gdf.geometry.x > MIN_X) & (gdf.geometry.y > MIN_Y)]
    
    return filtered_gdf

def analyze_coordinates(gdf):
    """Analysiert die Koordinaten und findet minimale und maximale Werte."""
    # Extrahiere die Koordinaten aus der GeoDataFrame
    x_values = gdf.geometry.x
    y_values = gdf.geometry.y

    # Finde min und max Werte
    min_x, max_x = x_values.min(), x_values.max()
    min_y, max_y = y_values.min(), y_values.max()

    print(f"Min X: {min_x}, Max X: {max_x}")
    print(f"Min Y: {min_y}, Max Y: {max_y}")

def main():
    # Basispfad zum Projektordner
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    # Pfad zur GeoJSON-Datei im 'data'-Ordner
    DATA_PATH = os.path.join(BASE_DIR, 'data', 'trees.geojson')

    # Lade die GeoJSON-Daten
    gdf = gpd.read_file(DATA_PATH)

    # Filtere Ausreißer
    filtered_gdf = filter_outliers(gdf)

    # Analysiere die Koordinaten der gefilterten Daten
    analyze_coordinates(filtered_gdf)

if __name__ == '__main__':
    main()
