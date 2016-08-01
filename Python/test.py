#!/usr/bin/env bash

__author__ = 'BRB2399'

#Validate import of all libraries
#Yes I know there are better ways to do this, testing for now

import sys
import os
import uuid
import pika
import nltk
import json
from flask import render_template, Response, request, jsonify, app
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *
from nltk.corpus import stopwords
from nltk import tokenize
from nltk import bigrams 
import redis
import string
import re
from elasticsearch import Elasticsearch
import platform
import os
from neo4j.v1 import GraphDatabase, basic_auth
import twython

def main():

    nltk.download('stopwords')
    nltk.download('vader_lexicon')        
        
    print("\n================================================================================\n")
    print("---------------------------------- Platform Information ------------------------")
    print('machine: {}'.format(platform.machine()))
    print('node: {}'.format(platform.node()))    
    print('processor: {}'.format(platform.processor()))    
    print('release: {}'.format(platform.release()))
    print('system: {}'.format(platform.system()))    
    print('version: {}'.format(platform.version()))
    print('uname: {}'.format(platform.uname()))
    
    #mem = virtual_memory()
    #print('memory: {}'.format(mem.total))  # total physical memory available
    
    print('python_build: {}'.format(platform.python_build()))
    print('python_compiler: {}'.format(platform.python_compiler()))
    print('python_branch: {}'.format(platform.python_branch()))
    print('python_implementation: {}'.format(platform.python_implementation()))
    
    print('python_revision: {}'.format(platform.python_revision()))
    print('python_version: {}'.format(platform.python_version()))
    
    print("\n================================================================================\n")
    
    
if __name__ == "__main__":
    main()    
