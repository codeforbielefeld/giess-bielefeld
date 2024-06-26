# Giess Bielefeld

TODO: Beschreibung hinzufügen.

## Setup

### Supabase-Instanz starten

Für die lokale Entwicklung muss eine Supabase-Instanz aufgesetzt werden.

**Supabase** ist eine Open-Source-Plattform, die eine vollständige Backend-Infrastruktur mit Funktionen wie Datenbanken, Authentifizierung, Speicher und API-Generierung bietet, um schnell und einfach moderne Anwendungen zu entwickeln.

Hierfür kann die [`supabase-cli`](https://supabase.com/docs/guides/cli) verwendet werden.

```
npm install -g supabase-cli
```

Da die supabase-cli im Hintergrund Docker nutzt, musst du den Docker Daemon starten (ggf. noch zuerst Docker Desktop installieren), bevor du die supabase-cli starten kannst:

```
supabase start
```
Idealerweise erhältest du dann im Terminal eine Meldung "Started supabase local development setup." mit verschiednen Werten.

Darunter findest du auch die Studio URL mit der du Supabase Studio im Browser kannst. aufrufen.

Zudem sind für uns sind besonders die folgenden Eigenschaften (Zugangsdaten für die Supabase-Instanz) relevant:
- "anon key"
- "service_role key"

Diese Werte kopierst du bitte in eine .env kopieren (die der Struktur von der .env.example - Datei des Projektes folgt) für die entsprechenden Eigenschaften "VITE_SUPABASE_ANON_KEY" und "SUPABASE_SERVICE_ROLE_KEY".

```
VITE_SUPABASE_URL=http://127.0.0.1:54321
VITE_SUPABASE_ANON_KEY=
SUPABASE_SERVICE_ROLE_KEY=
```


Abschließend noch ausführen:

```
supabase migrations up
```

### Berechtigungen

Um auf die Supabase-Instanz und die darin enthaltenen Daten zugreifen zu können, müssen die Berechtigungen für die
Tabelle `trees` vergeben werden.
1.) Dazu kann das Supabase Studio unter der URL http://127.0.0.1:54323 geöffnet werden, solange die Supabase im Hintergrund
läuft. Dort kann die Tabelle `trees` ausgewählt und die Berechtigungen für die Tabelle vergeben werden:
2.) In der linken Seitenleiste wird der Table Editor ausgewählt.
3.) In der geöffneten Ansicht wählst du dann die Tabelle `trees` aus.
"RLS disabled" -> "Enable RLS for this table" -> "Enable RLS" -> "Add RLS policy" -> "Create a new policy"

Wähle das Template "SELECT: Enable read access for all users" 

```
create policy "Enable read access for all users" on "public"."trees" as permissive for select to public using (true);
```
und anschließend mit Klick auf `Save policy` speichern.

-> oder in `/supabase/migrations/20240316110547_create_trees_table` speichern

???

### Datenimport

Für den Import der Daten wird die `trees.json`-Datei benötigt, die aktuell nicht Bestandteil dieses Repositorys ist!


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