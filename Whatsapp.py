echo "# Learning-2" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/InsertMusicHere/Learning-2.git
git push -u origin master

import pandas as pd
import numpy as np
import re
import dateparser
from collections import Counter
import matplotlib.pyplot as plt     #have not used this
import seaborn as sns
plt.style.use('ggplot')


Open_file = open("Downloaded_chat.txt",'r',encoding='utf-8') #make sure to keep this file in the right path
Read_file = Open_file.read()
content = Read_file.splitlines()
#print(content) #This step to check/debug your code, i have used print function for this purpose a lot of time in this code

#Deleting 'you were added/someone was removed/joined using group's link' lines
clean_chat = [line for line in content if not "You were added" in line]

#Focusing now on the contenet
msgs = [] #List created to store the content retrived from Read_file
position = 0 

for line in clean_chat:
    if re.findall("\A\d+[/]", line):
        msgs.append(line)
        position += 1
    else:
        take = msgs[pos-1] + ". " + line
        msgs.append(take)
        msgs.pop(position-1)
print(len(msgs))

#Creating lists to collect various information such as , Dates ,Time and chat content
date = []
for i in msgs:
    date.append(i.split(',')[0])
    
print(len(date))
#print(date)

time = []
for i in range(len(msgs)):
    time.append(msgs[i].split('-')[0][10:16])

print(len(time))
#print(time)

name = []
for i in range(len(msgs)):
    name.append(msgs[i].split(' ')[3][0:3])

#print(name)

content = []
for i in range(len(msgs)):
  try:
    content.append(msgs[i].split(':')[2])
  except IndexError:
    content.append('Missing')

#Using Panda's library    
df = pd.DataFrame(list(zip(date, time, name, content)),
                  columns = ['Date', 'Time', 'Name', 'Content'])

df = df[df["Content"]!='Missing']
df.reset_index(inplace=True, drop=True)

print(df.head()) #this step is done again to verify the data
df.to_csv("Select_the_filename.csv")

