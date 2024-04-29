# import requests
# import time

# from langchain.document_loaders import PyPDFLoader

# # Load the pdf file from the path
# loader = PyPDFLoader('tom_sawyer-4.pdf')
# document = loader.load()
# text = document[0].page_content

# text_list = []
# text_list.append(text)


# url = "https://anvichip--pixiplot-cli.modal.run"

# myobj = {'auth': 1,'text':text_list, 'task_num': 1}

# x = requests.post(url, json = myobj)
# next_text = []
# print("Task 1")
# print(x.text)
# next_text.append(x.text)
# myobj = {'auth': 1,'text':next_text, 'task_num': 2}
# time.sleep(20)
# x = requests.post(url, json = myobj)
# next_text = []
# print("Taks 2")
# print(x.text)
# next_text.append(x.text)
# #time.sleep(3)
# myobj = {'auth': 1,'text':next_text, 'task_num': 3}

# x = requests.post(url, json = myobj)
# print("Task-3")
# print(x.text)


import time
import requests
from langchain_community.document_loaders import PyPDFLoader

def call_llm_api(pdf_path):
    # Load the PDF file
    loader = PyPDFLoader(pdf_path)
    document = loader.load()
    text = document[0].page_content
    
    # Initialize list to store processed text

    processed_texts = []
    for page in document:
        text = page.page_content
        processed_texts.append(text)

    print(processed_texts)
    print(len(processed_texts))
    
    # URL of the LLM API
    llm_api_url = "https://anvichip--pixiplot-cli.modal.run"

    # Define payload for the first task
    payload = {'auth': 1, 'text': processed_texts, 'task_num': 1}

    # Send request for the first task
    response = requests.post(llm_api_url, json=payload)
    
    print("Task 1")
    print(response.text)

    # Extract processed text from the response
    processed_texts = [response.text]

    # Define payload for the second task
    payload = {'auth': 1, 'text': processed_texts, 'task_num': 2}

    # Send request for the second task after waiting for some time (adjust time.sleep if needed)
    time.sleep(20)  # Adjust sleep time as needed
    response_panel = requests.post(llm_api_url, json=payload)
    
    print("Task 2")
    print(response_panel.text)

    # Extract processed text from the response
    processed_texts = [response_panel.text]

    # Define payload for the third task
    payload = {'auth': 1, 'text': processed_texts, 'task_num': 3}

    # Send request for the third task
    response = requests.post(llm_api_url, json=payload)
    
    print("Task 3")
    print(response.text)

    # Return the final processed text or any other relevant data based on your requirement
    return response.text,response_panel.text

 

call_llm_api(r'D:\deeplearning project\pixi-plot\tom_sawyer-4.pdf')



