from test_modal import call_llm_api
from sdxl import clean_input, generate_images_from_text_prompts
from ppt import ppt_main

# Function to process the uploaded PDF file
def main_flask():
    pdf_path = input("Enter PDF Path ")
    # Call LLM API to process the PDF and get the output text
    # llm_output, ppt_text = call_llm_api(pdf_path)
    ppt_text, prompts = call_llm_api(pdf_path)
    print("LLM Output: ", ppt_text)
    print("Prompts: ", prompts)
    
    # Call SDXL API with the output of LLM as input
    clean_input(prompts)
    
    # Process the SDXL output and generate image
    ppt_main(ppt_text)


main_flask()
