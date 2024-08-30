import geopandas as gpd
import json
import os
from shapely.geometry import box

# Definiert Pfade für Eingabe- und Ausgabedaten sowie Basispfad der Ausführung
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_PATH = os.path.join(BASE_DIR, "input", "trees.geojson")
OUTPUT_DIR = os.path.join(BASE_DIR, "segments")

# Definiert die Anzahl der Segmente pro Achse im Raster (GRID_SIZE x GRID_SIZE Raster)
GRID_SIZE = 10

def create_filtered_gdf(segment_gdf):
    """
    Filtert die GeoDataFrame nach spezifischen Eigenschaften und behält nur relevante Spalten bei.
    
    :param segment_gdf: GeoDataFrame, die GeoJSON-Daten eines Segments enthält.
    :return: Ein gefiltertes GeoDataFrame, das nur die gewünschten Eigenschaften und die Geometrie enthält.
    """

    # Definiere die gewünschten Eigenschaften, die im gefilterten GeoDataFrame enthalten sein sollen
    desired_properties = ["pitID", "Baumart_de", "Kronendurc"]
    
    # Überprüfe, welche der gewünschten Eigenschaften tatsächlich in den Daten vorhanden sind
    available_properties = [prop for prop in desired_properties if prop in segment_gdf.columns]

    # Filtere das GeoDataFrame, um nur die verfügbaren gewünschten Eigenschaften und die Koordinaten zu behalten
    filtered_data = segment_gdf[available_properties + ["geometry"]]

    return filtered_data


def create_segments_and_index(gdf):
    """
    Erstellt rasterbasierte Segmente aus dem GeoDataFrame und speichert sie als separate GeoJSON-Dateien.
    Außerdem wird ein Index-File erstellt, das die Informationen über alle Segmente enthält.
    
    :param gdf: Das gefilterte GeoDataFrame, das in Segmente aufgeteilt werden soll.
    """

    # Bestimme die äußeren Grenzen des GeoDataFrame
    minX, minY, maxX, maxY = gdf.total_bounds

    # Berechne die Breite und Höhe eines einzelnen Segments im Raster
    width = (maxX - minX) / GRID_SIZE
    height = (maxY - minY) / GRID_SIZE

    # Initialisiere eine Liste, um Informationen über alle Segmente zu speichern
    json_index = []

    # Durchlaufe das Raster und erstelle die Segmente
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            # Bestimme die Grenzen für das aktuelle Segment
            segment_bounds = {
                "minX": minX + x * width,
                "minY": minY + y * height,
                "maxX": minX + (x + 1) * width,
                "maxY": minY + (y + 1) * height
            }

            # Definiere die Position des aktuellen Segments im Raster
            grid_position = {"x": x, "y": y}

            # Erstelle das Segment und speichere es als GeoJSON-Datei
            file_name = create_segment_file(gdf, segment_bounds, grid_position)

            # Füge die Segmentinformationen dem Index hinzu
            json_index.append({
                "minX": segment_bounds["minX"],
                "maxX": segment_bounds["maxX"],
                "minY": segment_bounds["minY"],
                "maxY": segment_bounds["maxY"],
                "fileName": file_name
            })
    
    # Speichere den Index aller Segmente als JSON-Datei
    index_path = os.path.join(OUTPUT_DIR, "segments_index.json")
    with open(index_path, "w") as f:
        json.dump(json_index, f)


def create_segment_file(gdf, segment_bounds, grid_position):
    """
    Erstellt ein einzelnes Segment basierend auf den angegebenen Grenzen und speichert es als GeoJSON-Datei.
    
    :param gdf: Das gefilterte GeoDataFrame.
    :param segment_bounds: Ein Dictionary mit den Grenzen (minX, minY, maxX, maxY) des Segments.
    :param grid_position: Die Position des Segments im Raster, angegeben als Dictionary mit 'x' und 'y'.
    :return: Der Dateiname der erstellten GeoJSON-Datei oder None, wenn das Segment leer ist.
    """

    # Erstelle eine Bounding Box für das Segment basierend auf den übergebenen Grenzen
    bbox = box(segment_bounds["minX"], segment_bounds["minY"], segment_bounds["maxX"], segment_bounds["maxY"])
    
    # Filtere das GeoDataFrame, um nur die Daten zu behalten, die innerhalb der Bounding Box liegen
    segment_gdf = gdf[gdf.intersects(bbox)]

    # Speichere das Segment, wenn es nicht leer ist
    if not segment_gdf.empty:
        file_name =  f'segment_{grid_position["x"]+1:02}_{grid_position["y"]+1:02}.geojson'
        segment_path = os.path.join(OUTPUT_DIR, file_name)
        segment_gdf.to_file(segment_path, driver="GeoJSON")
        return file_name
    
    return None


def main():
    """
    Der Haupteinstiegspunkt für das Skript.
    Lädt die GeoJSON-Daten, filtert sie, erstellt Rastersegmente und speichert die Ergebnisse.
    """

    # Lade das GeoDataFrame aus der Eingabe-GeoJSON-Datei
    gdf = gpd.read_file(INPUT_PATH)
    
    # Stelle sicher, dass das CRS auf "EPSG:4326" gesetzt ist, und transformiere es gegebenenfalls
    if gdf.crs != "EPSG:4326":
        gdf = gdf.to_crs("EPSG:4326")

    # Filtere das GeoDataFrame, um nur relevante Spalten beizubehalten
    gdf = create_filtered_gdf(gdf)

    # Stelle sicher, dass das Ausgabeverzeichnis existiert
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Erstelle die Rastersegmente und den zugehörigen Index
    create_segments_and_index(gdf)

if __name__ == "__main__":
    # Starte das Skript, wenn es direkt ausgeführt wird
    main()
