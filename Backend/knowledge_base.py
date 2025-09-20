import os

def load_knowledge_base(directory_path):
    """
    Loads all .txt files from the given directory into a dictionary
    Returns:
        dict: Keys are filenames without ".txt",  values are file contents as strings
    """

    knowledge = {}  # initialise empty dictionary to hold all topics

    # iterate over every file in the directory 

    for filename in os.listdir(directory_path):   # only process .txt files 
        if filename.endswith(".txt"):
            topic_name = filename[:-4]     # Remove ".txt" from filename to get topic 
            file_path = os.path.join(directory_path, filename)   # Full Path to file 

            # open and Read the file 
            with open(file_path, 'r',  encoding='utf-8') as f:
                content = f.read()
            
            knowledge[topic_name] = content      # Store content in dictionary

    return knowledge