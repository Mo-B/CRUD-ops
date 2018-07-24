'''
Services Required:
1. List running & pending campaigns
    -P/F/Pending
    -Show Test Equip ID
2. List available Equipments
3. Add a Campaign
4. Remove a running/pending campaign
5. Change order of pending campaign
'''

'''
# Ideally I would like to use MongoDB or MySQL Database to store my data.

import pymysql
conn = pysql.connect(host="localhost", user="root", passwd="",db="mydb")
mycursor = conn.cursor()

# All queuries have to be created and submitted with the following lines. Queries can be anything
# For example
# queries = """CREATE TABLE TestEquip (
                   tename varchar(20) primary key,
                   run_state varchar(20),
                   test_state varchar(20) )"""

mycursor.execute(queries)
conn.commit()

Other libraries I will be needing
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
'''

# Since the PC won't have MongoDB configured, I will use a dictionary and my stack for CRUD operations
from stack import te_stack

# In Django, we have to create a method for every operation, which we can map later to a buttons, check boxes etc on the page from the sites folder. This part we are skipping


def create_te(obj, dict_args):    # Method to add TEs
    obj.push(dict_args)
    #print("Added TE {} to DB".format(dict_args))


def list_available_te(obj):
    # for k, v in te.items.iteritems(): # python2
    for k, v in te.items.items():  # python3,
        if "Available" in v:
            print(k)


def update_pending_tests(obj):
    for k, v in te.items.items():  # python3,
        if v[0] == 'Available' and v[1] == 'Pending':
            v[1] = '(Updated) Pass'


def remove_pending_jobs(obj):
    for k, v in te.items.items():
        if k == 'Anite2' and v[1] == 'Pending':
            print(k)


# TE Operations Test.
# First lets create some TEs
te = te_stack()
create_te(te, {'Anritsu': ['Running', 'Pass']})
create_te(te, {'Anite1': ['Running', 'Fail']})
create_te(te, {'Anite2': ['Running', 'Pending']})
create_te(te, {'Azimuth': ['Available', 'Pending']})
create_te(te, {'Spirent': ['Available', 'Pass']})
create_te(te, {'Agilent': ['Available', 'Pass']})

# 1. List running Pass/Fail & pending campaigns
#    -P/F/Pending
#    -Show Test Equip ID
print("1. List running Pass/Fail & pending campaigns")
if not te.is_empty():
    print(te.printstats())

# 2. List availablle TE's only
print("2. List availablle TE's only")
list_available_te(te)
# 3. Add a Campaign
print("3. Add a Campaign")
create_te(te, {'Anritsu2': ['Running', 'Pending']})
print(te.printstats())

# 4. Remove a running/pending campaign
print("4. Remove a running / pending campaign")
remove_pending_jobs(te)
# print(te.printstats())

# # 5. Change order of pending campaign
# print(" 5. Change order of pending campaign")
# update_pending_tests(te)
# print(te.printstats())
