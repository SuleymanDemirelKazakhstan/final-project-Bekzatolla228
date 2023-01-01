## Classify SDU's Instagrams chat

In this project, we tried to divide sdu chat messages into 9 classes. The program must give the message the class to which it belongs.

## Data

First.py - this file is needed to read the data and select all the text from there. Next, it removes emoticons, links, replies from the sdu and all the sticky signs.
C_01.csv - here are preserved all the text from the sdu chat that was cleared. This file is created with First.py.
Merged file.csv - Here are stored 600 texts that have been classified manually.
Untitled7.ipynb - with the help of this code we train our algorithm and determine which class the text belongs to.
