#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 06:36:04 2019

@author: abhijithneilabraham
"""

from rasa_nlu.training_data import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu import config
from rasa_nlu.model import Metadata, Interpreter

# Functions
#------------
def train (data, config_file, model_dir):
    training_data = load_data(data)
    trainer = Trainer(config.load(config_file))
    trainer.train(training_data)
    model_directory = trainer.persist(model_dir, fixed_model_name = 'chat')

# Training
#------------
train('nlu_train.md', 'nlu_config.yml', 'models/nlu')
# loading the interpreter 
interpreter = Interpreter.load('./models/nlu/default/chat')

# define function to ask question
def ask_question(text):
    print(interpreter.parse(text))

# asking question
ask_question("How many days in January")
ask_question("How many days in March")

