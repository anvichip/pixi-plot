## Importing Libraries
from langchain import LLMChain
import os
#from scripts import save_summaries, read_pages
from langchain.document_loaders import PyPDFLoader
#from llama_models import intialize_pipeline
#from prompts import get_prompt
from langchain import HuggingFacePipeline
#from sdxl import initiate_sdxl, gen_image

### prompt.py
from langchain import PromptTemplate


import os
import logging


## function to read 
def read_pages(path_folder):
    text = ""
    directory = path_folder
    for filename in os.listdir(directory):
        if(filename.endswith('.txt')):
            filepath = os.path.join(directory, filename)

            with open(filepath,'r') as f:
                text += f.read() 
    
    return text


## Function to read JSON

   


## Function to generate a summary using the llama prompt
def generate_summary(llm_chain,text):
 
    output = llm_chain.run(text)
    extract = output.split('[/INST]')
    return extract[1]

## Function to save the generated summaries in a folder and take out summaries of all files in a folder
def save_summaries(document):
    # Directory to save the summaries
    summaries_directory = "summaries"

    # Create the "summaries" directory if it doesn't exist
    os.makedirs(summaries_directory, exist_ok=True)

    if(type(document) == 'list'):
        # Iterate over each chapter
        for i, chapter_content in enumerate(document, start=1):
            # Generate summary for the chapter
            summary = generate_summary(chapter_content)

            # Write the summary to a text file
            summary_file_path = os.path.join(summaries_directory, f'summary_page_{i}.txt')
            with open(summary_file_path, 'w') as f:
                f.write(summary)
        
        logging.info('Files saved in Summary')
    
    elif(type(document) == 'str'):
        text = generate_summary(document)
        return text


## Function to convert summaries into panels
def generate_panels(llm_chain,text):
 
    output = llm_chain.run(text)
    extract = output.split('[/INST]')
    return extract[1]










def get_prompt(num):
    if(num == 0):
        
        ##Summarizer
        template_summary = """
        <s>[INST] <<SYS>>
        You are an expert act as a book chapter summarizer, and summarize the text given.
        <</SYS>>

        {text} [/INST]
        """

        prompt = PromptTemplate(
            input_variables=["text"],
            template=template_summary,
        )
    
    elif(num == 3):
        ## Characters descriptions
        template_char = """
        <s>[INST] <<SYS>>
        I am giving you the summary of a story, extract the unique characters from it and add their names along with a short description of the character conveying their unique characteristics, age, gender in JSON format. 
        <</SYS>>

        {text} [/INST]
        """

        prompt = PromptTemplate(
            input_variables=["text"],
            template=template_char,
        )

    elif(num == 2):
        
        ##panels formation
        template_panel = """
        <s>[INST] <<SYS>>
        This is the summary of a book chapter. I want to visualize the story using panels. Divide the summary into scenes which can be represented using panels, return all the panels in JSON format.

        {text} [/INST]
        """

        prompt  = PromptTemplate(
            input_variables=["text"],
            template=template_panel,
        )
    
    elif(num == 1):
        ## panel->prompt

        template_prompts = """
        <s>[INST] <<SYS>>
        Act as the assistant to a painter. I am giving you some image descriptions, Change them to very simple prompts not decriptive for a painter to draw.

        {text} [/INST]
        """

        prompt = PromptTemplate(
            input_variables=["text"],
            template=template_prompts,
        )
    
    return prompt


from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from transformers import pipeline
from langchain import HuggingFacePipeline
from langchain import PromptTemplate,  LLMChain
from token_api import hf_token

def intialize_pipeline():
    tokenizer = AutoTokenizer.from_pretrained("./meta-llama/Llama-2-7b-chat-hf"
                                            #token = hf_token, 
                                            #cache_dir = './models'
                                            )

    model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b-chat-hf"
                                            #device_map='auto',
                                            #torch_dtype=torch.float16,
                                            #use_auth_token=True,
                                            #cache_dir = './models',
                                            #token = hf_token
                                            )

    pipe = pipeline("text-generation",
                    model=model,
                    tokenizer= tokenizer,
                    torch_dtype=torch.bfloat16,
                    device_map="auto",
                    max_new_tokens = 4096,
                    do_sample=True,
                    top_k=30,
                    num_return_sequences=1,
                    eos_token_id=tokenizer.eos_token_id
                    )
    return pipe

def initialize_llm_chain(prompt,llm):
    llm_chain = LLMChain(prompt=prompt, llm=llm)
    return llm_chain



def load_pdf(path):
    loader = PyPDFLoader(path) ## Load the pdf file from the path
    document = loader.load()
    return document


def main(path):

    ##??? loader
    document = load_pdf(path)
    print(type(document))

    ##intialize llama2 pipe
    pipe_llama = intialize_pipeline() 
    llm = HuggingFacePipeline(pipeline = pipe_llama, model_kwargs = {'temperature':0}) ##initalize llm 


    
    ##summmary of each page
    prompt_summary = get_prompt(0)
    print(prompt_summary)
    llm_chain_summary = LLMChain(prompt=prompt_summary, llm=llm)
    save_summaries(document)

    
    ##summmary of all pages
    #prompt_summary = get_prompt(0)
    # llm_chain_summary = LLMChain(prompt=prompt_summary, llm=llm)
    # all_pages_text = read_pages('./summaries')
    # all_pages_summary = save_summaries(all_pages_text)


    ##summary -> panels
    prompt_panel = get_prompt(1)
    print(prompt_panel)
    llm_chain_panel = LLMChain(prompt=prompt_panel, llm=llm)




    ##panel -> prompt
    prompt_prompt = get_prompt(2)
    llm_chain_prompt = LLMChain(prompt=prompt_prompt, llm=llm)



    # ##character description
    # prompt_char = get_prompt(3)
    # llm_chain_prompt = LLMChain(prompt=prompt_char, llm=llm)


    # ##image from prompts
    # pipe = initiate_sdxl()
    # os.makedirs('./images', exist_ok = True)
    # for i in prompts_list:
    #     image = gen_image(i)
    #     image.save('image_{i}.jpg')
    

path = r"D:\pixi_plot\tom_sawyer-4.pdf"
main(path)