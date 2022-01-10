#!/bin/python3
from pyFunc import moduleSys

def AIML():
    print("AIML")
    return "monday"
def tuesday():
    return "tuesday"
def wednesday():
    return "wednesday"
def thursday():
    return "thursday"
def friday():
    return "friday"
def saturday():
    return "saturday"
def sunday():
    return "sunday"
def default():
    return "Incorrect day"

switcher = {
    "20010-000123-A.0": AIML,
    2: tuesday,
    3: wednesday,
    4: thursday,
    5: friday,
    6: saturday,
    7: sunday
    }

def switch(pnNum):
    return switcher.get(pnNum, default)()

switch("20010-000123-A.0")
