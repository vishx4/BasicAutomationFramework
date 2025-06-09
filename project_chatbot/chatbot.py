import pandas as pd
import sys # For sys.exit()

def load_status_data(filepath: str) -> pd.DataFrame | None:
    """
    Loads project status data from an Excel file.
    Converts relevant date columns to datetime objects.
    Handles file not found, sheet not found, and other read errors.
    """
    expected_columns = [
        'Junior_Name', 'Project_Name', 'Current_Task',
        'Task_Status', 'Blockers', 'Estimated_Completion_Date', 'Last_Updated'
    ]
    try:
        df = pd.read_excel(filepath, sheet_name='Sheet1')

        if df.empty:
            # This could happen if Sheet1 exists but is empty.
            # Or if read_excel for some reason returns empty on other non-exception errors.
            print(f"Warning: The sheet 'Sheet1' in {filepath} was found but appears to be empty.")
            # We can decide to return an empty DataFrame or None.
            # For consistency with "missing columns" or other data issues, let's return None.
            # If an empty DataFrame is desired, 'return df' would be here.
            return None

        missing_columns = [col for col in expected_columns if col not in df.columns]
        if missing_columns:
            print(f"Error: The Excel file '{filepath}' (Sheet1) is missing the following columns: {', '.join(missing_columns)}")
            return None

        if 'Last_Updated' in df.columns:
            df['Last_Updated'] = pd.to_datetime(df['Last_Updated'], errors='coerce')
        if 'Estimated_Completion_Date' in df.columns:
            df['Estimated_Completion_Date'] = pd.to_datetime(df['Estimated_Completion_Date'], errors='coerce')

        return df
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
        return None
    except ValueError as ve: # Pandas often raises ValueError for sheet issues
        if "Worksheet named 'Sheet1' not found" in str(ve) or "No sheet named <Sheet1>" in str(ve) : # Example error messages
            print(f"Error: Could not find 'Sheet1' in the Excel file '{filepath}'. Details: {ve}")
        else:
            print(f"Error: Could not process data in '{filepath}'. Possible data format issue. Details: {ve}")
        return None
    except Exception as e: # Catch-all for other pandas or unexpected errors
        print(f"Error: Could not read or process the Excel file '{filepath}'. Details: {e}")
        return None

def get_status_by_name(data_df: pd.DataFrame, name: str) -> pd.DataFrame | None:
    """
    Filters the DataFrame for a specific name in 'Junior_Name' (case-insensitive).
    """
    if data_df is None or data_df.empty:
        return None
    if 'Junior_Name' not in data_df.columns:
        print("Error: 'Junior_Name' column not found in DataFrame for searching.") # More specific error
        return None

    matches = data_df[data_df['Junior_Name'].astype(str).str.lower() == name.lower()]
    return matches if not matches.empty else None

def get_all_statuses(data_df: pd.DataFrame) -> pd.DataFrame | None:
    """
    Returns the entire DataFrame if it's not None or empty.
    """
    if data_df is None or data_df.empty:
        return None
    return data_df

def display_data(df: pd.DataFrame | None):
    """
    Displays the DataFrame in a user-friendly format.
    Shows selected columns and handles NaT for date columns.
    """
    if df is None or df.empty:
        print("No status information to display.")
        return

    display_columns = [
        'Junior_Name', 'Project_Name', 'Current_Task',
        'Task_Status', 'Estimated_Completion_Date', 'Blockers', 'Last_Updated'
    ]
    existing_display_columns = [col for col in display_columns if col in df.columns]

    df_display = df[existing_display_columns].copy()

    # Handle NaT and format date columns for better readability
    date_cols_to_format = ['Estimated_Completion_Date', 'Last_Updated']
    for col_name in date_cols_to_format:
        if col_name in df_display.columns:
            # Fill NaT with "N/A" before attempting to format
            if pd.api.types.is_datetime64_any_dtype(df_display[col_name]):
                df_display[col_name] = df_display[col_name].fillna("N/A")
                # Apply strftime only to valid datetime objects, skip "N/A"
                df_display[col_name] = df_display[col_name].apply(lambda x: x.strftime('%Y-%m-%d') if isinstance(x, pd.Timestamp) else x)
            else: # If it's not a datetime (e.g. already string due to mixed types from coerce)
                df_display[col_name] = df_display[col_name].fillna("N/A")


    print(df_display.to_string(index=False))


if __name__ == "__main__":
    EXCEL_FILE_PATH = "project_status.xlsx"
    print("Loading initial project status data...")
    data_df = load_status_data(EXCEL_FILE_PATH)

    if data_df is None:
        print("Exiting due to data loading failure. Please check 'project_status.xlsx' and its 'Sheet1'.")
        sys.exit(1)

    print("Data loaded successfully. Welcome to the Project Status Chatbot!")

    while True:
        command_input = input("\nEnter command (type 'help' for options): ").strip()
        if not command_input:
            continue

        parts = command_input.split()
        command = parts[0].lower()
        args = parts[1:]

        if command == "help":
            if args:
                print("Info: 'help' command does not take any arguments. They will be ignored.")
            print("\nAvailable commands:")
            print("  status <Junior_Name>  - Show status for a specific junior (e.g., status Alice).")
            print("  status all            - Show status for all juniors.")
            print("  reload                - Reload data from the Excel file.")
            print("  exit                  - Exit the chatbot.")
            print("  help                  - Show this help message.")

        elif command == "exit":
            if args:
                print("Info: 'exit' command does not take any arguments. They will be ignored.")
            print("Exiting chatbot. Goodbye!")
            break

        elif command == "reload":
            if args:
                print("Info: Arguments to 'reload' (like '{}') are ignored.".format(" ".join(args)))
            print("Reloading data...")
            reloaded_data_df = load_status_data(EXCEL_FILE_PATH)
            if reloaded_data_df is None:
                print(f"Failed to reload data from '{EXCEL_FILE_PATH}'. Please check the file and 'Sheet1'.")
                print("The chatbot might not have data until a successful reload or restart.")
                data_df = None
            else:
                data_df = reloaded_data_df
                print("Data reloaded successfully.")

        elif command == "status":
            if data_df is None:
                print(f"Data not currently loaded. Please try 'reload' to load from '{EXCEL_FILE_PATH}'.")
                continue

            if len(args) == 0:
                print("Please specify a junior's name or 'all'. Usage: status <Name> OR status all")
            elif args[0].lower() == "all":
                if len(args) > 1:
                    print("Info: Extra arguments for 'status all' (like '{}') are ignored.".format(" ".join(args[1:])))
                all_statuses_df = get_all_statuses(data_df)
                display_data(all_statuses_df)
            else:
                name_to_find = " ".join(args)
                status_df = get_status_by_name(data_df, name_to_find)
                if status_df is not None and not status_df.empty:
                    display_data(status_df)
                else:
                    print(f"No status found for '{name_to_find}'.")

        else:
            print(f"Invalid command: '{command}'. Type 'help' for options.")
