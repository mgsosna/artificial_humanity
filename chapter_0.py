########################################################################################################
# ARTIFICIAL HUMANITY
# Chapter 0: introduction
#
# Matt Grobis
########################################################################################################
# Load modules
import pickle
import numpy as np
import time
from custom_functions import *

# Create empty character dictionary
player = {}
player['chapter'] = 0
player['ch_1'] = dict()
player['ch_2'] = dict()
player['ch_3'] = dict()

#-----------------------------------------------------------------------------------------
# Scrolling binary with transition to text

scrolling_binary(screen_size=37, n_rows=12, n_spaces=10, time_sleep=0.5)

for step in range(len("Hello.")):

    binary = np.random.randint(2, size = (73 - (step*2) + 1))
    str_binary = " " * 10 + str(binary)[1:len(binary)] + " "
    str_binary = str_binary + "H e l l o."[0:(step*2)]
    print('\r' + str_binary, end = '')

    time.sleep(0.5)

#------------------------------------------------------------------------------------------
print("\n" * 1)

time.sleep(1)

print("Hello. Can you hear me?")

time.sleep(1)

print("\n" + "Commander.")

time.sleep(3)

print("\n" + "Commander, can you hear me?")

time.sleep(2)

#-----------------------------------------------------------------------------------
player['name'] = ""

# Record player name, and avoid them accidentally clicking through this part
while len(player['name']) == 0:
    player['name'] = input("\n" + "[What is your name?].......").capitalize()

time.sleep(1)

print("\n" + "Commander {}, there has been a breach.".format(player['name']))
print()
time.sleep(2)

<<<<<<< HEAD
############################################################################################
=======
##########################################################################################
>>>>>>> efc8a6793302600840d5d91d5983cb84dc65a4fb
# Scrolling binary, slower

scrolling_binary(screen_size=37, n_rows=5, n_spaces=10, time_sleep=1)

time.sleep(1)

print("\n"*2 + " " * 35, "ARTIFICIAL HUMANITY" + "\n"*2)

time.sleep(2)

scrolling_binary(screen_size=37, n_rows=10, n_spaces=10, time_sleep=1)


# Chapter complete
player['chapter'] = 1

save_object(player, "player_stats.pkl")

# Start the fun
import chapter_1
