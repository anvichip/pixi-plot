from flask import Flask, render_template, request, send_file
import tempfile

import os

app = Flask(__name__)

# Function to process the uploaded PDF file
def main(pdf_path):
    # Implement your processing logic here
    # This is just a placeholder
    return "Processed PPT file path"

# Route for the home page
@app.route('/')
def home():
    return render_template('update.html')

# Endpoint for uploading the PDF file
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'pdf_file' not in request.files:
        return "No file part"
    pdf_file = request.files['pdf_file']
    if pdf_file.filename == '':
        return "No selected file"
    if pdf_file:
        # Save the PDF file to a temporary directory
        _, temp_pdf_path = tempfile.mkstemp(suffix=".pdf")
        pdf_file.save(temp_pdf_path)
        
        # Call the main function to process the PDF
        ppt_path = main(temp_pdf_path)
        
        # Delete the temporary PDF file
        os.remove(temp_pdf_path)
        
        # Return the PPT file for download
        return send_file(ppt_path, as_attachment=True)
    return "Error processing file"

if __name__ == "__main__":
    app.run()
