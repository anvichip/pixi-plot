## Importing Libraries
#from langchain import LLMChain
from langchain.chains import LLMChain
import os
from scripts import save_summaries, read_pages
from langchain.document_loaders import PyPDFLoader
from llama_models import intialize_pipeline
from prompts import get_prompt
from langchain import HuggingFacePipeline
from sdxl import initiate_sdxl, gen_image

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
    #print(prompt_summary)
    llm_chain_summary = LLMChain(prompt=prompt_summary, llm=llm)
    save_summaries(llm_chain_summary,document)

    
    ##summmary of all pages
    #prompt_summary = get_prompt(0)
    # llm_chain_summary = LLMChain(prompt=prompt_summary, llm=llm)
    # all_pages_text = read_pages('./summaries')
    # all_pages_summary = save_summaries(all_pages_text)


    ##summary -> panels
    prompt_panel = get_prompt(1)
    #print(prompt_panel)
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