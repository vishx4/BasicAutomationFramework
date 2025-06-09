import pandas as pd

# Define the headers
headers = [
    'Junior_Name',
    'Project_Name',
    'Current_Task',
    'Task_Status',
    'Blockers',
    'Estimated_Completion_Date',
    'Last_Updated'
]

# Create an empty DataFrame with these headers
df = pd.DataFrame(columns=headers)

# Write the DataFrame to an Excel file
try:
    df.to_excel('project_status.xlsx', index=False, sheet_name='Sheet1')
    print("Excel file created successfully.")
except Exception as e:
    print(f"Error creating Excel file: {e}")
