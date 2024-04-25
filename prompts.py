### prompt.py
from langchain_core.prompts import PromptTemplate

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