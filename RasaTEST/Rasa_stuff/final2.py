#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 10:51:21 2019

@author: abhijithneilabraham
"""#!/usr/bin/env python3
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
import csv
import googlemaps
import numpy as np
gmaps = googlemaps.Client(key='AIzaSyDD3BrAMj8NXDunRffUiVkTy9WBfpimLq0') #API_Key
data = "hs.csv"
h_list={}
x=0

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


a=""
while a!="STOP":
    av=str(input('enter text here'))
    if av==" I need immediate healthcare":
        
        
        
        with open(data, 'r') as file:
            reader = csv.reader(file)
            hospital_list = list(reader)
        for a in hospital_list:
            if a[1][0]=='N':
                #print("\n")
                continue
            for i in range(0,15):
                if a[1][i]==',':
                    break
            h_list[x,0]=a[3]
            h_list[x,1]=a[2]
            h_list[x,2]=a[1][0:i]
            h_list[x,3]=a[1][i+1:21]
            h_list[x,5]=a[0]
            x+=1
        LatP = 9.991111 #latitude
        LongP =76.35125#longtitude
        for i in range(0,x):
            t = float(h_list[i,2])-float(LatP)
            p = float(h_list[i,3])-float(LongP)
            if t<0.1 and t>-0.1:
                if p<0.1 and p>-0.1:
                    LatD = h_list[i,2]
                    LongD = h_list[i,3]
                    distance = gmaps.distance_matrix([str(LatP) + " " + str(LongP)], [str(LatD) + " " + str(LongD)], mode='driving')['rows'][0]['elements'][0]
                    h_list[i,4]=distance["distance"]["text"]
                    #print("Name :",h_list[i,0],"\nAddress :",h_list[i,1],"\nDistance :",h_list[i,4],"\n")
        
        #Backend data acquisition
        
        
        with open('HospitalServices.csv', 'r') as file1:
            reader = csv.reader(file1)
            hospital_services = list(reader)
            i=0
        k={}
        for b in hospital_services:
            if i%2==0:
                k[int(i/2)]=b
            i+=1
        
        
        Hospital_Services={}
        for i in range(0,10): #change range to x
            t = float(h_list[i,2])-float(LatP)
            p = float(h_list[i,3])-float(LongP)
            if t<0.1 and t>-0.1:
                if p<0.1 and p>-0.1:
                    Hospital_Services[i,0]=h_list[i,5] #Hospital ID
                    Hospital_Services[i,1]=int(k[i][0])
                    Hospital_Services[i,2]=int(k[i][1])
                    Hospital_Services[i,3]=int(k[i][2])
        
            
        
        #Hospital optimizing algorithm
        TreatmentProbability=[0,0,0,0,0,0,0,0,0,0]
        AdmittanceProbability=[0,0,0,0,0,0,0,0,0,0,0]
        FinalProbability=[0,0,0,0,0,0,0,0,0,0]
        
        
        n=0
        for i in range(0,10):
            t = float(h_list[i,2])-float(LatP)
            p = float(h_list[i,3])-float(LongP)
            if t<0.1 and t>-0.1:
                if p<0.1 and p>-0.1:
                    TreatmentProbability[i]=(Hospital_Services[i,2]/Hospital_Services[i,3])
                    AdmittanceProbability[i]=((TreatmentProbability[i]*Hospital_Services[i,1])/(Hospital_Services[i,2]*Hospital_Services[i,3]))
                    u=h_list[i,4]
                    FinalProbability[i]=(TreatmentProbability[i]*AdmittanceProbability[i]*AdmittanceProbability[i])/(pow(float(u[0:4]),3))
                    #print("Name :",h_list[i,0],"\nAddress :",h_list[i,1],"\nDistance :",h_list[i,4],"\n")
                    #print("Treatment Probability :",TreatmentProbability[i],"\n Admittance Probability :",AdmittanceProbability[i],"\n")
                else:
                    n+=1
            else:
                n+=1
        print("\nThe nearest hospital with minimum patient traffic \n")
        d=max(FinalProbability)
        for i in range(0,10):
            if FinalProbability[i]==d:
                print("Name :",h_list[i,0],"\nAddress :",h_list[i,1],"\nDistance :",h_list[i,4],"\n")
                break
        
        print("\nOther hospitals in the area\n")
        for i in range(0,10):
            t = float(h_list[i,2])-float(LatP)
            p = float(h_list[i,3])-float(LongP)
            if t<0.1 and t>-0.1:
                if p<0.1 and p>-0.1:
                    print("Name :",h_list[i,0],"\nAddress :",h_list[i,1],"\nDistance :",h_list[i,4],"\n")
                    #print("Treatment Probability :",TreatmentProbability[i],"\n Admittance Probability :",AdmittanceProbability[i],"\n")
                
        b=agent.handle_text(av)
        print("Answer:"+b[0]['text'])
        print(b)
            
                
                
        
        
        
