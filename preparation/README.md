# GeoSplitter

## Überblick
`GeoSplitter` ist ein Python-Tool, um große GeoJSON-Dateien in kleinere, handhabbare Segmente aufzuteilen. Dies ist besonders nützlich, um die Ladezeiten und Effizienz bei der Arbeit mit umfangreichen geographischen Daten in Webanwendungen oder GIS-Projekten zu verbessern. Zusätzlich generiert GeoSplitter einen JSON-Index, der jedes Segment mit einem spezifischen Koordinatenbereich verknüpft, um eine einfache Integration und Nutzung der segmentierten Daten zu ermöglichen.

## Voraussetzungen

Bevor du `GeoSplitter` verwendest, stelle sicher, dass Python `3.x` auf deinem System installiert ist und folgende Pakete verfügbar sind:

- `Geopandas`: Eine Erweiterung für Pandas, um räumliche Daten einfach zu handhaben.
- `Shapely`: Für geometrische Operationen innerhalb der Python-Umgebung.

Diese Abhängigkeiten kannst du durch die Installation der `requirements.txt` Datei einbinden, die im Projekt enthalten ist.

## Einrichtung

1. Klone das `GeoSplitter`-Repository auf dein lokales System.
2. Installiere die erforderlichen Pakete mit Pip:

```bash
pip install -r requirements.txt
```

Die `requirements.txt` enthält alle notwendigen Python-Pakete, einschließlich:

- **Geopandas** (`geopandas==0.14.3`)
- **Shapely** (`shapely==2.0.3`)
- **Fiona** (`fiona==1.9.6`) für das Lesen und Schreiben von GeoJSON-Dateien

## Verwendung

1. **Vorbereitung der Eingabedaten:** Platziere deine GeoJSON-Datei im `input`-Unterordner. Es wird erwartet, dass sie `trees.geojson` heißt; ändere gegebenenfalls den Wert von `INPUT_PATH` im `splitter.py` Skript, um auf deine spezifische Datei zu verweisen.
2. **Ausführen des `splitter` - Skripts:** Starte das `splitter.py`-Skript, um die GeoJSON-Datei zu segmentieren und die Index-Datei zu generieren. Standardmäßig wird ein neuer Unterordner `segments` erzeugt mit mehreren kleinen GeoJSON-Dateien sowie eine `segments_index.json`, die die Segmentdateien mit den Koordinatenbereichen verknüpft.