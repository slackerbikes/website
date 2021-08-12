import pandas as pd
import datetime
from datetime import date
import csv

import django

import os

filename = 'data/events_2020.csv'

def formatDF(filename):
    ## Create pandas dataframe w/ datetime index
    with open(filename) as f:
        df = pd.read_csv(f)
        df['Day'] = pd.to_datetime(df['Day'],format='%d/%m/%Y')
        df = df.set_index(['Day'])
    return df

def populate(df):
    ## Create new object for each event (row)
    for index,row in df.iterrows():
        add_event(index,row)

def add_event(index,row):
    ## Create new object
    g = gig.objects.get_or_create(date=index)[0]
    g.weekday = row['DoW']
    g.band = row['Booking']
    g.save()
    return g

if __name__ == '__main__':
    ## Run population script
    print("Starting gig population script")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE','events.settings') 
    django.setup()
    from events.models import gig
    df = formatDF(filename)
    populate(df)