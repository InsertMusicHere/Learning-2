# Learning-2
Using Python to clean Whatsapp chat data and then eventually creating data visualizations using Power BI

I have recently started learning coding, using Python language.

for this specific code, I used a walkthrough given on the website : https://resagratia.com/2020/01/visualizing-whatsapp-chats-using-python-and-power-bi/

The only part which I have copied as is, is a loop which uses regular expressions.

'''for line in clean_chat:
    if re.findall("\A\d+[/]", line):
        msgs.append(line)
        pos += 1'''

Rest of the code present in the 'whatapp.py' file is written by me.


In whatsapp.py I have added the code created using Python language.
Later in Power BI:
I have created some extra columns which helped me to eventually produce better graphs, Which are :::
Date.DayOfWeekName([Date])
Date.Day([Date])
Date.Month([Date])

If you think any changes are required or can be added please help me with it.
Thanks in advance!!
