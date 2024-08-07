import geopandas as gpd
import json
import os
from shapely.geometry import box
from tqdm import tqdm

# Definiert Pfade für Eingabe- und Ausgabedaten sowie Basispfad der Ausführung
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, 'data', 'clean_trees.geojson')
SEGMENTS_DIR = os.path.join(BASE_DIR, 'segments')

# Festlegen der Anzahl von Segmenten pro Achse im Raster
GRID_SIZE = 10

def create_filtered_gdf(segment_gdf):
    """
    Erstellt eine gefilterte GeoDataFrame, die nur die spezifizierten Eigenschaften enthält.
    
    :param segment_gdf: GeoDataFrame, die die GeoJSON-Daten eines Segments enthält.
    :return: Eine neue GeoDataFrame mit nur den gewünschten Eigenschaften.
    """

    # Definiere die gewünschten Eigenschaften
    desired_properties = ['oid', 'Baumart', 'Kronendurc', 'Standort_N', 'Objekt_Bez']
    
    # Prüfe, welche der gewünschten Eigenschaften in den Daten vorhanden sind
    available_properties = [prop for prop in desired_properties if prop in segment_gdf.columns]

    # Filtere die Daten, um nur die gewünschten Eigenschaften und die Geometrie zu behalten
    filtered_data = segment_gdf[available_properties + ['geometry']]

    return filtered_data


def create_segments(gdf, json_map):
    """
    Erstellt segmentierte GeoJSON-Dateien basierend auf den definierten Rastersegmenten
    
    :param gdf: GeoDataFrame der originalen GeoJSON-Daten
    :param json_map: Liste von Dictionaries, die Rastersegmente und Dateinamen definieren
    """
    for segment in tqdm(json_map):
        # Erstellt eine Bounding Box für das aktuelle Segment
        bbox = box(segment["minX"], segment["minY"], segment["maxX"], segment["maxY"])
        # Selektiert Features, die sich innerhalb der Bounding Box befinden
        segment_gdf = gdf[gdf.intersects(bbox)]
        
        # Filtere und behalte nur die gewünschten Eigenschaften
        if not segment_gdf.empty:
            filtered_segment_gdf = create_filtered_gdf(segment_gdf)
            
            # Speichert das gefilterte Segment als GeoJSON, wenn es Features enthält
            if not filtered_segment_gdf.empty:
                segment_path = os.path.join(SEGMENTS_DIR, segment["fileName"])
                filtered_segment_gdf.to_file(segment_path, driver="GeoJSON")

        else:
            json_map[json_map.index(segment)]['fileName'] = None
    return json_map





def main():
    # Lädt die ursprünglichen GeoJSON-Daten in eine GeoDataFrame
    gdf = gpd.read_file(DATA_PATH)

    # Setze das aktuelle Koordinatensystem, falls es nicht schon gesetzt ist
    gdf.crs = "EPSG:25832"

    # Transformiere die Koordinaten zu WGS84
    gdf = gdf.to_crs("EPSG:4326")

    # Ermittelt die äußeren Grenzen der GeoDataFrame
    minx, miny, maxx, maxy = gdf.total_bounds

    # Berechnet die Dimensionen eines einzelnen Segments
    width = (maxx - minx) / GRID_SIZE
    height = (maxy - miny) / GRID_SIZE

    # Initialisiert die Liste, die die Karte der Segmente speichert
    json_map = []

    # Generiert die Segmente basierend auf dem Raster
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            rect_minx = minx + x * width
            rect_miny = miny + y * height
            rect_maxx = rect_minx + width
            rect_maxy = rect_miny + height
            file_name = f'segment_{x+1:02}_{y+1:02}.geojson'
            json_map.append({
                "minX": rect_minx,
                "maxX": rect_maxx,
                "minY": rect_miny,
                "maxY": rect_maxy,
                "fileName": file_name
            })

    # Stellt sicher, dass das Ausgabeverzeichnis existiert
    os.makedirs(SEGMENTS_DIR, exist_ok=True)
    
    # Ruft die Funktion zum Erstellen der Segment-Dateien auf
    json_map = create_segments(gdf, json_map)

    # Speichert die Karte der Segmente als JSON
    map_path = os.path.join(SEGMENTS_DIR, 'map.json')
    with open(map_path, 'w') as f:
        json.dump(json_map, f)

if __name__ == '__main__':
    main()
