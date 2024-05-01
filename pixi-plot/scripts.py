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
def save_summaries(llm_chain,document):
    print(type(document))
    # Directory to save the summaries
    summaries_directory = "summaries"

    # Create the "summaries" directory if it doesn't exist
    os.makedirs(summaries_directory, exist_ok=True)

    #if(type(document) == 'list'):
    print("Doc is list")
    # Iterate over each chapter
    for i, chapter_content in enumerate(document, start=1):
        # Generate summary for the chapter
        summary = generate_summary(llm_chain, chapter_content)

        # Write the summary to a text file
        summary_file_path = os.path.join(summaries_directory, f'summary_page_{i}.txt')
        with open(summary_file_path, 'w') as f:
            f.write(summary)
    
        #logging.info('Files saved in Summary')
    
    # elif(type(document) == 'str'):
    #     text = generate_summary(document)
    #     return text


## Function to convert summaries into panels
def generate_panels(llm_chain,text):
 
    output = llm_chain.run(text)
    extract = output.split('[/INST]')
    return extract[1]











