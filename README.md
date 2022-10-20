# Monopoly Tracker 

A small python project that gives you a notification after a specified amount of spins has been spun without hitting "4-rolls" in the [Monopoly Casino Game](https://www.evolution.com/our-games/monopoly-live/)

It works by scraping the data from [Tracksino](https://tracksino.com/monopoly) every minute and checking the "4-roll Spin Since" number to give you a notification. Every time a 4-roll is hit, it will write it to the file "spins_to_get_rolls.txt". Some of the data currently in there is from having the program running over-night. Please note that this program is not maintained, and should tracksino undergo major changes, it is likely that it will no longer function.

Note that this project was done for educational purposes only, and is in no way recommended to use for gambling purposes. Just because it has been X amount of time since the last time Y event happened, it does not increase the chance of an event to be more likely to happen in the future. Thinking it does is refered to as [Gambler's Fallacy](https://www.investopedia.com/terms/g/gamblersfallacy.asp). Please be gambling aware.

# How to use

In main.py specify how many amount of spins you want to happen before recieving a notification in the "amount_of_spins_until_notification" variable.
Install the required packages:

`pip install -r requirements.txt` to install packages
`python main.py` to run main.py

# Author
[Thomas H](https://github.com/thom9346)
