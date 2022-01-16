# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 17:00:39 2022

@author: EL221XK
"""

#Loading Packages
import numpy as np
import pandas as pd
import transformers
import sklearn
import sentence_transformers
from transformers import AutoTokenizer, TFAutoModelForSequenceClassification
from transformers import pipeline
from sentence_transformers import SentenceTransformer, util
from sklearn.metrics.pairwise import cosine_similarity
similarity_model = SentenceTransformer('distilbert-base-nli-stsb-mean-tokens')

#%% 
#Classification Model
tokenizer = AutoTokenizer.from_pretrained("d4data/environmental-due-diligence-model")
model = TFAutoModelForSequenceClassification.from_pretrained("d4data/environmental-due-diligence-model")
classifier = pipeline('text-classification', model=model, tokenizer=tokenizer) # cuda = 0,1 based on gpu availability

#%%
def load_embeddings():
    return pd.read_csv('data/embeddings.csv')

def predict(text_input):
    #running the classification model to predict the classes
    edd_classification = classifier(text_input)
    edd_label = edd_classification[0]['label']
    edd_score = edd_classification[0]['score']
    
    #running due diligence ranking module
    # due diligence ranking dictionary
    embeddings_text = np.float64(similarity_model.encode([text_input]))
    embeddings_df = load_embeddings()
    
    
    if edd_label == 'Remediation Activities':
        embeddings_dict = np.array(embeddings_df.iloc[0, :]).reshape(1, -1) 
    
    if edd_label == 'Groundwater-Surfacewater interaction':
        embeddings_dict = np.array(embeddings_df.iloc[1, :]).reshape(1, -1)

    if edd_label == 'Contaminants':
        embeddings_dict = np.array(embeddings_df.iloc[2, :]).reshape(1, -1)
    
    if edd_label == 'Extent of contamination':
        embeddings_dict = np.array(embeddings_df.iloc[3, :]).reshape(1, -1)
        
    if edd_label == 'Contaminated media':
        embeddings_dict = np.array(embeddings_df.iloc[4, :]).reshape(1, -1)        
        
    if edd_label == 'Source of contamination':
        embeddings_dict = np.array(embeddings_df.iloc[5, :]).reshape(1, -1)
        
    if edd_label == 'Depth to Water':
        embeddings_dict = np.array(embeddings_df.iloc[6, :]).reshape(1, -1)

    if edd_label == 'GW Velocity':
        embeddings_dict = np.array(embeddings_df.iloc[7, :]).reshape(1, -1)
        
    if edd_label == 'Remediation Standards':
        embeddings_dict = np.array(embeddings_df.iloc[8, :]).reshape(1, -1)
            
    if edd_label == 'Remediation Goals':
        embeddings_dict = np.array(embeddings_df.iloc[9, :]).reshape(1, -1)  
        
    if edd_label == 'Geology':
        embeddings_dict = np.array(embeddings_df.iloc[10, :]).reshape(1, -1)
    
                                        
    cosine_scores = util.cos_sim(embeddings_text, embeddings_dict)
    
    final_probability = np.float64(cosine_scores)
    
    if final_probability > 0.3:
        return [edd_label, np.float64(cosine_scores)]
    else:
        return ["Not Relevant", np.float64(cosine_scores)]

#%%

