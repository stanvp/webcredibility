# -*- coding: utf-8 -*-
#!/usr/bin/env python

from elixir import *
from webcredibility.model import *
from webcredibility import corpus, classifier
import sys
import yaml

config = yaml.load(open("config.yml"))

metadata.bind = config["db"]["uri"]
metadata.bind.echo = True

action = sys.argv[1]

if action == "setup":
    create_all(True)
    print "Database " + config["db"]["uri"] + " created."
    
elif action == "load":
    dirpath = sys.argv[2]
    corpus.load(dirpath)
    print "Loaded corpus data."

elif action == "extract":
    documents = Document.query.all()
    
    features_functions = [
            #text.punctuation_marks,
            #text.sentiment,
            #text.spelling_errors,
            #text.text_complexity,
            #social.page_rank
            ]
    
    corpus.extract_features(documents, features_functions)
    
    print "Features extracted and loaded into the database."
    
elif action == "classify":
    documents = Document.query.all()
    classifier.test(documents)
    
elif action == "drop":
    drop_all()
    print "Tables dropped."
else:
    print "Please choose action: setup, load, drop"