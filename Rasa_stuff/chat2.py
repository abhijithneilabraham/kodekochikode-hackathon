#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 12:00:32 2019

@author: abhijithneilabraham
"""

# Imports
#-----------
# rasa core
import logging
from rasa_core import training
from rasa_core.actions import Action
from rasa_core.agent import Agent
from rasa_core.domain import Domain
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.featurizers import MaxHistoryTrackerFeaturizer, BinarySingleStateFeaturizer

from rasa_core.interpreter import RegexInterpreter
from rasa_core.interpreter import RasaNLUInterpreter

# Function
#------------
def train_dialog(dialog_training_data_file, domain_file, path_to_model = 'models/dialogue'):
    logging.basicConfig(level='INFO')
    agent = Agent(domain_file,
              policies=[MemoizationPolicy(max_history=1)])
    training_data = agent.load_data(dialog_training_data_file)
    agent.train(
        training_data,
        augmentation_factor=50,
        epochs=200,
        batch_size=10,
        validation_split=0.2)
    agent.persist(path_to_model)

# Train
#--------
train_dialog('stories.md', 'domain.yml')
rasaNLU = RasaNLUInterpreter('models/nlu/default/chat')
agent = Agent.load("models/dialogue", interpreter= rasaNLU)

a=str(input('enter text here'))
b=agent.handle_text(a)
print(b[0]['text'])
