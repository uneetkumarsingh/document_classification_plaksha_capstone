#!/usr/bin/env python
# coding: utf-8

# In[38]:


import docx
import re
import pickle
import copy
import six
import sys
import numpy as np
from time import time
sys.modules['sklearn.externals.six'] = six
import warnings
warnings.filterwarnings("ignore")


# In[13]:


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


# In[14]:


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


# In[15]:


def load_models(model_path, vectorizer_path):
    '''
    params:
        model_path: path where pickel file of the model is
        vectoriser_path: path where pickle file of vectoriser is
    return:
        model: model object
        vectoriser: vectoriser object
    '''
    model = pickle.load(open(model_path, 'rb'))
    vectorizer = pickle.load(open(vectorizer_path, 'rb'))
    print("+++Model and Vectoriser loaded+++")
    return model, vectorizer


# In[39]:


def predict(model, vectorizer, file_path):
    text = load_text(docx_path)
    t1 = time()
    x = vectorizer.transform(text)
    t2 = time()
    y = model.classes_[model.predict(x).astype(int)][0]
    t3 = time()
    prob = np.max(model.predict_proba(x))
    return {"class":y, "probability":prob, "vectorization_time":t2-t1, "inference_time":t3-t2}


# In[28]:


#Loading model, vectoriser
model_path = "estimator_v3_pruned.sav"
vectoriser_path = "tfidf_v3_min_max_df.sav"

#dummy docx_path
docx_path = "../new_gold_annotated/ASAA_36.docx"
model, vectorizer = load_models(model_path, vectoriser_path)


# In[29]:


param = {
    "model": model,
    "vectorizer": vectorizer,
    "file_path": docx_path
}


# In[40]:


predict(**param)


# In[ ]:

if __name__ == "__main__":
    print(predict(**param))


