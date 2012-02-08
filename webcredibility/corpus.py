# -*- coding: utf-8 -*-
'''
Corpus related operations

@author: Stanislav Peshterliev
'''

from elixir import *
from webcredibility.features import text, social
from webcredibility.model import *
import csv
import os
import sys
import urllib


def extract_features(documents, features_functions):    
    for document in documents:
        for features_function in features_functions:
            features = features_function(document)
            for fname, fval in features.items():
                document.features.append(Feature(name=fname, value=fval))        
    
    session.commit()               

def load(dirpath):
    cachedpages = os.path.join(dirpath, "cachedpages")
    ratings = os.path.join(dirpath, "web_credibility_1000_url_ratings.csv")
    expert_ratings = os.path.join(dirpath, "web_credibility_expert_ratings_for_test_set.csv")
        
    documents = []
    
    # load ratings    
    ratings_reader = csv.reader(open(ratings, 'rb'), delimiter=',', quotechar='"')
    i = 0
    
    for row in ratings_reader:  
        print str(i) + " " + row[3]
        
        parts = row[3].replace("http://", "").replace(".jhtml", ".html").split("/")
        
        if len(parts) <= 1:
            parts.append("index.html")
            
        if parts[-1] == "":
            parts[-1] = "index.html"
            
        if parts[-1].find(".htm") == -1 and parts[-1].find(".asp") == -1:
            parts[-1] = parts[-1] + ".html"
            
        filename = os.path.join(cachedpages, os.path.sep.join(parts))    
          
        if os.path.isfile(filename):
            f = open(filename)
        else:                
            f = urllib.urlopen(row[3])
            
        html = f.read()
        f.close()
        
        documents.append(Document(topic=row[0], search_query=row[1], content=unicode(html, errors='replace'),
                            result_rank=int(row[2]), url=unicode(row[3], errors='ignore'), rating=int(row[4])))
        i += 1        
    
    # load expert ratings  
    expert_ratings_reader = csv.reader(open(expert_ratings, 'rb'), delimiter=',', quotechar='"')
        
    for row in expert_ratings_reader:
        for document in documents:
            if document.url == row[2]:
                if document.expert_rating1 != None:
                    document.expert_rating1 = int(row[4])
                else:
                    document.expert_rating2 = int(row[4])
                break
        
    session.commit()
    