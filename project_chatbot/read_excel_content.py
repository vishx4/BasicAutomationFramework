import pandas as pd

excel_file_path = 'project_status.xlsx'

try:
    df = pd.read_excel(excel_file_path, sheet_name='Sheet1')
    # Print the DataFrame as CSV to stdout
    # This is a simple way to view the content in a text-based output
    print(df.to_csv(index=False))
except FileNotFoundError:
    print(f"Error: The file {excel_file_path} was not found.")
except Exception as e:
    print(f"Error reading or processing Excel file: {e}")
