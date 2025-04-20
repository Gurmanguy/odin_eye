Odin_Eye
                                                              

A lightweight CLI tool for collecting live process and network activity and exporting it to Google Sheets.

Features:

Process Data Collection: Gather process details (PID, command line, executable path, parent PID, username).
Network Connection Data: Capture active network connections with process context (local/remote addresses, status).
Google Sheets Export: Push collected data directly to a specified Google Sheet tab.
CLI Interface: Easy-to-use command-line flags to choose data mode and target sheet.

Installation

Clone the repository

git clone https://github.com/Gurmanguy/Odin_Eye.git
cd Odin_Eye

Install dependencies

pip install -r requirements.txt
# or install directly
pip install .

Usage

odin_eye --creds path/to/credentials.json --sheet-id YOUR_SHEET_ID [--mode procs|net] [--sheet-name SHEET_TAB]

--creds : Path to your Google service account JSON file.

--sheet-id : ID of the Google Sheet where data will be written.

--mode : procs for process data (default), net for network connection data.

--sheet-name : (Optional) Name of the worksheet tab. Defaults to Sheet1 for processes and Sheet2 for network.

Examples

Write process data to default tab:

odin_eye --creds cred.json --sheet-id 1ABCdefGHIjklMNOpQRs

Write network data to a custom tab:

odin_eye --creds cred.json --sheet-id 1ABCdefGHIjklMNOpQRs --mode net --sheet-name "Connections"

Configuration

Service Account: Create a Google service account and grant it Editor access to your target sheet.
 
Export service users credentials via JSON file (includes authentication for Gsheet integration)


Roadmap

#NXLog JSON Integration: Ingest process and network data via NXLog’s JSON output.

#Local CSV Export: Add a flag (--output csv) to save data locally as CSV files.

#Test Suite & CI: Implement unit tests and GitHub Actions for continuous integration.


Built with :eye: by Guy Gurman
PS: made for fun and practice
