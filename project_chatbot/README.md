# Project Status CLI Chatbot

## Description

The Project Status CLI Chatbot is a command-line tool designed for QA leads (or any project manager) to quickly query and view the project statuses of junior team members. The chatbot reads its data from a structured Excel file (`project_status.xlsx`).

## Features

*   **View Status by Junior Name:** Get the current project status for a specific junior team member.
*   **View All Statuses:** Get a consolidated view of project statuses for all junior team members.
*   **Reload Data:** Refresh the data from the Excel file without restarting the chatbot.
*   **Interactive CLI:** Simple command-line interface for easy interaction.
*   **Error Handling:** Provides feedback for incorrect commands or issues with data loading.

## Setup Instructions

### Prerequisites

*   Python 3.7 or higher
*   pip (Python package installer, usually comes with Python)

### Installation

1.  **Clone the Repository / Download Files:**
    Obtain the project files (e.g., by cloning a Git repository or downloading a ZIP).

2.  **Navigate to the Project Directory:**
    Open your terminal or command prompt and change to the `project_chatbot` directory:
    ```bash
    cd path/to/project_chatbot
    ```

3.  **Create a Virtual Environment (Recommended):**
    It's highly recommended to use a virtual environment to manage project dependencies.
    ```bash
    python -m venv venv
    ```
    Activate the virtual environment:
    *   On macOS and Linux:
        ```bash
        source venv/bin/activate
        ```
    *   On Windows:
        ```bash
        venv\Scripts\activate
        ```

4.  **Install Dependencies:**
    Install the required Python packages using the `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```
    The `requirements.txt` file should contain:
    ```
    pandas
    openpyxl
    ```

### Excel File Setup (`project_status.xlsx`)

The chatbot requires an Excel file named `project_status.xlsx` to be present in the same directory as the `chatbot.py` script.

**Required Columns:**

The Excel file **must** have a sheet named `Sheet1` with the following columns in the first row:

1.  `Junior_Name`: The name of the junior team member.
2.  `Project_Name`: The name of the project they are working on.
3.  `Current_Task`: The specific task they are currently handling.
4.  `Task_Status`: The status of the current task (e.g., In Progress, Completed, Blocked, Pending).
5.  `Blockers`: Any issues or blockers they are facing (can be empty).
6.  `Estimated_Completion_Date`: The estimated date for completing the current task (e.g., YYYY-MM-DD). Invalid dates will be shown as "N/A".
7.  `Last_Updated`: The date when the status was last updated by the junior (e.g., YYYY-MM-DD). Invalid dates will be shown as "N/A".

**Example Data in `Sheet1`:**

| Junior_Name | Project_Name      | Current_Task              | Task_Status | Blockers    | Estimated_Completion_Date | Last_Updated |
|-------------|-------------------|---------------------------|-------------|-------------|---------------------------|--------------|
| Alice       | Chatbot Feature X | Implement user login      | In Progress | API down    | 2024-08-15                | 2024-07-30   |
| Bob         | Data Analysis Y   | Clean dataset             | Completed   |             | 2024-07-25                | 2024-07-24   |
| Charlie     | UI Improvement Z  | Design new dashboard mock | Blocked     | Needs Review| 2024-08-20                | 2024-07-29   |

**Updating the Excel File:**
Junior team members are responsible for keeping their project status updated in this `project_status.xlsx` file. They should regularly edit the file to reflect their current tasks, progress, and any blockers. The chatbot will then read this file to provide the latest information.

## How to Run the Chatbot

Ensure you are in the `project_chatbot` directory and have activated the virtual environment (if used).

Run the chatbot script using Python:
```bash
python chatbot.py
```
This will start the interactive command-line interface.

## Available Commands

The chatbot accepts the following commands:

*   `status <Junior_Name>`: Shows the current project status for the specified junior team member.
    *   Example: `status Alice`
*   `status all`: Displays the project statuses for all junior team members listed in the Excel file.
*   `reload`: Reloads the data from the `project_status.xlsx` file. Use this if the Excel file has been updated while the chatbot is running.
*   `help`: Shows the list of available commands and their usage.
*   `exit`: Exits the chatbot.

## How to Run Unit Tests

The project includes unit tests to verify the core logic of the chatbot.

To run the tests, navigate to the **parent directory** of `project_chatbot` (e.g., if your project is in `C:\Projects\MyChatbot\project_chatbot`, navigate to `C:\Projects\MyChatbot`). Then, run the following command:

```bash
python -m unittest project_chatbot.tests.test_chatbot_logic
```

Alternatively, if you are already inside the `project_chatbot` directory, you can try:
```bash
python -m unittest tests.test_chatbot_logic
```
However, the primary method tested during development assumes running from the parent directory of `project_chatbot` due to how Python's module discovery works with the `sys.path` modification in the test script.

---
This `README.md` provides a comprehensive guide for users and developers of the Project Status CLI Chatbot.
