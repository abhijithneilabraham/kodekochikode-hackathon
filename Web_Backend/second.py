#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 21:51:43 2019

@author: abhijithneilabraham
"""

from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    
     return 'This is homepage'
@app.route('/about')
def about():
    
    return '<h2> About page </h2>'
 
if __name__ == "__main__":
    app.run(debug = True)
