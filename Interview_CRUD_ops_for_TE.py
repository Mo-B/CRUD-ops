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
    # print("Added TE {} to DB".format(dict_args))


def list_available_te(obj):
    # for k, v in te.items.iteritems(): # python2
    for k, v in te.items_.items():  # python3,
        if "Available" in v:
            print(k)


def update_pending_tests(obj, te_name, job_state):
    for k, v in te.items_.items():  # python3,
        if k == te_name:
            if v[1] == 'Pending':
                v[1] = job_state


def remove_pending_jobs(obj, te_name):
    for k in list(te.items_.keys()):
        if k == te_name:
            te.remove(k)


# TE Operations Test.
# First lets create some TEs
te = te_stack()
create_te(te, {'Anritsu': ['Running', 'Pass']})
create_te(te, {'Anite1': ['Running', 'Fail']})
create_te(te, {'Anite2': ['Running', 'Pending']})
create_te(te, {'Azimuth': ['Available', 'Pending']})

# 1. List running Pass/Fail & pending campaigns
#    -P/F/Pending
#    -Show Test Equip ID
print("\n")
print("Adding few minimum TEs")
if not te.is_empty():
    te.printstats()
print("\n")
# # 2. List availablle TE's only
# print("2. List availablle TE's only")
# list_available_te(te)
# # 3. Add a Campaign
# print("3. Add a Campaign")
# create_te(te, {'Anritsu2': ['Running', 'Pending']})
# print(te.printstats())

# 4. Remove a running/pending campaign
# print("4. Remove a running / pending campaign")
# remove_pending_jobs(te, "Anritsu")
# print("\n")
# te.printstats()
# print("\n")
# print(te.printstats())

# # 5. Change order of pending campaign
# print(" 5. Change order of pending campaign")
# update_pending_tests(te, 'Azimuth', 'Updated')
# print("\n After update: \n")
# print(te.printstats())


def main_menu(te):
    print("1. List running Pass/Fail & pending campaigns")
    print("2. Add a Campaign")
    print("3. List availablle TE's only")
    print("4. Remove a running / pending campaign")
    print("5. Change order of pending campaign")
    print("6. Exit")
    selection = True
    while selection:
        selection = int(input("Enter Choice : "))
        if selection == 1:
            if not te.is_empty():
                print("\n")
                te.printstats()
                print("\n")

        elif selection == 2:
            te_state = ""
            job_state = ""
            te_name = input('Enter TE Name : ')
            while True:
                te_state = input('Enter TE state (Running/Available) : ')
                if not te_state.istitle() or te_state not in ('Running', 'Available'):
                    print("Not allowed choice. Retry")
                else:
                    break
            while True:
                job_state = input('Enter job result (Pass/Fail/Pending) : ')
                if not job_state.istitle() or job_state not in ('Pass', 'Fail', 'Pending'):
                    print("Not allowed choice. Retry")
                else:
                    break
            create_te(te, {te_name: [te_state, job_state]})
            print("\n")
            te.printstats()
            print("\n")
        elif selection == 3:
            print("\n")
            list_available_te(te)
            print("\n")
        elif selection == 4:
            avail_te = []
            for k, v in te.items_.items():
                avail_te.append(k)
            print("Available TE's are: {}".format(avail_te))
            te_name = input('Enter TE Name : ')
            if te_name in avail_te:
                remove_pending_jobs(te, te_name)
                print("\n After removal: \n")
                print(te.printstats())
                print("\n")
            else:
                print("TE name not in stack.")

        elif selection == 5:
            pending_jobs_are = []
            for k, v in te.items_.items():
                if "Pending" in v:
                    print(k, v)
                    pending_jobs_are.append(k)
            te_to_change = input('Enter TE name : ')
            new_job_state = input('Enter new job state : ')
            update_pending_tests(te, te_to_change, new_job_state)
            print("\n After update: \n")
            print(te.printstats())
            print("\n")
        elif selection == 6:
            print("\n GoodBye")
            break
        else:
            print("Invalid choice. Enter 1-6")


main_menu(te)
# print(te.printstats())
