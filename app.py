# # from flask import Flask, render_template, request, send_file
# # import tempfile

# # import os

# # app = Flask(__name__)

# # # Function to process the uploaded PDF file
# # def main(pdf_path):
# #     # Implement your processing logic here
# #     # This is just a placeholder
# #     return "Processed PPT file path"

# # # Route for the home page
# # @app.route('/')
# # def home():
# #     return render_template('update.html')

# # # Endpoint for uploading the PDF file
# # @app.route('/upload', methods=['POST'])
# # def upload_file():
# #     if 'pdf_file' not in request.files:
# #         return "No file part"
# #     pdf_file = request.files['pdf_file']
# #     if pdf_file.filename == '':
# #         return "No selected file"
# #     if pdf_file:
# #         # Save the PDF file to a temporary directory
# #         _, temp_pdf_path = tempfile.mkstemp(suffix=".pdf")
# #         pdf_file.save(temp_pdf_path)
        
# #         # Call the main function to process the PDF
# #         ppt_path = main(temp_pdf_path)
        
# #         # Delete the temporary PDF file
# #         os.remove(temp_pdf_path)
        
# #         # Return the PPT file for download
# #         return send_file(ppt_path, as_attachment=True)
# #     return "Error processing file"

# # if __name__ == "__main__":
# #     app.run()


# from flask import Flask, render_template, request, send_file
# import tempfile
# import os
# import requests
# from test_modal import call_llm_api
# from sdxl import clean_input, generate_images_from_text_prompts
# from ppt import ppt_main
# app = Flask(__name__)

# # Function to process the uploaded PDF file
# def main(pdf_path):
#     # Call LLM API to process the PDF and get the output text
#     llm_output,ppt_text = call_llm_api(pdf_path)
    
#     # Call SDXL API with the output of LLM as input
#     sdxl_output = call_sdxl_api(llm_output)
    
#     # Process the SDXL output and generate image (You need to implement this function)
#     # For demonstration, let's assume the SDXL API returns a URL of the generated image
#     process_sdxl_output(ppt_text)


# # Function to call the LLM API
# def llm_api(pdf_path):
#     # Implement the logic to call your LLM API
#     # For example:
#     # response = requests.post(llm_api_url, files={'pdf_file': open(pdf_path, 'rb')})
#     # llm_output = response.json()
#     # return llm_output
#     llm_output,ppt_text=call_llm_api(r'D:\deeplearning project\pixi-plot\tom_sawyer-4.pdf')
#     return llm_output,ppt_text

# # Function to call the SDXL API
# def call_sdxl_api(llm_output):
#     # Implement the logic to call your SDXL API
#     # For example:
#     # response = requests.post(sdxl_api_url, json={'llm_output': llm_output})
#     # sdxl_output = response.json()
#     # return sdxl_output
#     clean_input(llm_output)
#     # return sdxl_output

# # Function to process the SDXL output and generate image
# def process_sdxl_output(sdxl_output):
#     # Implement the logic to process the SDXL output
#     # For demonstration, let's assume the SDXL output contains URL of the generated image
#     # You may need to download the image or use it directly based on your requirement
#     # For now, we'll just return the URL
#     ppt_main()
#     return sdxl_output

# # Route for the home page
# @app.route('/')
# def home():
#     return render_template('update.html')

# # Endpoint for uploading the PDF file
# @app.route('/upload', methods=['POST'])
# def upload_file():
#     if 'pdf_file' not in request.files:
#         return "No file part"
#     pdf_file = request.files['pdf_file']
#     if pdf_file.filename == '':
#         return "No selected file"
#     if pdf_file:
#         # Save the PDF file to a temporary directory
#         _, temp_pdf_path = tempfile.mkstemp(suffix=".pdf")
#         pdf_file.save(temp_pdf_path)
        
#         # Call the main function to process the PDF
#         image_url = main(temp_pdf_path)
        
#         # Delete the temporary PDF file
#         os.remove(temp_pdf_path)
        
#         # Return the URL of the generated image
#         return image_url
#     return "Error processing file"

# if __name__ == "__main__":
#     app.run()


# from flask import Flask, render_template, request, send_file
# import tempfile
# import os
# # from test_modal import call_llm_api
# # from sdxl import clean_input, generate_images_from_text_prompts
# # from ppt import ppt_main
# # from scripts_flask_final import main_flask

# app = Flask(__name__)


# # Route for the home page
# @app.route('/')
# def home():
#     return render_template('update.html')

# # Endpoint for uploading the PDF file
# @app.route('/upload', methods=['POST'])
# def upload_file():
#     return render_template('index.html')
#     # if 'pdf_file' not in request.files:
#     #     return "No file part"
#     # pdf_file = request.files['pdf_file']
#     # if pdf_file.filename == '':
#     #     return "No selected file"
#     # if pdf_file:
#     #     # Save the PDF file to a temporary directory
#     #     _, temp_pdf_path = tempfile.mkstemp(suffix=".pdf")
#     #     pdf_file.save(temp_pdf_path)
        
#     #     # Call the main function to process the PDF
#     #     main_flask(temp_pdf_path)
        
#     #     # Delete the temporary PDF file
#     #     os.remove(temp_pdf_path)
        
#     #     # Return a message indicating successful processing
#     #     return "PDF file processed successfully"
#     # return "Error processing file"

# if __name__ == "__main__":
#     app.run()


from flask import Flask, render_template, request, send_file
import tempfile
import os
from scripts_flask_final import main_flask

app = Flask(__name__)

# # Function to process the uploaded PDF file
# def main_flask(pdf_path):
#     # Add your logic here to process the PDF file using main_flask
#     pass

# Route for the home page
@app.route('/')
def home():
    return render_template('update.html')

# Endpoint for uploading the PDF file
# @app.route('/upload', methods=['POST'])
# def upload_file():
#     if request.method == 'POST':
#         if 'pdf_file' not in request.files:
#             return "No file part"
        
#     # pdf_file = request.files['pdf_file']
#         # print(pdf_file)
        
#         # if pdf_file.filename == '':
#         #     return "No selected file"
        
#         # Save the PDF file to a temporary directory
#     #     _, temp_pdf_path = tempfile.mkstemp(suffix=".pdf")
#     #     pdf_file.save(temp_pdf_path)
#     #     pdf_path = 'pixi-plot\tom_sawyer-4.pdf'
#     # # Uncomment the following line after confirming that the file upload works correctly
#     # # main_flask(pdf_path)
    
#     #     # Delete the temporary PDF file
#     #     os.remove(temp_pdf_path)
#         # Redirect or render a template indicating successful processing
#     return render_template('index.html')  # You can redirect to another page or render a success template

# from flask import Flask, render_template, request
# import os

# app = Flask(_name_)

# @app.route('/')
# def home():
#     return render_template('update.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'pdf_file' not in request.files:
        return "No file part", 400  # Bad Request
        
    pdf_file = request.files['pdf_file']
        
    if pdf_file.filename == '':
        return "No selected file", 400  # Bad Request
        
    # Save the PDF file to a temporary directory
    pdf_file.save(os.path.join("uploads", pdf_file.filename))
    
    # Redirect or render a template indicating successful processing
    return render_template('index.html')

if __name__ == "__main__":
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(debug=True)
# if __name__ == "__main__":
    # app.run()


