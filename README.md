# DataFun-03-Analytics

This project demonstrates how to fetch and process various types of data (CSV, Excel, JSON, and text) using Python.  
It includes scripts to automate data acquisition and analysis, following a professional Python workflow.

---

## Project Structure

- **Fetchers:** Download data files from the web and save them locally.
- **Processors:** Analyze the downloaded data and save results to the `processed` folder.
- **Automation:** Run all fetchers and processors in sequence with a single script.

---

## Fetcher Scripts

| Script Name                      | Description                                                      |
|----------------------------------|------------------------------------------------------------------|
| michaeljmoore_get_csv.py         | Fetches a CSV file and saves it to the `data` folder.            |
| michaeljmoore_get_excel.py       | Fetches an Excel file and saves it to the `data` folder.         |
| michaeljmoore_get_json.py        | Fetches a JSON file and saves it to the `data` folder.           |
| michaeljmoore_get_text.py        | Fetches a text file and saves it to the `data` folder.           |

---

## Processor Scripts

| Script Name                      | Description                                                      |
|----------------------------------|------------------------------------------------------------------|
| michaeljmoore_process_csv.py     | Analyzes the CSV file for statistics (min, max, mean, stdev).    |
| michaeljmoore_process_excel.py   | Processes the Excel file to count occurrences of a word.         |
| michaeljmoore_process_json.py    | Counts famous people by zodiac sign from the JSON file.          |
| michaeljmoore_process_text.py    | Counts occurrences of a specific word in the text file.          |

---

## How to Run All Scripts

To automate the workflow, run:

```shell
python run_all_datafun_scripts.py
```

This will fetch all data files and then process them in sequence.

---

## Individual Script Usage

Activate your virtual environment and run any script directly, for example:

```shell
python michaeljmoore_get_csv.py
python michaeljmoore_process_csv.py
```

---

## Requirements

- Python 3.x
- VS Code
- Git
- All dependencies listed in `requirements.txt`

---

## Professional Workflow

- Use a virtual environment (`.venv`)
- Use clear, descriptive commit messages
- Test each script before committing

---

## Example Git Commands

```shell
git add .
git commit -m "Describe your changes"
git push -u origin main
```

---

## Credits

Custom implementation by Michael J Moore, based on [datafun-03-analytics](https://github.com/denisecase/datafun-03-analytics).

---

*For more details, see the comments and docstrings in each script.*
