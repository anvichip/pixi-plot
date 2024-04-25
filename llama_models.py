from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from transformers import pipeline
from langchain import HuggingFacePipeline
from langchain import PromptTemplate,  LLMChain
from token_api import hf_token
import logging
from prompts import get_prompt

def intialize_pipeline():
    #print('In Pipe line function')

    tokenizer = AutoTokenizer.from_pretrained(r"D:\pixi_plot\models\models--meta-llama--Llama-2-7b-chat-hf\snapshots\f5db02db724555f92da89c216ac04704f23d4590"
                                            #token = hf_token, 
                                            #cache_dir = './models'
                                            )

    model = AutoModelForCausalLM.from_pretrained(r"D:\pixi_plot\models\models--meta-llama--Llama-2-7b-chat-hf\snapshots\f5db02db724555f92da89c216ac04704f23d4590",
                                            device_map='auto',
                                            torch_dtype=torch.float16,
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

    #print('success pipe')
    return pipe

def initialize_llm_chain(prompt,llm):
    llm_chain = LLMChain(prompt=prompt, llm=llm)
    return llm_chain


# prompt = get_prompt(0)

# pipe = intialize_pipeline()
# llm = HuggingFacePipeline(pipeline = pipe, model_kwargs = {'temperature':0})
# print("here")
# llm_chain_summary = LLMChain(prompt=prompt, llm=llm)   
# llm_chain_summary.run("She went to the bed and ate an apple")