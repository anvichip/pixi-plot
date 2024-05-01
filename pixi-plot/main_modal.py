from typing import Dict
import modal

MODEL = "meta-llama/Llama-2-7b-chat-hf"


def download_models():
    from huggingface_hub import login
    login(token = "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")

    from transformers import AutoTokenizer, AutoModelForCausalLM
    # from token_api import hf_token
    import os
    print(os.listdir("."))
    tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-chat-hf", 
                                            # token = "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", 
                                            #cache_dir = './models'
                                            )
    model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b-chat-hf"
                                        #device_map='auto',
                                        #torch_dtype=torch.float16,
                                        #use_auth_token=True,
                                        #cache_dir = './models',
                                        #token = hf_token
                                        )
    # model = AutoModelForCausalLM.from_pretrained("TheBloke/Llama-2-13B-GGUF", model_file="llama-2-13b.q4_K_M.gguf", model_type="llama", gpu_layers=50)
    tokenizer.save_pretrained("./models/hf-frompretrained-download/Llama-2-7b-chat-hf/")
    model.save_pretrained("./models/hf-frompretrained-download/Llama-2-7b-chat-hf/")
    
    print(os.listdir("."))

host_machine_code = (
    modal.Image.debian_slim()
    .run_commands(
        "apt-get update && apt-get -y upgrade",
        "apt-get install -y curl python3 python3-pip python-is-python3",
    )
    .pip_install(
        "torch", "transformers", "sentencepiece", "langchain", "PyPDF", "llama-index", "doc2text", "huggingface_hub", "accelerate", 
        "gdown", "langchain-community", "langchain_core"
    )
    .run_function(
        download_models
    )
    .run_commands(
        'gdown https://drive.google.com/uc?id=16mOoOZIT85qE3PxCtIqIry1kIu8ieRm-',
    )
)

stub = modal.Stub(name="pixiplot", image=host_machine_code)


@stub.cls(gpu="A100", container_idle_timeout=600)
class depModal:
    # @modal.enter()
    def intialize_pipeline(self):
        import os
        # from huggingface_hub import login
        # login(token = "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")

        from transformers import AutoTokenizer, AutoModelForCausalLM
        import torch
        from transformers import pipeline

        import subprocess
        # from token_api import hf_token

        # print(os.listdir("."))

        # tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-chat-hf", 
        #                                         # token = "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", 
        #                                         cache_dir = '/root/models/hf-frompretrained-download/Llama-2-7b-chat-hf'
        #                                         )

        # model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b-chat-hf",
        #                                         device_map='auto',
        #                                         torch_dtype=torch.float16,
        #                                         #use_auth_token=True,
        #                                         cache_dir = '/root/models/hf-frompretrained-download/Llama-2-7b-chat-hf',
        #                                         #token = hf_token
        #                                         )
        
        tokenizer = AutoTokenizer.from_pretrained('/root/models/hf-frompretrained-download/Llama-2-7b-chat-hf', 
                                                # token = "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", 
                                                # cache_dir = '/root/models/hf-frompretrained-download/Llama-2-7b-chat-hf'
                                                torch_dtype = torch.float16,
                                                )

        model = AutoModelForCausalLM.from_pretrained('/root/models/hf-frompretrained-download/Llama-2-7b-chat-hf',
                                                device_map='auto',
                                                torch_dtype=torch.float16,
                                                #use_auth_token=True,
                                                # cache_dir = '/root/models/hf-frompretrained-download/Llama-2-7b-chat-hf',
                                                #token = hf_token
                                                )
        
        # model = model.to('cuda')
        # tokenizer = tokenizer.to('cuda')

        # print(os.listdir("models"))

        print("The model has been loaded inside model")

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
        
        print("Pipeline has been constructed")

        # output = subprocess.check_output(["pip install gdown", "gdown https://drive.google.com/uc?id=16mOoOZIT85qE3PxCtIqIry1kIu8ieRm-"])

        print(os.listdir('.'))

        return pipe

    def initialize_llm_chain(self, prompt,llm):
        from langchain.chains import LLMChain

        llm_chain = LLMChain(prompt=prompt, llm=llm)
        return llm_chain

    def load_pdf(self, path):
        # from langchain.document_loaders import PyPDFLoader
        from langchain_community.document_loaders import PyPDFLoader

        loader = PyPDFLoader(path) ## Load the pdf file from the path
        document = loader.load()
        return document
    
    print("Model successfully loaded\nAttempting generation")

