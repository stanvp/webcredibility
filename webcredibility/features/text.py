# -*- coding: utf-8 -*-

import nltk
import nltk.data
from nltk.util import clean_html, ngrams
import operator
import enchant
import math


def punctuation_marks(document):
    text = clean_html(document.content)
    return {
     "#dots": text.count("."),
     "#commas": text.count(","),
     "#questions": text.count("?"),
     "#exclamations": text.count("!")
    }
  
    
def spelling_errors(document):
    d = enchant.Dict("en_US")
    num = 0
    tokens = nltk.word_tokenize(clean_html(document.content))
    
    for token in tokens:
        if len(token) >= 2 and not d.check(token):
            num += 1
    
    return {
     '#spelling_errors': num
    }
  
    
def text_complexity(document):
    word_freq = nltk.FreqDist(w.lower() for w in nltk.word_tokenize(clean_html(document.content)))
    n = len(word_freq.samples())
    c = 0.0
    log10_n = math.log10(n)
    
    for f in word_freq.items():
        c += f[1] * (log10_n - math.log10(f[1]))
    
    c = c * (1.0/len(word_freq.samples()))
    
    return {
     '@text_complexity': c
    }
    
    
def sentiment(document):
    classifier = nltk.data.load("classifiers/polarity _NaiveBayes.pickle")
    words = nltk.word_tokenize(clean_html(document.content))
    words_ngrams = reduce(operator.add, [words if n == 1 else ngrams(words, n) for n in [1,2]])
    
    features = dict([(words_ngram, True) for words_ngram in words_ngrams])    
    
    polarity = classifier.classify(features)
    
    return {
     "?polarity": (0 if polarity[0] == "neg" else 1) 
    }
    
    
def part_of_speach(document):
    text = clean_html(document.content)
    sentences = nltk.sent_tokenize(text)
    
    features = {}
    
    for sentence in sentences:
        tokens = nltk.word_tokenize(sentence)
        tagged = nltk.pos_tag(tokens)
        
        for word, tag in tagged:
            if len(tag) < 2: continue
             
            fname = "#" + tag
            if fname in features:
                features[fname] += 1
            else:
                features[fname] = 1
                
    return features