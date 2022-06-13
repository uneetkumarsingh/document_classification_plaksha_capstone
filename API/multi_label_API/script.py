#!/usr/bin/env python
# coding: utf-8

# In[21]:


import docx
import re
import pickle
from time import time
import numpy as np
import warnings
warnings.filterwarnings("ignore")


# In[22]:


def clean_text(text):
    '''
    for removing special characters, lowering the case and removing 
    punctuations
    
    params:
        text: str - text string of the document to be cleaned 
    returns:
        text_list : list of cleaned text that has length one. 
                    tfidf_vectoriser accepts only list of strings
    '''
    pattern = r'[^A-Za-z ]+'
    clean_text = [re.sub(pattern,'', str(x.lower())) for x in text.split(" ")]
    text_list = " ".join(clean_text)
    #if you are sending this to the model,

    return [text_list]


# In[23]:


def load_text(path):
    '''
    Reads text from file stored at path
    '''
    path = path.rstrip("\n")
    doc_object = docx.Document(path)
    text = " "
    heading = " "
    for para in doc_object.paragraphs:
        text+=""+para.text

    clean_t = clean_text(text)
    return clean_t


# In[24]:


def load_models(model_path, vectoriser_path):
    '''
    params:
        model_path: path where pickel file of the model is
        vectoriser_path: path where pickle file of vectoriser is
    return:
        model: model object
        vectoriser: vectoriser object
    '''
    model = pickle.load(open(model_path, 'rb'))
    vectoriser = pickle.load(open(vectoriser_path, 'rb'))
    print("+++Model and Vectoriser loaded+++")
    return model, vectoriser


# In[25]:


def convert_multilabel(y_pred):
    
    '''
    It takes multilable prediction and converts it into a single Label
    '''
    
    labels = {('non-rp', 'non-rtrc', 'abstract'): 'Abstract', 
    ('non-rp', 'non-rtrc', 'non-abstract'): 'Other', 
    ('non-rp', 'rtrc', 'non-abstract'): 'Response to reviewer comments', 
    ('rp', 'non-rtrc', 'non-abstract'): 'Research paper_Journal article'}
    labels_ = ["Abstract", "Other", "Response to reviewer comments", "Research paper_Journal article"]

    y_pred_simple = []
    
    for i in np.array(y_pred):
        y_pred_simple.append(labels[tuple(i)])
    
    return y_pred_simple


# In[26]:


def predict(model, vectorizer, file_path):
    text = load_text(docx_path)
    t1 = time()
    x = vectorizer.transform(text)
    t2 = time()
    y = convert_multilabel(model.predict(x))
    t3 = time()
    prob = np.prod(np.max(np.array(model.predict_proba(x)).squeeze(1),axis = 1))
    return {"class":y, "probability":prob, "vectorization_time":t2-t1, "inference_time":t3-t2}


# In[27]:


#Loading model, vectoriser
model_path = "estimator_v6_rfc_bucket.sav"
vectoriser_path = "tfidf_v6_bucket.sav"

#dummy docx_path
docx_path = "../../../new_gold_annotated/ASAA_36.docx"
model, vectorizer = load_models(model_path, vectoriser_path)


# In[28]:


param = {
    "model": model,
    "vectorizer": vectorizer,
    "file_path": docx_path
}


# In[29]:


predict(**param)

