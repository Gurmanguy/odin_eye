import gspread
from google.oauth2.service_account import Credentials
from gspread.exceptions import WorksheetNotFound

class SheetExporter:
    """
    Handles exporting data tables to Google Sheets via the gspread client.
    """
    def __init__(self, cred_path: str, spreadsheet_id: str):
        scopes = ["https://www.googleapis.com/auth/spreadsheets"]
        creds = Credentials.from_service_account_file(cred_path, scopes=scopes)
        client = gspread.authorize(creds)
        self.workbook = client.open_by_key(spreadsheet_id)

    def write(self, worksheet_title: str, data: list[list]):
        """
        Write a 2D list to the specified worksheet tab, starting at A1,
        clearing existing content and bolding the header. If the tab
        doesn’t exist, it will be created.

       
        """
        try:
            ws = self.workbook.worksheet(worksheet_title)
        except WorksheetNotFound:
            # Create the worksheet with enough rows and columns
            rows = len(data)
            cols = len(data[0]) if data else 1
            ws = self.workbook.add_worksheet(worksheet_title, rows, cols)

        ws.clear()

        # Write data starting at cell A1
        ws.update("A1", data)

        # Bold the header row
        if data:
            last_col = chr(ord('A') + len(data[0]) - 1)
            ws.format(f"A1:{last_col}1", {"textFormat": {"bold": True}})

# TODO: Add CSV export option for local file output
# TODO: Add google OAuth authntication
# TODO: Add NXLog JSON ingestion support
