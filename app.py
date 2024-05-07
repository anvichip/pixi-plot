# # # from flask import Flask, render_template, request, send_file
# # # import tempfile

# # # import os

# # # app = Flask(__name__)

# # # # Function to process the uploaded PDF file
# # # def main(pdf_path):
# # #     # Implement your processing logic here
# # #     # This is just a placeholder
# # #     return "Processed PPT file path"

# # # # Route for the home page
# # # @app.route('/')
# # # def home():
# # #     return render_template('update.html')

# # # # Endpoint for uploading the PDF file
# # # @app.route('/upload', methods=['POST'])
# # # def upload_file():
# # #     if 'pdf_file' not in request.files:
# # #         return "No file part"
# # #     pdf_file = request.files['pdf_file']
# # #     if pdf_file.filename == '':
# # #         return "No selected file"
# # #     if pdf_file:
# # #         # Save the PDF file to a temporary directory
# # #         _, temp_pdf_path = tempfile.mkstemp(suffix=".pdf")
# # #         pdf_file.save(temp_pdf_path)
        
# # #         # Call the main function to process the PDF
# # #         ppt_path = main(temp_pdf_path)
        
# # #         # Delete the temporary PDF file
# # #         os.remove(temp_pdf_path)
        
# # #         # Return the PPT file for download
# # #         return send_file(ppt_path, as_attachment=True)
# # #     return "Error processing file"

# # # if __name__ == "__main__":
# # #     app.run()


# # from flask import Flask, render_template, request, send_file
# # import tempfile
# # import os
# # import requests
# # from test_modal import call_llm_api
# # from sdxl import clean_input, generate_images_from_text_prompts
# # from ppt import ppt_main
# # app = Flask(__name__)

# # # Function to process the uploaded PDF file
# # def main(pdf_path):
# #     # Call LLM API to process the PDF and get the output text
# #     llm_output,ppt_text = call_llm_api(pdf_path)
    
# #     # Call SDXL API with the output of LLM as input
# #     sdxl_output = call_sdxl_api(llm_output)
    
# #     # Process the SDXL output and generate image (You need to implement this function)
# #     # For demonstration, let's assume the SDXL API returns a URL of the generated image
# #     process_sdxl_output(ppt_text)


# # # Function to call the LLM API
# # def llm_api(pdf_path):
# #     # Implement the logic to call your LLM API
# #     # For example:
# #     # response = requests.post(llm_api_url, files={'pdf_file': open(pdf_path, 'rb')})
# #     # llm_output = response.json()
# #     # return llm_output
# #     llm_output,ppt_text=call_llm_api(r'D:\deeplearning project\pixi-plot\tom_sawyer-4.pdf')
# #     return llm_output,ppt_text

# # # Function to call the SDXL API
# # def call_sdxl_api(llm_output):
# #     # Implement the logic to call your SDXL API
# #     # For example:
# #     # response = requests.post(sdxl_api_url, json={'llm_output': llm_output})
# #     # sdxl_output = response.json()
# #     # return sdxl_output
# #     clean_input(llm_output)
# #     # return sdxl_output

# # # Function to process the SDXL output and generate image
# # def process_sdxl_output(sdxl_output):
# #     # Implement the logic to process the SDXL output
# #     # For demonstration, let's assume the SDXL output contains URL of the generated image
# #     # You may need to download the image or use it directly based on your requirement
# #     # For now, we'll just return the URL
# #     ppt_main()
# #     return sdxl_output

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
# #         image_url = main(temp_pdf_path)
        
# #         # Delete the temporary PDF file
# #         os.remove(temp_pdf_path)
        
# #         # Return the URL of the generated image
# #         return image_url
# #     return "Error processing file"

# # if __name__ == "__main__":
# #     app.run()


# # from flask import Flask, render_template, request, send_file
# # import tempfile
# # import os
# # # from test_modal import call_llm_api
# # # from sdxl import clean_input, generate_images_from_text_prompts
# # # from ppt import ppt_main
# # # from scripts_flask_final import main_flask

# # app = Flask(__name__)


# # # Route for the home page
# # @app.route('/')
# # def home():
# #     return render_template('update.html')

# # # Endpoint for uploading the PDF file
# # @app.route('/upload', methods=['POST'])
# # def upload_file():
# #     return render_template('index.html')
# #     # if 'pdf_file' not in request.files:
# #     #     return "No file part"
# #     # pdf_file = request.files['pdf_file']
# #     # if pdf_file.filename == '':
# #     #     return "No selected file"
# #     # if pdf_file:
# #     #     # Save the PDF file to a temporary directory
# #     #     _, temp_pdf_path = tempfile.mkstemp(suffix=".pdf")
# #     #     pdf_file.save(temp_pdf_path)
        
# #     #     # Call the main function to process the PDF
# #     #     main_flask(temp_pdf_path)
        
# #     #     # Delete the temporary PDF file
# #     #     os.remove(temp_pdf_path)
        
# #     #     # Return a message indicating successful processing
# #     #     return "PDF file processed successfully"
# #     # return "Error processing file"

# # if __name__ == "__main__":
# #     app.run()


# from flask import Flask, render_template, request, send_file
# import tempfile
# import os
# from scripts_flask_final import main_flask

# app = Flask(__name__)

# # # Function to process the uploaded PDF file
# # def main_flask(pdf_path):
# #     # Add your logic here to process the PDF file using main_flask
# #     pass

