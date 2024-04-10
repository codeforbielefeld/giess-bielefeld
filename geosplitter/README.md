# GeoSplitter

## Überblick
GeoSplitter ist ein Python-Tool, um große GeoJSON-Dateien in kleinere, handhabbare Segmente aufzuteilen. Dies ist besonders nützlich, um die Ladezeiten und Effizienz bei der Arbeit mit umfangreichen geographischen Daten in Webanwendungen oder GIS-Projekten zu verbessern. Zusätzlich generiert GeoSplitter eine JSON-Karte, die jedes Segment mit einem spezifischen Koordinatenbereich verknüpft, um eine einfache Integration und Nutzung der segmentierten Daten zu ermöglichen.

## Voraussetzungen

Bevor du GeoSplitter verwendest, stelle sicher, dass Python 3.x auf deinem System installiert ist und folgende Pakete verfügbar sind:

- Geopandas: Eine Erweiterung für Pandas, um räumliche Daten einfach zu handhaben.
- Shapely: Für geometrische Operationen innerhalb der Python-Umgebung.

Diese Abhängigkeiten kannst du durch die Installation der `requirements.txt` Datei einbinden, die im Projekt enthalten ist.

## Einrichtung

1. Klone das GeoSplitter-Repository auf dein lokales System.
2. Installiere die erforderlichen Pakete mit Pip:

```bash
pip install -r requirements.txt
```

Die `requirements.txt` enthält alle notwendigen Python-Pakete, einschließlich:

- Geopandas (`geopandas==0.14.3`)
- Shapely (`shapely==2.0.3`)
- Fiona (`fiona==1.9.6`) für das Lesen und Schreiben von GeoJSON-Dateien

## Verwendung

1. **Vorbereitung der Eingabedaten:** Platziere deine GeoJSON-Datei im `data`-Unterordner. Ändere gegebenenfalls den `DATA_PATH` im Skript, um auf deine spezifische Datei zu verweisen.
2. **Konfigurieren der Segmentgröße:** Die `GRID_SIZE` Variable im Skript bestimmt, wie viele Segmente pro Dimension erstellt werden. Experimentiere mit verschiedenen Werten, um die optimale Größe für deine Anwendung zu finden.
3. **Ausführen des Skripts:** Starte das Skript, um die GeoJSON-Datei zu segmentieren und die JSON-Karte zu generieren.

Das Ergebnis sind mehrere kleinere GeoJSON-Dateien im `segments`-Ordner und eine `map.json`, die die Segmentdateien mit den Koordinatenbereichen verknüpft.