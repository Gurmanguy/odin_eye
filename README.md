Odin_Eye

A lightweight CLI tool for collecting live process and network activity and exporting it to Google Sheets.

Features

Process Data Collection: Gather process details (PID, command line, executable path, parent PID, username).

Network Connection Data: Capture active network connections with process context (local and remote addresses, status).

Google Sheets Export: Push collected data directly to specified worksheet tabs in a Google Spreadsheet.

Command-Line Interface: Easy-to-use flags for selecting data modes and target worksheets.

#Installation

Clone the repository

git clone https://github.com/Gurmanguy/odin_eye.git
cd odin_eye

Create and activate a virtual environment (optional but recommended)

python3 -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1


Install dependencies

pip install -r requirements.txt

Or install the package directly:

pip install .

Usage

odin_eye --creds path/to/credentials.json --sheet-id YOUR_SHEET_ID [--mode procs net]

--creds: Path to your Google service account JSON file.

--sheet-id: ID of the Google Spreadsheet (from the URL).

--mode: One or both of procs (process logs) and net (network logs); defaults to both.

Examples

# Export both process and network logs
odin_eye --creds cred.json --sheet-id 1ABCdefGHIjklMNOpQRs

# Export only process logs
odin_eye --creds cred.json --sheet-id 1ABCdefGHIjklMNOpQRs --mode procs

# Export only network logs
odin_eye --creds cred.json --sheet-id 1ABCdefGHIjklMNOpQRs --mode net

Configuration

Create a Google service account with the Sheets API enabled.

Share your target spreadsheet with the service account email (Editor role).

Point the --creds flag at the downloaded JSON key file.

Roadmap

NXLog JSON Integration: Ingest data via NXLog JSON output.

Local CSV Export: Add a --output csv option to save logs locally.

Test Suite & CI: Implement unit tests and a GitHub Actions workflow.

License

MIT License — see LICENSE for details.

Authored by Guy Gurman.
