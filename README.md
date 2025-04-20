# Odin_Eye

A lightweight CLI tool for collecting live process and network activity and exporting it to Google Sheets.
Made for fun and practice!

## Features

- **Process Data Collection**: Gather process details including PID, command line, executable path, parent PID, and username.
- **Network Connection Data**: Capture active network connections with process context such as local and remote addresses and connection status.
- **Google Sheets Export**: Push the collected data directly into designated tabs of a Google Spreadsheet.
- **CLI Interface**: Simple command-line flags to select data mode and target worksheet.

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Gurmanguy/odin_eye.git
   cd odin_eye
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
 ## Development Setup

We use a Python virtual environment to isolate dependencies:

```bash
# 1. Create a venv in the project root
python3 -m venv .venv

# 2. Activate it
# Windows (PowerShell):
.venv\Scripts\Activate.ps1

# 3. Install the project in editable mode
pip install -e .

## Usage

```bash
odin_eye --creds /path/to/credentials.json --sheet-id YOUR_SHEET_ID [--mode procs|net]
```

- `--creds` : Path to your Google service account JSON file (requires Editor access to the sheet).  
- `--sheet-id` : The ID of the Google Spreadsheet (found in its URL).  
- `--mode` : `procs` for process data (default), `net` for network connection data, or both when repeated.

### Examples

- **Process data** (default tab "Process Logs"):
  ```bash
  odin_eye --creds cred.json --sheet-id ID
  ```

- **Network data** (default tab "Network Logs"):
  ```bash
  odin_eye --creds cred.json --sheet-id ID --mode net
  ```

- **Both modes**:
  ```bash
  odin_eye --creds cred.json --sheet-id ID --mode procs net
  ```

## Configuration

1. **Create a Google service account** with the Sheets API enabled.  
2. **Share** your target spreadsheet with the service account’s email address, granting Editor permissions.  
3. **Obtain** the service account JSON key file and pass its path via `--creds`.

## Roadmap

- **NXLog JSON Integration**: Ingest process and network data via NXLog’s JSON output.  
- **Local CSV Export**: Add an `--output csv` flag to save data locally as CSV files.  
- **Test Suite & CI**: Implement unit tests and set up GitHub Actions for continuous integration.

## Contributing

Contributions are welcome. Please open an issue or submit a pull request for any feature requests or bug fixes.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

Built by Guy Gurman.

