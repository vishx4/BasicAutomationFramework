import unittest
import pandas as pd
from pandas.testing import assert_frame_equal, assert_series_equal
import os
import sys

# Adjust path to import from parent directory (project_chatbot)
# This assumes the test is run from the root directory containing 'project_chatbot'
# or that 'project_chatbot' is in PYTHONPATH.
# For 'python -m unittest project_chatbot.tests.test_chatbot_logic' from root, this is fine.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from chatbot import load_status_data, get_status_by_name, get_all_statuses

class TestChatbotLogic(unittest.TestCase):

    def setUp(self):
        """Set up test fixtures, including a temporary Excel file."""
        self.test_excel_file_path = "test_project_status.xlsx"
        self.test_excel_missing_sheet_path = "test_missing_sheet.xlsx"
        self.test_excel_missing_column_path = "test_missing_column.xlsx"

        self.sample_data = {
            'Junior_Name': ['Alice', 'Bob', 'alice', 'Charlie', None, 'Diana'],
            'Project_Name': ['Alpha Proj', 'Beta Proj', 'Gamma Proj', 'Delta Proj', 'Epsilon Proj', 'Zeta Proj'],
            'Current_Task': ['Dev Login', 'Test UI', 'Plan Sprint', 'Write Docs', 'Setup Env', 'Review Code'],
            'Task_Status': ['In Progress', 'Completed', 'In Progress', 'Blocked', 'Pending', 'In Progress'],
            'Blockers': ['API Issue', None, None, 'Needs Review', None, 'Merge Conflict'],
            'Estimated_Completion_Date': ['2024-09-01', '2024-07-20', '2024-09-15', '2024-08-25', 'invalid-date', '2024-08-05'],
            'Last_Updated': ['2024-07-30', '2024-07-19', '2024-07-28', '2024-07-29', '2024-07-27', '2024-08-01']
        }
        self.df_sample = pd.DataFrame(self.sample_data)

        # Create the main test Excel file
        self.df_sample.to_excel(self.test_excel_file_path, sheet_name="Sheet1", index=False)

        # Create a file with a different sheet name for testing missing sheet
        df_temp_sheet = pd.DataFrame({'A': [1], 'B': [2]})
        df_temp_sheet.to_excel(self.test_excel_missing_sheet_path, sheet_name="Sheet2", index=False)

        # Create a file with a missing column for testing
        df_missing_col = self.df_sample.copy()
        del df_missing_col['Current_Task']
        df_missing_col.to_excel(self.test_excel_missing_column_path, sheet_name="Sheet1", index=False)

        # Load the main sample data into self.df for relevant tests
        self.df = load_status_data(self.test_excel_file_path)


    def tearDown(self):
        """Tear down test fixtures, removing temporary files."""
        if os.path.exists(self.test_excel_file_path):
            os.remove(self.test_excel_file_path)
        if os.path.exists(self.test_excel_missing_sheet_path):
            os.remove(self.test_excel_missing_sheet_path)
        if os.path.exists(self.test_excel_missing_column_path):
            os.remove(self.test_excel_missing_column_path)

    # --- Test cases for load_status_data ---
    def test_load_valid_excel_file(self):
        df = load_status_data(self.test_excel_file_path)
        self.assertIsNotNone(df)
        self.assertEqual(len(df), len(self.sample_data['Junior_Name']))
        self.assertEqual(len(df.columns), len(self.sample_data.keys()))
        self.assertListEqual(list(df.columns), list(self.sample_data.keys()))

        # Check date parsing (valid dates should be datetime, 'invalid-date' should be NaT)
        self.assertTrue(pd.api.types.is_datetime64_any_dtype(df['Estimated_Completion_Date']))
        self.assertTrue(pd.api.types.is_datetime64_any_dtype(df['Last_Updated']))

        # Specifically check the row with 'invalid-date' which should result in NaT
        # In our sample, Epsilon Proj has 'invalid-date'
        epsilon_row_date = df[df['Project_Name'] == 'Epsilon Proj']['Estimated_Completion_Date'].iloc[0]
        self.assertTrue(pd.isna(epsilon_row_date), "Expected NaT for 'invalid-date'")


    def test_load_file_not_found(self):
        df = load_status_data("non_existent_file.xlsx")
        self.assertIsNone(df)

    def test_load_excel_missing_sheet(self):
        df = load_status_data(self.test_excel_missing_sheet_path)
        self.assertIsNone(df, "Expected None when 'Sheet1' is missing.")

    def test_load_excel_missing_column(self):
        df = load_status_data(self.test_excel_missing_column_path)
        self.assertIsNone(df, "Expected None when a required column is missing.")

    # --- Test cases for get_status_by_name ---
    def test_get_status_existing_name_single_entry(self):
        self.assertIsNotNone(self.df, "Setup failed: self.df was not loaded.")
        result_df = get_status_by_name(self.df, "Bob")
        self.assertIsNotNone(result_df)
        self.assertEqual(len(result_df), 1)
        self.assertEqual(result_df.iloc[0]['Junior_Name'], "Bob")

    def test_get_status_existing_name_multiple_entries_case_insensitive(self):
        self.assertIsNotNone(self.df, "Setup failed: self.df was not loaded.")
        result_df = get_status_by_name(self.df, "alice") # Search with lowercase
        self.assertIsNotNone(result_df)
        self.assertEqual(len(result_df), 2)
        # Check if both "Alice" and "alice" are present
        names_found = result_df['Junior_Name'].str.lower().tolist()
        self.assertIn("alice", names_found)
        # Ensure original casing is preserved
        original_names = result_df['Junior_Name'].tolist()
        self.assertTrue("Alice" in original_names or "alice" in original_names)


    def test_get_status_non_existing_name(self):
        self.assertIsNotNone(self.df, "Setup failed: self.df was not loaded.")
        result_df = get_status_by_name(self.df, "David")
        self.assertIsNone(result_df) # Function should return None if not found

    def test_get_status_with_none_dataframe(self):
        result_df = get_status_by_name(None, "Alice")
        self.assertIsNone(result_df)

    def test_get_status_with_empty_dataframe(self):
        empty_df = pd.DataFrame(columns=self.sample_data.keys()) # Ensure it has expected columns
        result_df = get_status_by_name(empty_df, "Alice")
        self.assertIsNone(result_df) # Should be None for empty dataframe as well

    def test_get_status_name_is_none_in_data(self): # Test searching for 'None' if it's a name
        self.assertIsNotNone(self.df, "Setup failed: self.df was not loaded.")
        # The sample data has a row where Junior_Name is None.
        # .astype(str).str.lower() converts None to "none"
        result_df = get_status_by_name(self.df, "none")
        self.assertIsNotNone(result_df)
        self.assertEqual(len(result_df), 1)
        self.assertEqual(result_df.iloc[0]['Project_Name'], "Epsilon Proj")


    # --- Test cases for get_all_statuses ---
    def test_get_all_statuses_with_valid_data(self):
        self.assertIsNotNone(self.df, "Setup failed: self.df was not loaded.")
        result_df = get_all_statuses(self.df)
        self.assertIsNotNone(result_df)
        self.assertEqual(len(result_df), len(self.df_sample))
        # Using pandas testing function for more robust comparison if needed
        assert_frame_equal(result_df.reset_index(drop=True), self.df.reset_index(drop=True))


    def test_get_all_statuses_with_none_dataframe(self):
        result_df = get_all_statuses(None)
        self.assertIsNone(result_df)

    def test_get_all_statuses_with_empty_dataframe(self):
        empty_df = pd.DataFrame()
        result_df = get_all_statuses(empty_df)
        self.assertIsNone(result_df) # Current implementation returns None for empty


if __name__ == '__main__':
    # Ensures that the script can be run directly for testing.
    # The test runner (like 'python -m unittest ...') will discover tests without this,
    # but it's good practice for direct execution.
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
