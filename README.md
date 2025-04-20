Odin_Eye

A lightweight CLI tool for collecting live process and network activity and exporting it to Google Sheets.

Features

Process Data Collection

PID

Command line arguments

Executable path

Parent PID

Username

Network Connection Data

Local and remote addresses

Connection status

Associated process context

Google Sheets Export

Writes directly to named worksheet tabs in a Google Spreadsheet

Command-Line Interface

Select one or both data modes (procs, net)

Specify credentials and spreadsheet ID

Installation

Clone the repository:

git clone https://github.com/Gurmanguy/odin_eye.git
cd odin_eye

(Optional) Create and activate a virtual environment:

python3 -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
# macOS/Linux
source .venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Or install the package itself:

pip install .

Usage

Run both process and network collection (default):

odin_eye --creds /path/to/credentials.json --sheet-id YOUR_SHEET_ID

Run only process logs:

odin_eye --creds /path/to/credentials.json --sheet-id YOUR_SHEET_ID --mode procs

Run only network logs:

odin_eye --creds /path/to/credentials.json --sheet-id YOUR_SHEET_ID --mode net

Command-Line Arguments

--creds (required): Path to Google service account JSON file

--sheet-id (required): Google Spreadsheet ID (from the URL)

--mode: One or more of procs (process logs) and net (network logs). Default is both.

Configuration

Create a Google service account and enable the Sheets API.

Share your target spreadsheet with the service account email (Editor role).

Use the --creds flag to point to the downloaded key JSON.

Roadmap

NXLog JSON integration

Local CSV export via --output csv

Unit tests and CI workflow
