
This Python script calculates the Semester Grade Point Average (SGPA) based on subject grades and credit hours.  It supports both manual input and reading data from an XML file.

## Features

* Calculates SGPA.
* Supports manual input of grades and credits.
* Reads grades and credits from an XML file (`grades.xml`).
* Error handling for invalid input and XML file issues.
* Clear output of the calculated SGPA.

## How to Use

1.  **Prerequisites:**
    * Python 3.x installed.
    * (Optional) An XML file named `grades.xml` with the correct format if you choose the XML input method.

2.  **Running the script:**

    * Save the Python script (e.g., `sgpa_calculator.py`).
    * Open your terminal or command prompt.
    * Navigate to the directory where you saved the script.
    * Run the script using: `python sgpa_calculator.py`

3.  **Input:**

    * The script will prompt you to choose between:
        * `manual`:  Enter grades and credits manually.
        * `xml`: Read data from the `grades.xml` file.
    * Follow the on-screen instructions to provide the required information.

### XML Input Format (`grades.xml`)

```xml
<gradesheet>
  <subject>
    <grade>A+</grade>
    <credit>4</credit>
  </subject>
  <subject>
    <grade>B</grade>
    <credit>3</credit>
  </subject>
  </gradesheet>

