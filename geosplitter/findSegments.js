// Importiere das Dateisystem- und Pfadmodul von Node.js.
const fs = require('fs');
const path = require('path');

// Konstruiere den Pfad zur map.json Datei im segments-Ordner relativ zum Skriptverzeichnis.
const MAP_PATH = path.join(__dirname, 'segments', 'map.json');

/**
 * Überprüft, ob sich zwei geographische Bereiche überschneiden.
 * 
 * @param {Object} segment - Ein Objekt, das die Grenzen eines Segments repräsentiert.
 * @param {Object} viewport - Ein Objekt, das die Grenzen eines Bildausschnitts repräsentiert.
 * @returns {boolean} - Gibt true zurück, wenn sich die Bereiche überschneiden, sonst false.
 */
function intersects(segment, viewport) {
    return segment.min_x <= viewport.maxX &&
           segment.max_x >= viewport.minX &&
           segment.min_y <= viewport.maxY &&
           segment.max_y >= viewport.minY;
}

/**
 * Nimmt die Koordinaten eines Bildausschnitts entgegen und gibt die Dateinamen der Segmente zurück,
 * die sich mit diesem Bildausschnitt überschneiden.
 * 
 * @param {number} minX - Die minimale X-Koordinate des Bildausschnitts.
 * @param {number} maxX - Die maximale X-Koordinate des Bildausschnitts.
 * @param {number} minY - Die minimale Y-Koordinate des Bildausschnitts.
 * @param {number} maxY - Die maximale Y-Koordinate des Bildausschnitts.
 * @returns {Array} - Ein Array von Dateinamen der Segmente, die sich mit dem Bildausschnitt überschneiden.
 */
function findMatchingSegments(minX, maxX, minY, maxY) {
    // Synchrones Einlesen der map.json, um die Liste der Segmente zu erhalten.
    const data = fs.readFileSync(MAP_PATH);
    const segments = JSON.parse(data);

    // Definiere den Bildausschnitt als Objekt mit den gegebenen Koordinaten.
    const viewport = { minX, maxX, minY, maxY };

    // Filtere die Segmente heraus, die sich mit dem Bildausschnitt überschneiden.
    const matchingSegments = segments.filter(segment => intersects(segment, viewport));

    // Extrahiere die Dateinamen der überschneidenden Segmente und gib sie zurück.
    return matchingSegments.map(segment => segment.file_name);
}

// Beispielaufruf der Funktion mit einem Bildausschnitt in WGS84 Koordinaten.
const exampleViewport = {
    // Angenommene WGS84 Koordinaten für den Bildausschnitt
    minX: 8.5, // Minimale Länge (Longitude)
    maxX: 8.52, // Maximale Länge (Longitude)
    minY: 52, // Minimale Breite (Latitude)
    maxY: 52.2  // Maximale Breite (Latitude)
};

// Ermittle die passenden Dateinamen basierend auf dem Beispiel-Bildausschnitt.
const matchingFiles = findMatchingSegments(exampleViewport.minX, exampleViewport.maxX, exampleViewport.minY, exampleViewport.maxY);

// Gib die passenden Dateinamen auf der Konsole aus.
console.log(matchingFiles);