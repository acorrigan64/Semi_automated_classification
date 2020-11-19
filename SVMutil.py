"""
IMPORTS
"""
import nltk.data
import random
import tkinter as tk


"""
TEST FILES AND TOKENIZER
"""

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
fp = open("test.txt")
data = fp.read()

"""
FUNCTIONS
"""

#Retrieves predictions from trained SVM and trained tokenizer, returns input sentences, labels and confidence levels
def getOutput(data):
    sentences = tokenizer.tokenize(data)
    label_list=[]
    confidence_list=[]
    index = range(len(sentences))
    for i in sentences:
        
        label_list.append(getLabelSVM(i)[0])
        confidence_list.append(getLabelSVM(i)[1])
    dct = {a: {'sentences': b,'Label':c,'Confidence':d} for a, b, c,d in zip(index,sentences,label_list,confidence_list)}
    return dct
    
#Outputs the data to the terminal
def printOutput(data):
    dct = getOutput(data)
    for p_id, p_info in dct.items():
        print("\nText ID:", p_id)
        for key in p_info:
            print(key + ':', p_info[key])
            
 
#Function to return predictions for displaying in interface
def returnOutput(data):
    dct = getOutput(data)
    output = ""
    for p_id, p_info in dct.items():
        output += "\nText ID: {}\n".format(p_id)
        output += "Text: {}\n".format(p_info['sentences'])
        output+= "Label: {}\n".format(p_info['Label'])
        output+= "Confidence: {}\n".format(p_info['Confidence'])
            
    return output
    
