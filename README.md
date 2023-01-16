---
description: >-
  The aim of the project was to create a bot which writes up Birthday Wishes to
  my contacts on Whatsapp.
---

# Whatsapp-Birthday-Bot

1. I compiled the list of my contacts and their birthdays into a csv file
2. Using Selenium and Whatsapp Web, I would then search the contact and send them birthday wishes accordingly
3. I then used to run the python code daily on my laptop automatically before shutdown, and it would do the needful if someone's Birthday was on that day.



Overall the project was a success and the code worked very well.

Later, I realised that I didn't really wanna do this so I have shut it down for now, and removed any sensitive data from the project, altho the code is still there for anyone to use.



#### How to Use this Code

**main.py** : simply calls the various functions I have created in various files in the project

**webdriver.py** : runs the function of the bot to open Whatsapp Web and search for the contact whose message it is.

**messages.py** : selects a birthday wish randomly from a group of wishes&#x20;

**database.py :** Initializes the dataframe with the given characteristics. Retreives and fills back data in after sending the message. Updates the already sent values in the dataframe, so that the same user doesn't get the same messages



\------------------------------------------------------------------------------------------
