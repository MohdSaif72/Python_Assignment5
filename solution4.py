import pandas as pd

def new_sheet(filepath, sheetname, columnheaders):
    """
    Create a new sheet in an existing Excel file with the specified column headers.

    Parameters:
    - filepath (str): Path to the existing Excel file.
    - sheetname (str): Name of the new sheet to be created.
    - columnheaders (list): List of column headers to be added to the new sheet.
    """
    try:
        xl = pd.ExcelFile(filepath)
        if sheetname in xl.sheet_names:
            return
        df = pd.DataFrame(columns=columnheaders)
        
        with pd.ExcelWriter(filepath, mode='a', engine='openpyxl') as writer:
            df.to_excel(writer, sheet_name=sheetname, index=False)

    except Exception as e:
        print(f"An error occurred: {e}")

filepath = "saucedemo.xlsx"
sheetname = "Order Details"
columnheaders = ["User ID", "Product Name", "Quantity", "Price"]
new_sheet(filepath, sheetname, columnheaders)
