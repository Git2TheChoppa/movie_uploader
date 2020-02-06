#------------------------------------------------------------------------------
# Imports
#------------------------------------------------------------------------------
#import pandas as pd
#import numpy as np
import boto3
import os
import re
#------------------------------------------------------------------------------
# Main
#------------------------------------------------------------------------------
#Global
s3 = boto3.resource('s3')

def movie_finder():
    
    ext = ".MP4"
    movie_pattern = re.compile(ext)
    for file in os.listdir("."):
        if movie_pattern.search(file):
            print(file)
            s3.Object('your-bucket-name', str(file)).put(Body=open(str(file), 'rb'))

movie_finder()

