# Discord-Bot für Rollenmanagement

Ein Discord-Bot, der Slash-Commands bereitstellt, um Rollen auf einem Discord-Server zu verwalten. Der Bot ermöglicht Administratoren, eine erlaubte Rolle festzulegen, und Moderatoren mit der entsprechenden Berechtigung, Rollen zu Nutzern hinzuzufügen oder zu entfernen.

## Funktionen
- **/set_allowed_role**: Legt die Rolle fest, die den Bot nutzen darf (nur für Administratoren).
- **/add_role**: Fügt einem Nutzer eine Rolle hinzu (für Moderatoren mit „Manage Roles“-Berechtigung und der erlaubten Rolle).
- **/remove_role**: Entfernt eine Rolle von einem Nutzer (für Moderatoren mit „Manage Roles“-Berechtigung und der erlaubten Rolle).

## Voraussetzungen
- **Python**: Version 3.8 oder höher (getestet mit Python 3.10/3.13).
- **Discord Developer Portal**: Ein Bot-Token und korrekte Einstellungen (siehe unten).
- **Betriebssystem**: Windows (getestet), Linux oder macOS sollten ebenfalls funktionieren.
- **Visual Studio Code** oder ein anderer Code-Editor (empfohlen für die Entwicklung).

## Installation

1. **Ordnerstruktur**:
   - Stelle sicher, dass folgende Dateien im Ordner `Bot für das TagSystem` vorhanden sind:
     - `bot.py`: Der Hauptcode des Bots.
     - `.env`: Enthält den Bot-Token.
     - `requirements.txt`: Listet die benötigten Python-Bibliotheken.

2. **Python installieren**:
   - Lade Python 3.8+ von [python.org](https://www.python.org/downloads/) herunter.
   - Stelle sicher, dass „Add Python to PATH“ während der Installation aktiviert ist.
   - Überprüfe die Installation im Terminal:
     ```
     python --version
     ```

3. **Bibliotheken installieren**:
   - Öffne ein Terminal in Visual Studio Code (Menü > Terminal > Neues Terminal).
   - Wechsle zu `cmd` (falls PowerShell geöffnet wird):
     ```
     cmd
     ```
   - Navigiere zum Ordner:
     ```
     cd C:\Users\DEIN_BENUTZERNAME\Desktop\Bot für das TagSystem
     ```
   - Installiere die Bibliotheken:
     ```
     pip install -r requirements.txt
     ```
   - Überprüfe die Installation:
     ```
     pip show discord.py
     pip show python-dotenv
     ```

4. **Bot-Token einrichten**:
   - Gehe zu [discord.com/developers/applications](https://discord.com/developers/applications).
   - Wähle deine Bot-Anwendung > **Bot** > **Token** > **Copy**.
   - Öffne `.env` und füge den Token hinzu:
     ```
     BOT_TOKEN=DEIN_BOT_TOKEN
     ```
   - Speichere die Datei als `.env` (nicht `.env.txt`).

5. **Bot im Developer Portal einrichten**:
   - Gehe zu **Bot** > **Privileged Gateway Intents**:
     - ☑ **Presence Intent**
     - ☑ **Server Members Intent**
   - Gehe zu **OAuth2 > URL Generator**:
     - Scopes: ☑ **bot**, ☑ **applications.commands**
     - Bot Permissions: ☑ **View Channels**, ☑ **Send Messages**, ☑ **Manage Roles**
   - Kopiere die URL, öffne sie im Browser und lade den Bot zu deinem Server ein.

## Nutzung
1. **Bot starten**:
   - Öffne ein `cmd`-Terminal in VS Code:
     ```
     cd C:\Users\DEIN_BENUTZERNAME\Desktop\Bot für das TagSystem
     python bot.py
     ```
   - Erwartete Ausgabe:
     ```
     Bot ist online als DeinBotName#1234!
     Slash-Commands synchronisiert.
     ```
2. **Slash-Commands verwenden**:
   - Gehe in einen Textkanal deines Servers und tippe `/`.
   - Verfügbare Commands:
     - `/set_allowed_role role:@Rolle`: Legt die Rolle fest, die den Bot nutzen darf (nur für Admins).
     - `/add_role member:@Nutzer role:@Rolle`: Fügt einem Nutzer eine Rolle hinzu.
     - `/remove_role member:@Nutzer role:@Rolle`: Entfernt eine Rolle von einem Nutzer.
   - **Hinweis**: Die Commands erscheinen unter „Apps“ oder direkt beim Tippen von `/`. Dies kann bis zu einer Stunde dauern (globale Synchronisierung).

3. **Rollenhierarchie**:
   - Stelle sicher, dass die Bot-Rolle in Discord (Server-Einstellungen > Rollen) oberhalb der zu verwaltenden Rollen (z. B. „Mitglied“, „VIP“) und unterhalb der Moderator-Rolle liegt.
   - Der Bot benötigt die Berechtigungen „View Channels“, „Send Messages“, „Manage Roles“.

## Fehlerbehebung
- **Commands erscheinen nicht**:
  - Warte bis zu einer Stunde (globale Synchronisierung).
  - Überprüfe den `applications.commands`-Scope im Developer Portal.
  - Lade den Bot neu ein (OAuth2-URL).
  - Starte den Bot neu:
    ```
    python bot.py
    ```
  - Schließe Discord und starte es neu, um Cache-Probleme zu beheben.
- **„Invalid Token“**:
  - Überprüfe den Token in `.env` (keine Leerzeichen, Anführungszeichen oder Zeilenumbrüche).
  - Kopiere den Token neu aus dem Developer Portal (Bot > Token > Copy).
- **„ModuleNotFoundError: No module named 'discord'“**:
  - Installiere die Bibliotheken neu:
    ```
    pip install -r requirements.txt
    ```
  - Verwende `cmd` statt PowerShell im Terminal.
- **„Keine Berechtigung“**:
  - Stelle sicher, dass die Bot-Rolle „Manage Roles“ hat.
  - Nur Nutzer mit „Administrator“ können `/set_allowed_role` nutzen; „Manage Roles“ ist für `/add_role` und `/remove_role` erforderlich.

## Dateistruktur
# Bot für das TagSystem             
# Hauptcode des Bots        ├── bot.py                
# Bot-Token (BOT_TOKEN=DEIN_BOT_TOKEN)      ├── .env    
# Benötigte Bibliotheken (discord.py, python-dotenv)        ├── requirements.txt
# Diese Datei       ├── README.md

## Hinweise
- Halte den Bot-Token geheim und teile ihn nicht öffentlich.
- Wenn du den Ordner schließen willst, ohne etwas zu löschen:
  - Stoppe den Bot mit `Ctrl + C` im Terminal.
  - Gehe zu **Datei > Ordner schließen** in VS Code.
- Für weitere Fragen oder Anpassungen wende dich an den Entwickler oder die Dokumentation von `discord.py`.

## Lizenz
- Dieses Projekt ist für den privaten Gebrauch gedacht. Keine offizielle Lizenz definiert.