# ==========================================================================
# Functions to read
# ==========================================================================

    def read_pages(self, path_folder):
        import os
        text = ""
        directory = path_folder
        for filename in os.listdir(directory):
            if(filename.endswith('.txt')):
                filepath = os.path.join(directory, filename)

                with open(filepath,'r') as f:
                    text += f.read() 
        
        return text

    ## Function to generate a summary using the llama prompt
    def generate_summary(self, llm_chain, text):
        print("generate_summary" + str(type(text)))
        output = llm_chain.run(text)
        extract = output.split('[/INST]')
        return extract[1]

    ## Function to save the generated summaries in a folder and take out summaries of all files in a folder
    def save_summaries(self, llm_chain, text_list):
        import os
        import logging
        # Directory to save the summaries
        # summaries_directory = "/root/summaries/"

        # Create the "summaries" directory if it doesn't exist
        # os.makedirs(summaries_directory, exist_ok=True)

        # if(type(document) == 'list'):
        print("In save_summary list branch")
        print("save_summaries" + str(type(text_list)))
        summaries_list = []
        for i in text_list:
            summary = self.generate_summary(llm_chain, i)
        # Iterate over each chapter
        # for i, chapter_content in enumerate(document, start=1):
        #     # Generate summary for the chapter
        #     summary = self.generate_summary(llm_chain, chapter_content)

            # Write the summary to a text file
            # summary_file_path = os.path.join(summaries_directory, f'summary_page_{i}.txt')
            # with open(summary_file_path, 'w') as f:
            #     f.write(summary)
        summaries_list.append(summary)

            
        logging.info('Files saved in Summary')
        print(os.listdir('/root/'))
        return summaries_list
        # elif(type(document) == 'str'):
        #     text = self.generate_summary(document)
        #     return text


    ## Function to convert summaries into panels
    def generate_panels(self, llm_chain,text):

        output = llm_chain.run(text)
        extract = output.split('[/INST]')
        return extract[1]

    
    ## Function to convert panels into prompts
    def generate_prompts(self, llm_chain,text):
        output = llm_chain.run(text)
        extract = output.split('[/INST]')
        return extract[1]


    def get_prompt(self, num):
        from langchain_core.prompts import PromptTemplate
        if(num == 0):
            
            ##Summarizer
            template_summary = """
            <s>[INST] <<SYS>>
            You are an expert acting as a book chapter summarizer, your task is to give the important points that will act as summary to the book.
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
            This is the summary. Concise this into maximum 3 important points.
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
            You are a illustrator who makes stories for children. I am giving you some scene descriptions, change them to a very simple single prompt to visualize that scene.
            {text} [/INST]
            """

            prompt = PromptTemplate(
                input_variables=["text"],
                template=template_prompts,
            )
        
        return prompt


    @modal.method()
    def main_run(self,text, task_num):
        from langchain.chains import LLMChain
        import os
        from langchain_community.llms.huggingface_pipeline import HuggingFacePipeline

        print("Working inside main")

        ##??? loader
        # document = self.load_pdf(path)
        # print(type(document))

        ##intialize llama2 pipe
        pipe_llama = self.intialize_pipeline() 
        llm = HuggingFacePipeline(pipeline = pipe_llama, model_kwargs = {'temperature':0}) ##initalize llm 

        if(task_num == 1):
            # document = self.load_pdf(path)
            #summmary of each page
            prompt_summary = self.get_prompt(0)
            llm_chain_summary = LLMChain(prompt=prompt_summary, llm=llm)
            summaries_list = self.save_summaries(llm_chain_summary,text)
            print("summaries saved")
            return summaries_list
        
        elif(task_num == 2):
            ##summary -> panels
            prompt_panel = self.get_prompt(2)
            llm_chain_panel = LLMChain(prompt=prompt_panel, llm=llm)
            # path = '/root/summaries/'
            scenes = []
            # print("Data of type " + str(type(text)) +" received")
            for i in text:
                print("i is of type  " + str(type(i)))
                # print(i)
                # print("Test 1")
                # scene = self.generate_panels(llm_chain_panel, str(i))
                # ==== Alt code ====
                output = llm_chain_panel.run(i)
                # print("Ran that shit")
                extract = output.split('[/INST]')
                
                # print(extract[1])
                # return extract[1]
                # ===================
                # print("Test 2")
                scenes.append(extract[1])
                # print("Scene has been appended")

            # print(os.listdir(path))
            # for i in os.listdir(path):
            #     file_path = os.path.join(path,i)
            #     print(file_path)
            #     with open(file_path, 'r') as f:
            #         text = f.read()
            #     f.close()
            print("Panels Made")
            return scenes
        
        elif(task_num == 3):
            #panel -> prompt
            prompt_prompt = self.get_prompt(1)
            prompts = []
            llm_chain_prompt = LLMChain(prompt=prompt_prompt, llm=llm)
            for i in text:
                prompt = self.generate_prompts(llm_chain_prompt,i)
                prompts.append(prompt)
            print("Prompts Made")
            return prompts

        
        ##summmary of all pages
        #prompt_summary = get_prompt(0)
        # llm_chain_summary = LLMChain(prompt=prompt_summary, llm=llm)
        # all_pages_text = read_pages('./summaries')
        # all_pages_summary = save_summaries(all_pages_text)
        
        # return scenes


@stub.function(gpu="T4", container_idle_timeout=600, cloud="aws")
@modal.web_endpoint(method="POST")
def cli(varD: Dict):
    import os
    try:
        if varD['auth'] == 1:
            dM = depModal()
            print(varD["task_num"])
            return dM.main_run.remote(varD['text'], varD['task_num'])

        else:
            print("error")
        # print(os.listdir("."))
        # print(os.listdir("/"))
        # print(os.listdir("/root/models/"))
        # if varD['auth'] == 1:
        #     if os.path.isfile("/tom_sawyer-4.pdf"):
        #         print("File exists, code will move on as expected")
        #         dM = depModal()
        #         return dM.main_run.remote("/tom_sawyer-4.pdf")
        #     else:
        #         print("Core file does not exist, aborting")
    except Exception as e:
        print("======================== \n Yeah idk that didn't work \n ========================", e)