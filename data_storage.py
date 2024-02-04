# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:41:49 2024

@author: nhlam
"""

"""
Storing data in python
1. Lists
2. Dictionaries
3. Data Frames - specific to pandas
"""

import pandas as pd 

file = pd.read_csv("country_data.csv")

print(file)

"""
    Age Gender       Country
0    39      M  South Africa
1    25      M      Botswana
2    29      F  South Africa
3    46      M  South Africa
4    22      F         Kenya
5    35      F    Mozambique
6    22      F       Lesotho
7    49      M         Kenya
8    30      M         Kenya
9    40      F         Egypt
10   30      M         Sudan
"""

age1 = 30
age2 = 25
age3 = 29

age = [30, 25, 29, 46, 22, 35]

print(age)

"""
[30, 25, 29, 46, 22, 35]
"""

print(age[0])
"""
30
"""

print(min(age))
"""
30
"""

print(sum(age))
"""
187
"""

print(len(age))
"""
len - length
6
"""

avg = sum(age)/len(age)

print(avg)
"""
31.166666666666668
"""

g1 = "M"
g2 = "F"
g3 = "M"
gender = ["M", "F", "M"]

print(age[0:2])
"""
[30, 25]
"""

age.append(100)

print(age)
"""
when you want to add a neumber to a already given set of data
[30, 25, 29, 46, 22, 35, 100]
"""

"""
how can we append the number 100 in the first position (index 0) of the list
print(age)
age.insert (0,100)
"""

"""
Dictionaries - key:value pairs USE CURLY BRACKETS

cat: "a cute animal"

"""

mammals = {"cat": "a cute animal", "lion": "king of the jungle", "elephants": 
           "a gigantic herbivore"}

print(mammals["cat"])


"""
Data frames
df = dataframe
"""   

fruits = ["apple", "banana", "orange", "grape", "kiwi"]
size_nm = [9.8, 10.1, 13.2, 8.7, 20.5]

fruit_sizes = {'fruits':fruits, 'sizes': size_nm}

df = pd.DataFrame.from_dict(fruit_sizes)

print(df)

import pandas as pd 

df = pd.DataFrame(fruit_sizes) 

print(df['fruits'])

print(df['size_nm'])

