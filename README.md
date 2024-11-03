# Text Analysis Script

## Description
This script analyzes a text file, extracting various statistical parameters such as the total number of letters, words, sentences, the most common words, and letter frequency. The analysis results are saved in CSV format for further use.

## Project Tasks
1. Handling command-line arguments.
2. Implementing text analysis methods in `methods.py`.
3. Integrating `methods.py` with exception handling.
4. Adding a custom "skull" loading animation before displaying results.

## Requirements
- Python 3.8+
- Dependencies:
  - `methods.py`: A file containing text analysis functions.
  - `skull.py`: A file containing the `skull_loading()` function for a loading animation before displaying results.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/your_repository.git
    cd your_project
    ```
2. Make sure `methods.py` and `skull.py` are located in the same directory as the main script.

## Usage
The script takes the path to a text file as a command-line argument. For example:
```bash
python analyze.py path_to_file.txt
