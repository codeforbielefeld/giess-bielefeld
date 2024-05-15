# Gieß' Bielefeld

TODO: Beschreibung hinzufügen.

## Setup

Für die lokale Entwicklung muss eine Supabase-Instanz aufgesetzt werden.
Hierfür kann die [`supabase-cli`](https://supabase.com/docs/guides/cli) verwendet werden:

```
npm install -g supabase-cli
supabase start
supabase migrations up
```

Die `.env`-Datei muss mit den Zugangsdaten zur Supabase-Instanz gefüllt werden, die beim Start der Supabase auf der
Konsole ausgegeben werden. Ein Beispiel für die `.env`-Datei befindet sich in der Datei `.env.example`:

```
VITE_SUPABASE_URL=http://127.0.0.1:54321
VITE_SUPABASE_ANON_KEY=
SUPABASE_SERVICE_ROLE_KEY=
```

Die entsprechenden Werte für `VITE_SUPABASE_ANON_KEY` und `SUPABASE_SERVICE_ROLE_KEY` müssen in die `.env`-Datei
eingetragen werden und entsprechen den Werten `anon key` und `service_role key` aus der Ausgabe der 
`supabase start`-Kommandos.

### Berechtigungen

Um auf die Supabase-Instanz und die darin enthaltenen Daten zugreifen zu können, müssen die Berechtigungen für die
Tabelle `trees` vergeben werden.
Dazu kann das Supabase Studio unter der URL http://127.0.0.1:54323 geöffnet werden, solange die Supabase im Hintergrund
läuft.
Dort kann die Tabelle `trees` ausgewählt und die Berechtigungen für die Tabelle vergeben werden:
In der linken Seitenleiste wird der Table Editor ausgewählt.
In der geöffneten Ansicht wählst du dann die Tabelle `trees` aus.
Oben rechts klickst du auf `Add RLS policy` und dann oben rechts auf `New policy`, im sich öffnenden Dialog dann
`Get started quickly`.
Anschließend kannst du die Berechtigungen anpassen, für uns reicht es dann unten rechts auf `Use this template`  zu
klicken.
Danach klickst du auf `Review` unten rechts und schließlich auf `Save policy`.

### Datenimport

Für den Import der Daten wird die `trees.json`-Datei benötigt, die aktuell nicht Bestandteil dieses Repositorys ist.
Diese Datei muss im `import`-Verzeichnis abgelegt werden.
Anschließend kann der Import mit dem `import`-Skript im `import`-Ordner gestartet werden.
Da weitere Bibliotheken erforderlich sind, um die Daten zu importieren, empfiehlt es sich, eine virtuelle
Python-Umgebung zu erstellen und die erforderlichen Bibliotheken zu installieren:

```
cd import
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Anschließend kann der Import gestartet werden:

```
python import.py <path-to-geojson-file>
```

### Geosplitting

Um die Performance des Karten-Renderns zu verbessern muss die `trees.json`-Datei gesplittet werden.
Dazu sollte die [Anleitung](./geosplitter/README.md) befolgt werden.

Im Fall der zur Zeit bereitgestellten `trees.json` musste **vor** der Geosplitting eine Bereinigung der Daten erfolgen. 
Dazu kann das `./geosplitter/filter_geodata.py`-Skript genutzt werden.

Kopiere anschließend die neu erstellten Segmente aus `./geosplitting/segments/*` in das `static`-Verzeichnis.

```bash
cp geosplitter/segments static
```


## Entwicklung

Installiere die Abhängigkeiten, bevor du mit der Entwicklung beginnst:

```
npm install
```

Anschließend kannst du das mit Svelte entwickelte Frontend starten:

```
npm run dev
```