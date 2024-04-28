import requests
import time

from langchain.document_loaders import PyPDFLoader

# Load the pdf file from the path
loader = PyPDFLoader('tom_sawyer-4.pdf')
document = loader.load()
text = document[0].page_content

text_list = []
text_list.append(text)


url = "https://anvichip--pixiplot-cli.modal.run"

myobj = {'auth': 1,'text':text_list, 'task_num': 1}

x = requests.post(url, json = myobj)
next_text = []
print("Task 1")
print(x.text)
next_text.append(x.text)
myobj = {'auth': 1,'text':next_text, 'task_num': 2}
time.sleep(20)
x = requests.post(url, json = myobj)
next_text = []
print("Taks 2")
print(x.text)
next_text.append(x.text)
#time.sleep(3)
myobj = {'auth': 1,'text':next_text, 'task_num': 3}

x = requests.post(url, json = myobj)
print("Task-3")
print(x.text)


