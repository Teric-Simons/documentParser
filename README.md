# Document Processing Project

This project processes `.docx` files into their Json equivalent

## Prerequisites

- **Python 3.6+**
- **LibreOffice** (for converting `.docx` to `.pdf`)

## Installation
1. **Install system dependencies**
sudo apt install -y python3-pip python3-dev libmupdf-dev

2. **Install the required Python packages:**

    ```sh
    pip install -r requirements.txt
    ```

## Running the Script

1. **Place your `.docx` files in the `samples` folder.**

2. **Run the `main.py` script:**

    ```sh
    python main.py
    ```

## Note

1.Files with tables:
    The final JSON file will be named filename-final.json.
    
2.Files without tables:
    The JSON file will be named filename-filedata.json.



