'''
Created on Feb 7, 2012

@author: stanvp
'''

from elixir import *
from webcredibility.model import *
import csv
import os
import sys
import urllib
import random
import nltk
import tempfile
from nltk.classify import accuracy 

def test(documents):
    random.shuffle(documents)
    
    featuresets = [(document_features(d), document_category(d)) for d in documents]
    train_set, test_set = featuresets[100:], featuresets[:100]
    
    #naive_bayes(train_set, test_set)
    #maximum_entropy(train_set, test_set)
    #weka(train_set, test_set)
    #decision_tree(train_set, test_set)
    pyml_svm(train_set, test_set)
    
def pyml_svm(train_set, test_set):
    print '--- pyml.svm ---'
    from PyML import SparseDataSet, svm
            
    train_data = SparseDataSet([features for features, c in train_set], L = [c for features, c in train_set])
    test_data  = SparseDataSet([features for features, c in test_set], L = [c for features, c in test_set])
    
    classifier = svm.SVM(optimizer = 'liblinear', loss = 'l2')
    
    classifier.train(train_data)
    
    print classifier.cv(train_data, 5)    
    print classifier.test(test_data)
    

def weka(train_set, test_set, algorithm="svm"):
    from nltk.classify import weka    
    print '--- nltk.classify.weka %s ---' % algorithm
    temp_dir = tempfile.mkdtemp()
    classifier = nltk.classify.WekaClassifier.train(temp_dir  + '/cred.model', train_set, algorithm)
    print 'Overall accuracy:', accuracy(classifier, test_set)    


def svm(train_set, test_set):
    print '--- nltk.classify.svm ---'
    classifier = nltk.classify.SvmClassifier.train(train_set)
    print 'Overall accuracy:', accuracy(classifier, test_set)
    classifier.show_most_informative_features(10)


def maximum_entropy(train_set, test_set):
    print '--- nltk.classify.maximum_entropy ---'
        
    from nltk.classify import megam
    megam.config_megam()    
    
    classifier = nltk.classify.MaxentClassifier.train(train_set, "megam")
    
    print 'Overall accuracy:', accuracy(classifier, test_set)
    classifier.show_most_informative_features(10)
    
    
def naive_bayes(train_set, test_set):
    print '--- nltk.classify.naive_bayes ---'
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    
    print 'Overall accuracy:', accuracy(classifier, test_set)
    classifier.show_most_informative_features(10)   
    
    
def decision_tree(train_set, test_set):
    print '--- nltk.classify.decision_tree ---'
    classifier = nltk.DecisionTreeClassifier.train(train_set)
    
    print 'Overall accuracy:', accuracy(classifier, test_set)
    
    
def document_features(document):
    features = {}
    
    for f in document.features:
        features[f.name.encode("utf-8")] = f.value
    
    return features

def document_category(document):
    if document.rating > 3:
        return 'credible'
    else:
        return 'non-credible'