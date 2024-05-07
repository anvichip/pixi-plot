from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
from scripts_flask_final import main_flask
import tempfile
from vercel import vercel


app = Flask(__name__)

@app.route('/')
def render_upload_form():
    return render_template('update.html')

@app.route('/upload', methods=['POST'])
def upload_pdf():
    if 'pdf_file' not in request.files:
        return redirect(request.url)

    pdf_file = request.files['pdf_file']

    if pdf_file.filename == '':
        return redirect(request.url)

    if pdf_file:
        # Create a temporary file and save the uploaded file there
        _, temp_path = tempfile.mkstemp()
        pdf_file.save(temp_path)
        
        # Call the main_flask function with the path of the saved file
        main_flask(temp_path)
        
        # Remove the temporary file
        # os.remove(temp_path)
        
        return redirect(url_for('success'))

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/download')
def download_file():
    return send_from_directory(r"D:\deeplearning project\pixi-plot", 'output.pptx', as_attachment=True)

if __name__ == '__main__':
    # app.run(debug=True)
    vercel(app)

