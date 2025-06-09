import pandas as pd
import os

# Define the Excel file path
excel_file_path = 'project_status.xlsx'

# Define the headers (for verification and in case the file is empty)
headers = [
    'Junior_Name',
    'Project_Name',
    'Current_Task',
    'Task_Status',
    'Blockers',
    'Estimated_Completion_Date',
    'Last_Updated'
]

# Sample data to add
sample_data = [
    ['Alice', 'Chatbot Feature X', 'Implement user login', 'In Progress', 'None', '2024-08-15', '2024-07-30'],
    ['Bob', 'Data Analysis Y', 'Clean dataset', 'Completed', '', '2024-07-25', '2024-07-24'],
    ['Charlie', 'UI Improvement Z', 'Design new dashboard mock', 'Blocked', 'API down', '2024-08-20', '2024-07-29']
]

# Create a DataFrame for the new data
df_new_data = pd.DataFrame(sample_data, columns=headers)

# Check if the file exists and read it. If not, or if it's empty/invalid, start fresh.
if os.path.exists(excel_file_path) and os.path.getsize(excel_file_path) > 0:
    try:
        df_existing = pd.read_excel(excel_file_path, sheet_name='Sheet1')
        # Ensure headers match - this is a simple check
        if not list(df_existing.columns) == headers:
            print("Existing file has incorrect headers. Will overwrite with new data and correct headers.")
            df_to_write = df_new_data
        else:
            # Append new data
            df_to_write = pd.concat([df_existing, df_new_data], ignore_index=True)
    except Exception as e:
        print(f"Error reading existing Excel file: {e}. Will create a new file with the sample data.")
        df_to_write = df_new_data
else:
    print("Excel file not found or is empty. Creating a new file with sample data.")
    df_to_write = df_new_data

# Write the (potentially combined) DataFrame to the Excel file
try:
    df_to_write.to_excel(excel_file_path, index=False, sheet_name='Sheet1')
    print("Excel file updated successfully with sample data.")
except Exception as e:
    print(f"Error writing to Excel file: {e}")
