# Job-Application-Tracker
Job Application Tracker is a simple Python command-line tool to help you manage your internship and job applications. It allows you to add, view, and update application statuses, storing all data persistently in a JSON file. This project demonstrates skills in Python scripting, file handling, and data organization.
## Features

- Add new job applications with company name, role, and status.
- View all saved applications.
- Update the status of existing applications.
- Data is saved persistently in a JSON file (`data.json`) so your applications are stored between runs.

## How to Run

1. Make sure you have Python installed (Python 3.x recommended).
2. Clone this repository or download the files.
3. Open a terminal and navigate to the project folder.
4. Run the program:
    ```bash
    python tracker.py
    ```
5. Follow the on-screen menu options:
    - **1** to add a new application
    - **2** to view all saved applications
    - **3** to update the status of an existing application
    - **4** to exit the program

## How Stored Data Works

- All job applications you enter are saved in a file named `data.json` in the project directory.
- This file is automatically created when you add your first application.
- You can open `data.json` in any text editor to see your saved data in JSON format.

Example `data.json` content:

```json
[
    {
        "company": "Google",
        "role": "SDE Intern",
        "status": "Applied"
    },
    {
        "company": "Amazon",
        "role": "Software Developer",
        "status": "Interviewing"
    }
]