# # Route for the home page
# @app.route('/')
# def home():
#     return render_template('update.html')

# # Endpoint for uploading the PDF file
# # @app.route('/upload', methods=['POST'])
# # def upload_file():
# #     if request.method == 'POST':
# #         if 'pdf_file' not in request.files:
# #             return "No file part"
        
# #     # pdf_file = request.files['pdf_file']
# #         # print(pdf_file)
        
# #         # if pdf_file.filename == '':
# #         #     return "No selected file"
        
# #         # Save the PDF file to a temporary directory
# #     #     _, temp_pdf_path = tempfile.mkstemp(suffix=".pdf")
# #     #     pdf_file.save(temp_pdf_path)
# #     #     pdf_path = 'pixi-plot\tom_sawyer-4.pdf'
# #     # # Uncomment the following line after confirming that the file upload works correctly
# #     # # main_flask(pdf_path)
    
# #     #     # Delete the temporary PDF file
# #     #     os.remove(temp_pdf_path)
# #         # Redirect or render a template indicating successful processing
# #     return render_template('index.html')  # You can redirect to another page or render a success template

# # from flask import Flask, render_template, request
# # import os

# # app = Flask(_name_)

# # @app.route('/')
# # def home():
# #     return render_template('update.html')

# @app.route('/upload', methods=['POST'])
# def upload_file():
#     if 'pdf_file' not in request.files:
#         return "No file part", 400  # Bad Request
        
#     pdf_file = request.files['pdf_file']
        
#     if pdf_file.filename == '':
#         return "No selected file", 400  # Bad Request
        
#     # Save the PDF file to a temporary directory
#     pdf_file.save(os.path.join("uploads", pdf_file.filename))
    
#     # Redirect or render a template indicating successful processing
#     return render_template('index.html')

# if __name__ == "__main__":
#     if not os.path.exists('uploads'):
#         os.makedirs('uploads')
#     app.run(debug=True)
# # if __name__ == "__main__":
#     # app.run()





# from flask import Flask, render_template, request, redirect, url_for, send_from_directory
# import os
# from scripts_flask_final import main_flask
# import tempfile

# app = Flask(__name__)

# @app.route('/')
# def render_upload_form():
#     return render_template('update.html')

# @app.route('/upload', methods=['POST'])
# def upload_pdf():
#     if 'pdf_file' not in request.files:
#         return redirect(request.url)

#     pdf_file = request.files['pdf_file']

#     if pdf_file.filename == '':
#         return redirect(request.url)

#     if pdf_file:
#         # Create a temporary file and save the uploaded file there
#         _, temp_path = tempfile.mkstemp()
#         pdf_file.save(temp_path)
        
#         # Call the main_flask function with the path of the saved file
#         main_flask(temp_path)
        
#         # Remove the temporary file
#         # os.remove(temp_path)
        
#         return redirect(url_for('success'))

# @app.route('/success')
# def success():
#     return render_template('success.html')

# @app.route('/download')
# def download_file():
#     return send_from_directory(r"D:\deeplearning project\pixi-plot", 'output.pptx', as_attachment=True)

# if __name__ == '__main__':
#     app.run(debug=True)



# import streamlit as st
# from scripts_flask_final import main_flask
# import tempfile
# import os

# def save_uploaded_file(uploaded_file):
#     try:
#         with tempfile.NamedTemporaryFile(delete=False) as fp:
#             fp.write(uploaded_file.getvalue())
#             return fp.name
#     except Exception as e:
#         st.error(f"Error: {e}")
#         return None

# st.title('Welcome to Pixi-Plot!')

# uploaded_file = st.file_uploader("Your story book please...", type="pdf")

# if uploaded_file is not None:
#     temp_path = save_uploaded_file(uploaded_file)
#     if temp_path is not None:
#         # Call the main_flask function with the path of the saved file
#         main_flask(temp_path)
#         # Remove the temporary file
#         os.remove(temp_path)
#         st.success('File processed successfully.')
#     else:
#         st.error('File processing failed.')

# if st.button('Get your comic here :)'):
#     st.download_button(
#         label="Download output.pptx",
#         data=open(r"output.pptx", 'rb'),
#         file_name='output.pptx',
#         mime='application/vnd.openxmlformats-officedocument.presentationml.presentation'
#     )



import streamlit as st
from scripts_flask_final import main_flask
import tempfile
import os
import streamlit_ace

def save_uploaded_file(uploaded_file):
    try:
        with tempfile.NamedTemporaryFile(delete=False) as fp:
            fp.write(uploaded_file.getvalue())
            return fp.name
    except Exception as e:
        st.error(f"Error: {e}")
        return None

st.title('Welcome to Pixi-Plot!')

uploaded_file = st.file_uploader("Your story book please...", type="pdf")

if 'processed' not in st.session_state:
    st.session_state.processed = False

if uploaded_file is not None and not st.session_state.processed:
    temp_path = save_uploaded_file(uploaded_file)
    if temp_path is not None:
        # Call the main_flask function with the path of the saved file
        main_flask(temp_path)
        # Remove the temporary file
        os.remove(temp_path)
        st.session_state.processed = True
        st.success('File processed successfully.')
    else:
        st.error('File processing failed.')

if st.button('Get your comic here :'):
    st.download_button(
        label="Download output.pptx",
        data=open(r"output.pptx", 'rb'),
        file_name='output.pptx',
        mime='application/vnd.openxmlformats-officedocument.presentationml.presentation'
    )

