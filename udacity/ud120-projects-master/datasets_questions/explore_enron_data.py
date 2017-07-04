#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
poi_data = open("../final_project/poi_names.txt", "r").read()
'''print len(enron_data['METTS MARK'])
i = 0
for a in enron_data:
    if enron_data[a]["poi"] == 1 :
        i = i + 1
        print a
print i
#str.split(str="", num=string.count(str))
print poi_data
'''
for a in enron_data:
    if a == 'SKILLING JEFFREY K':
        print enron_data[a]