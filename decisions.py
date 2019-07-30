"""
Simple program to decide if a person is accepeted into college
Varables to compair: Age, GPA, Parents, SAT Score
"""

print("Welcome to our college application, please answer the following questions to apply.")

# These are constants. They are variable values that are not supposed to change.
# Python convention says constants should be uppercase.
SAT_SCORE_LOW = 400
SAT_SCORE_HIGH = 1700
GPA_LOW = 1.0
GPA_HIGH = 4.0

age = None
gpa = None
parent = None
sat = None

while True:

    try:

        if not age:
            age = float(input("How old are you? :  "))

        if not gpa:
            gpa = float(input("What was your high school GPA? :  "))

            if gpa < GPA_LOW or gpa > GPA_HIGH:
                gpa = None
                raise ValueError("Please enter a GPA value between {0} and {1}".format(GPA_LOW, GPA_HIGH))

        if not parent:
            parent = input("Did your parents attend our school? (y/n) :  ")

            if parent not in ['y', 'n']:
                # Must reset parent to None if input is invalid
                parent = None
                raise ValueError("Please enter either 'y" or 'n')

        if not sat:
            sat = float(input("What was your SAT Score? :  "))

            if not sat in range(SAT_SCORE_LOW, SAT_SCORE_HIGH + 1):
                sat = None
                raise ValueError("SAT score must be between {0} and {1}".format(SAT_SCORE_LOW, SAT_SCORE_HIGH))
        break
    except ValueError as e:
        print(e)
        continue
    except Exception as e:
        print(e)
        continue


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