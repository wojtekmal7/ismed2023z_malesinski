# Blood Test Manager (Python CLI App)

This is a simple console-based application for managing patient blood test data. It allows you to enter, display, search, save, load, and delete test results stored in memory or a file. The program is fully interactive and operated through a terminal menu.

## Features

- Add a new blood test entry (with input validation)
- Display all loaded test results
- Save all tests to a `.json` file
- Load test data from a `.json` file
- Search tests by PESEL number (Polish national ID)
- Delete a selected test for a given patient
- Clear all loaded data

## File Format

The test results are saved and loaded from `.json` files. Each test entry includes:

- First name
- Last name
- PESEL number (11 digits)
- Erythrocytes count
- Leukocytes count
- Platelets count

Example (in JSON array of strings format):
```json
[
  "99658704392 Eustachy Nowak 34 4444 566556",
  "44556600449 Piotr Glowacki 23123 2323 2323"
]
```
How to Use
Run the main.py script.

Follow the on-screen menu options:

1 - Add a new blood test

2 - Display all loaded tests

3 - Save data to file

4 - Load data from file

5 - Search for a patient by PESEL

6 - Delete a test by PESEL

7 - Exit

Requirements
This project requires Python 3.x. No external libraries are needed — everything runs with the standard library.

Notes
PESEL must contain exactly 11 digits.

Data validation is included for numeric fields.

Test files must be correctly formatted, otherwise an error message will be shown.

All PESELs and names are fictional. No real patient data is included due to privacy concerns.

License
This project is intended for educational and demonstration purposes.
