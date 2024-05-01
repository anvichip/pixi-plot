from test_modal import call_llm_api
from sdxl import clean_input, generate_images_from_text_prompts
from ppt import ppt_main
# Function to process the uploaded PDF file
def main_flask(pdf_path):
    # Call LLM API to process the PDF and get the output text
    llm_output, ppt_text = call_llm_api(pdf_path)
    
    # Call SDXL API with the output of LLM as input
    clean_input(llm_output)
    
    # Process the SDXL output and generate image
    ppt_main(ppt_text)
    print(ppt_text)


pdf_path = r'C:\Users\arush\OneDrive\Desktop\deeplearning project\pixi-plot\tom_sawyer-4_merged.pdf'
main_flask(pdf_path)