import os
import pandas as pd
import pickle
import base64

os.environ.setdefault('DJANGO_SETTINGS_MODULE','crover.settings')

import django
django.setup()
from crover.models import graph

filepath = "data/"

def convert(np_array):
    np_bytes = pickle.dumps(np_array)
    np_base64 = base64.b64encode(np_bytes)
    return np_base64

def populate():
    for data in os.listdir(filepath):
        title = data
        print("+++++ STORING: ",title, "+++++")
        df = pd.read_csv(filepath+data)
        print("+++++ ADDING TO TABLE +++++")
        add_silo(df,title)

def add_silo(df,title):
    s = graph.objects.get_or_create(title=title)[0]
    s.x = convert(df['x'].to_numpy())
    s.y = convert(df['y'].to_numpy())
    s.temperature = convert(df['temperature'].to_numpy())
    s.save()
    return s

if __name__ == '__main__':
    print("Starting Silo population script")
    populate()