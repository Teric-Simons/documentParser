import subprocess
import os

def convert_docx_to_pdf(docx_path, pdf_path):
    # Ensure the paths are absolute
    pdf_path = os.path.abspath(pdf_path)
    docx_path = os.path.abspath(docx_path)

    try:
        # First attempt with 'libreoffice' command
        command = [
            'libreoffice', '--headless', '--convert-to', 'pdf', '--outdir', 
            os.path.dirname(pdf_path), docx_path
        ]

        subprocess.run(command, check=True)
        print("LibreOffice converted the DOCX to PDF successfully.")
        return True

    except Exception as error:
        print(f"Error occurred with libreoffice command: {error}")

        try:
            # Second attempt with full path to soffice.exe
            soffice_path = r"C:\Program Files\LibreOffice\program\soffice.exe"
            command = [
                soffice_path, '--headless', '--convert-to', 'pdf', '--outdir', 
                os.path.dirname(pdf_path), docx_path
            ]

            subprocess.run(command, check=True)
            print("LibreOffice (full path) converted the DOCX to PDF successfully.")
            return True

        except subprocess.CalledProcessError as error:
            print(f"Error occurred with full path to LibreOffice: {error}")
            return False
