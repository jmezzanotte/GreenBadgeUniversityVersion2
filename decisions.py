#edit
# Simple program to decide if a person is accepeted into college
# Varables to compair: Age, GPA, Parents, SAT Score

print("Welcome to our college application, please answer the following questions to apply.")

age = float(input("How old are you? :  "))
gpa = float(input("What was your high school GPA? :  "))
parent = input("Did your parrents attend our school? (y/n) :  ")
sat = float(input("What was your SAT Score? :  "))

age_tf = True if age <= 55 else False
gpa_tf = True if gpa >= 3 else False
parent_tf = True if parent == "y" else False
sat_tf = True if sat >= 1700 else False

'''
# Check Age
if age <= 55:
    age_tf = True
# Check GPA
if gpa >= 3:
    gpa_tf = True
# Check Parents
if parent == "y":
    parent_tf = True
# Check SAT
if sat >= 1700:
    sat_tf = True
'''

if age_tf and gpa_tf and parent_tf and sat_tf == True:
    print("Welcome to our college.")
elif age_tf and gpa_tf and sat_tf or parent_tf == True:
    print("Welcome to our college.")
else:
    print("sorry you have been denied.")