import pandas as pd
import re
import time
import matplotlib.pyplot as plt


df = pd.read_csv("C:/Users/liamw/Documents/ATC&CS/PythonStats/train.csv")

print("Hello and welcome to Stats Summary Simulator! This application will take in your data, and can provide you with a quick, pre-programmed summary, or you can ask the bot to perform specific statistics calculations for you.")


#quick mood checker
a = input("Before we start, how are you today? ")

good = ['good', 'great', 'exceptional', 'marvelous', 'decent', 'pretty good', 'well']
bad = ['bad', 'horrible', 'poor', 'tired', 'exhausted']
temp = False
for i in range(len(good)):
    if re.search(good[i], a):
        if re.search('not', a) is not None:
            pass
        else:
            print("That's great, now we may begin!")
            temp = True

if temp == False:
    for i in range (len(bad)):
        if re.search(bad[i], a):
            if re.search('not', a):
                pass
            else:
                print("That's too bad. Hopefully this app will make you feel better :)")
                temp = True

if temp == False:
    print("Thanks for your input! Lets get started!")




#start of data analysis
time.sleep(1)
print("Now onto the stats stuff. In SSS Version 1.0, you will be allowed to input your own dataset")
print("However, as of now, I am restricted to using the titantic dataset from the Kaggle competiton")
print("In the next input, you can tell me what to do. Here are my functions:")
print("columns: I will give you the names of all of the columns")
print("summarize: I will give you a tailored and detailed overview of the dataset")
print("mean/median/standard deviation: I will give you the mean, mean, standard deviation")
print("head: I will give you all the data for the first couple rows of the dataset")
print("relationship: I will tell you the correlation between the two and what that means")

in_progress = True
first = True
while in_progress:
    #start logic
    if first:
        decision = input("What would you like to do first? ")
        first = False
    else:
        decision = input("What would you like to do? ")

    #print column values
    if decision == "columns":
        print(df.columns.values)
    
    #show mean, median, or standard deviation
    elif decision == "mean" or decision == "median" or decision == "standard deviation":
        column = input(f"Which column would you like the {decision} for (Fare or Age)? ")
        found = False
        for i in range(len(df.columns)):
            if df.columns[i] == column:
                found = True
            else:
                pass
        if found == True:
            if decision == "mean":
                output = df[column].mean()
            elif decision == "median":
                output = df[column].median()
            else:
                output = df[column].std()
            print(f"The {decision} of {column} is {output}")
        else:
            print("Please try again, incorrect column requested. Type columns to see column names")
    elif decision == "head":
        print(df.head())
    elif decision == "relationship":
        col1 = input("First Column: ")
        col2 = input("Second Column ")
        correlation = df[col1].corr(df[col2])
        if correlation > 0:
            sign = "positive, which means that as one goes up so does the other. "
        else:
            sign = "negative, which means that as one goes up, the other goes down. "
        if abs(correlation) > 0.5:
            magnitude = f"The significance of the relationship between {col1} and {col2} is high, which means they are closely associated"
        else:
            magnitude = f"The significance of the relationship between {col1} and {col2} is low, which means they are not closely associated"
        print(f"The correlation test shows the the correlation between {col1} and {col2} is {sign} {magnitude}")
    elif decision == "summarize":
        print(df.describe())

    elif decision == "quit":
        in_progress = False
    else:
        print("I'm sorry, you did not enter a correct command, please try again")
    time.sleep(3)

print("Thank you for chatting!")
