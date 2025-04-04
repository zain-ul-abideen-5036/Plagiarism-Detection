# Plagiarism Detection Tool Using Tkinter

## Overview
This repository contains a Python-based plagiarism detection tool that uses `Tkinter` for creating a graphical user interface (GUI). It reads two text files, compares them, and calculates the plagiarism percentage based on common words between the files. The tool visually displays the result in a window, with a background color indicating the severity of the plagiarism.

---

## Features
- Reads the contents of two text files and compares them.
- Detects common words between the files.
- Calculates plagiarism percentage.
- Displays the plagiarism result with a visual representation using Tkinter.
- Background color changes based on the level of plagiarism:
  - **Yellow**: 30% - 60% plagiarism.
  - **Red**: More than 60% or less than 30% plagiarism.

---

## Installation Instructions
Follow these steps to run the project locally.

### Prerequisites
- Python 3.x
- Tkinter (comes with Python installation)

### Steps to Run:
1. Clone the repository:
   ```bash
   git clone https://github.com/zain-ul-abideen-5036/Plagiarism-Detection.git
   ```
2. Navigate to the project folder:
   ```bash
   cd Plagiarism-Detection
   ```
3. Ensure you have the text files (`File_1.txt` and `File_2.txt`) in the same directory as the Python script.
4. Run the Python script:
   ```bash
   python DetectPlagiarism.py
   ```

---

## Files:
- **`DetectPlagiarism.py`**: The Python script for detecting plagiarism and displaying the result.
- **`File_1.txt` and `File_2.txt`**: Sample text files to test the plagiarism detection tool.

---

## Example
### 1. File_1.txt
   ```text
  The quick brown fox jumps over the lazy dog. The fox is fast and clever.
   ```
### 1. File_2.txt
   ```text
 A quick brown fox jumps over the lazy dog. The fox is very fast and clever.
   ```
### Output:
The plagiarism percentage will be displayed in a window with a background color indicating the degree of plagiarism.

---

## Contributing
Feel free to open issues or submit pull requests if you want to contribute to this project. I welcome any contributions and suggestions to improve this plagiarism detection tool.

---

## Contact
For questions or feedback, contact: abideen5036@gmail.com

---


