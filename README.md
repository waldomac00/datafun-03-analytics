# waldomac00-datafun-03-analytics
# datafun-03-analytics

This project demonstrates how to fetch and process various types of 
data (Excel, JSON, text, and CSV) using Python. 

The repository includes:

- Four example fetchers: Scripts to retrieve data from the web.
- Four example processors: Scripts to analyze and process the fetched data.

Start by running the examples to understand their functionality, and then build your own scripts to fetch and process data of your choice (using each of these example types).

## Project Requirements

- VS Code
- Git
- Python 

## Professional Python Workflow

See [pro-analytics-01](https://github.com/denisecase/pro-analytics-01/)

## Commands to Manage Virtual Environment

For Windows PowerShell (change if using Mac/Linux)

```powershell
py -m venv .venv
.\.venv\Scripts\activate
py -m pip install --upgrade pip setuptools wheel
py -m pip install --upgrade -r requirements.txt
```
## Commands to Run Python Scripts

Remember to activate your .venv (and install packages if they haven't been installed yet) before running files.
Verify that all required packages are included in requirements.txt (and have NOT been commented out).


```shell
py example_get_csv.py
py example_get_excel.py
py example_get_json.py
py example_get_text.py

py example_process_csv.py
py example_process_excel.py
py example_process_json.py
py example_process_text.py

py michaeljmoore_get_csv.py
py michaeljmoore_get_excel.py
py michaeljmoore_get_json.py
py michaeljmoore_get_text.py

py michaeljmoore_process_csv.py
py michaeljmoore_process_excel.py
py michaeljmoore_process_json.py
py michaeljmoore_process_text.py

```

## Commands to Git add-commit-push

```shell
git add .
git commit -m "custom message"
git push -u origin main
```

## Create and Run Your Data Fetchers
1. Find data files on the web for each type (CSV, Excel, JSON, and text).  
2. Create your own Python script to fetch each type of data and save it in a folder named **data**.
3. Name your scripts:
   1. michaeljmoore_get_csv.py
   2. michaeljmoore_get_excel.py
   3. michaeljmoore_get_json.py
   4. michaeljmoore_get_text.py
4. Implement your data-processing logic in small steps:
   - Fetch data for one file type.
   - Test, verify, and Git add-commit-push.
  
## Create and Run Your Data Processors
1. Determine a simple metric from each of your data files.  
2. Create your own Python script to read the data, process it, and save it in a folder named **data_processed**.
3. Name your scripts:
   1. michaeljmoore_process_csv.py
   2. michaeljmoore_process_excel.py
   3. michaeljmoore_process_json.py
   4. michaeljmoore_process_text.py
4. Work incrementally, using git add-commit-push after each bit of progress. 

## Update README.md to Describe Your Work
1. In your README.md, list each of your fetchers with a short description.
2. In your README.md, list each of your processors with a short description of what it does. 
3. Include the execution commands to run your fetchers and processors. 

## Helpful Documentation
If you're unsure about any of the setup steps or tools, consult these resources:
- [requests library documentation](https://docs.python-requests.org)

### Tips
- Use descriptive filenames for the data you fetch - and proper file extensions.
- Work incrementally—verify each small step works before moving to the next.
- The examples are required reading - use them to learn and understand first. 
- Test each script carefully before proceeding.
- Use meaningful commit messages when pushing to GitHub to document your progress.

## Review Commit History
Once your project is complete, review your commit history in GitHub under the **Commits** tab. 
Ensure your commit messages are clear and professional.

## Reference Projects

Custom implementation of the example project at 
[datafun-03-analytics](https://github.com/denisecase/datafun-03-analytics)

- [Module 2 Repo](https://github.com/denisecase/datafun-02-project-setup)
- [Module 1 Repo](https://github.com/denisecase/datafun-01-utils/)

# datafun-02-project-setup
Utilities for scripting project folders

## Project Requirements

- VS Code
- Git
- Python 

## Professional Python Workflow

See [pro-analytics-01](https://github.com/denisecase/pro-analytics-01/)

## Commands to Manage Virtual Environment

For Windows PowerShell (change if using Mac/Linux).
Verify that all required packages are included in requirements.txt (and have NOT been commented out).


```powershell
py -m venv .venv
.\.venv\Scripts\activate
py -m pip install --upgrade pip setuptools wheel
py -m pip install --upgrade -r requirements.txt
```

## Commands to Run Python Scripts

Remember to activate your .venv (and install packages if they haven't been installed yet) before running files.

```shell
py utils_michaeljmoore.py
py dirbot_michaeljmoore.py
```

## Commands to Git add-commit-push

```shell
git add .
git commit -m "custom message"
git push -u origin main
```

## Reference Projects

Custom implementation of the example project at 
[datafun-02-project-setup](https://github.com/denisecase/datafun-02-project-setup)

- [Module 1 Repo](https://github.com/denisecase/datafun-01-utils/)

# datafun-01-utils

Reusable module for my Data Analytics Python projects

## Project Requirements

- VS Code
- Git
- Python 

## Use Standard Professional Workflow

See [pro-analytics-01](https://github.com/denisecase/pro-analytics-01/)

## Commands to Manage Virtual Environment

These commands will:
1. Create virtual environment in .venv folder
2. Activate .venv
3. Upgrade core tools
4. Install external project packages
5. Verify installed packages

**Mac/Linux**

```shell
python3 --version
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip setuptools wheel
python3 -m pip install --upgrade -r requirements.txt
pip list
```

**Windows PowerShell**

```shell
py --version
py -m venv .venv
.\.venv\Scripts\activate
py -m pip install --upgrade pip setuptools wheel
py -m pip install --upgrade -r requirements.txt
py -m pip list
```

## Commands to Run Python Script

**Mac/Linux**

```shell
python3 utils_michaeljmooree.py
```

**Windows PowerShell**

```shell
py utils_michaeljmoore.py
```

> To stop a running Python program, press `Ctrl + C` in the terminal 
> (works the same on Windows, Mac, and Linux).

## Commands to Git add-commit-push

Write a custom message (-m) in quotes describing what was done, e.g. "completed first TODO", "final commit", etc. 

These commands work the same in all terminals and will:
1. Add all new and modified files in the current project folder into Git staging area. The `.` means _everything in this folder_.
2. Commit (record) a snapshot of staged changes with a descriptive message that will appear in the repo history.
3. Push (upload) commits from local machine to the remote (GitHub) repo (alias `origin`) on the main branch. The -u tells Git to remember this this branch mapping on upstream commands, so future git push commands can be shorter (just `git push`).


```shell
git add .
git commit -m "custom message here"
git push -u origin main
```

## Reference Project

This project is a custom implementation of the example project at 
[datafun-01-utils](https://github.com/denisecase/datafun-01-utils).

## Writing Good README.md Files

Every GitHub project has a README.md file with an overview.
The file type is `Markdown` and it's a very simple Markup language for text. 

- A Markdown `title` starts with: hash space
- A Markdown `second-level heading` starts with: hash hash space
- A Markdown `un-ordered list` starts with: dash space
- A Markdown `ordered list` start with: 1. space
- Markdown `code fencing` uses three **back tics** on their own line to display code and commands.
- Markdown **bold text** is surrounded by: two asterisks
- Markdown *underline text* is surrounded by: one asterisk


Markdown skills are critical for project README files, Jupyter Notebooks (code, charts, and narrative together), and writing technical papers with Sphinx.

## Example Screenshots

> Know how to display an image in Markdown - you'll want this to highlight your charts and more. 

![VS Code While Working](images/vs_code_while_working.png)


## Skills Demonstrated

- GitHub repo with README.md
- Git clone to machine.
- Create Python module.
- Create Python local virtual environment in .venv folder.
- Manage external packages (e.g. for logging and read-out-loud)
- Working with variables and functions. 
- Creating a standard Python module (ready for import or running as a script).
- Git clone, add, commit, push, pull
- Using a professional IDE (VS Code)
