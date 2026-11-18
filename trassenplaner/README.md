# DB InfraGO – Trassen- & Kabelnetz-Planer (Preview)

Lauffähige Preview-App des Prototyps `index.html`. Reines Frontend, keine Installation nötig.

## Starten

```bash
python3 trassenplaner/server.py            # http://127.0.0.1:8000/
python3 trassenplaner/server.py --port 9000
```

Die Seite liegt danach unter `http://127.0.0.1:8000/` (bzw. dem gewählten Port).

## Hinweise

- Tailwind CSS (`cdn.tailwindcss.com`) und Lucide-Icons (`unpkg.com`, Version 0.460.0) werden von CDNs geladen. Ohne Zugriff auf diese Hosts fehlen Styles und Icons.
- Daten sind Demo-Daten im Skript (`INFRA_DATA`). Änderungen werden nicht gespeichert.
- Rollen lassen sich oben rechts umschalten (ADMIN, PLANER, BAULEITER, VIEWER).
