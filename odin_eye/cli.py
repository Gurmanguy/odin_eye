import argparse
from .inspector import ProcessInspector, NetworkInspector
from .exporter import SheetExporter


def write_data(exporter, mode):
    """
    Collect and write data for the given mode to the corresponding worksheet tab.
    """
    if mode == 'procs':
        worksheet_title = 'Process Logs'
        data = ProcessInspector().collect()
    elif mode == 'net':
        worksheet_title = 'Network Logs'
        data = NetworkInspector().collect()
    else:
        raise ValueError(f"Unsupported mode: {mode}")

    # Ensure the worksheet exists (create if missing)
    try:
        exporter.workbook.worksheet(worksheet_title)
    except Exception as e:
        # Create worksheet with appropriate size
        exporter.workbook.add_worksheet(
            title=worksheet_title,
            rows=str(len(data)),
            cols=str(len(data[0]))
        )
    exporter.write(worksheet_title, data)
    print(f"YESSIR success {mode.upper()} data written to '{worksheet_title}'")


def main():
    parser = argparse.ArgumentParser(
        description="Odin_Eye: collect process & network info into Google Sheets"
    )
    parser.add_argument(
        '--creds', required=True,
        help='Path to Google service account JSON file'
    )
    parser.add_argument(
        '--sheet-id', required=True,
        help='Google Spreadsheet ID to write data into'
    )
    parser.add_argument(
        '--mode', nargs='+', choices=['procs', 'net'],
        default=['procs', 'net'],
        help="Modes of data collection: 'procs' for process logs, 'net' for network logs"
    )

    args = parser.parse_args()
    exporter = SheetExporter(args.creds, args.sheet_id)

    for mode in args.mode:
        write_data(exporter, mode)


if __name__ == '__main__':
    main()