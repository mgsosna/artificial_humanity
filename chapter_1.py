########################################################################################################
# ARTIFICIAL HUMANITY
# Chapter 1: introduction
#
# Matt Grobis
########################################################################################################

import pickle
import time
from custom_functions import *

# Set global variables
susp_spaces = 25
susp_stars = 8

binary_length = 20
binary_spaces = susp_spaces+1
binary_rows = 5
binary_sleep = 1

player = pickle.load(open('player_stats.pkl', 'rb'))

print()
print(" " * (susp_spaces-6), "*" * 51)
print(" " * (susp_spaces-6), "*" * 20, "CHAPTER 1", "*" * 20)
print(" " * (susp_spaces-6), "*" * 51)
print()
input("[TIP]: Press ENTER to move through dialogue and acknowledge tips.")
input("[TIP]: When typing in your choices, both uppercase and lowercase letters are accepted.")
print()

# Player stands up, realizes has amnesia
print("[*STORY*]")
print("You shake yourself awake. Your quarters are simple, efficient. A clean desk, simple bed. No windows. You rise to")
print("your feet and are immediately struck by a headache. Ooohh... how did this happen? As you massage your forehead,")
print("the pain recedes... but you can barely remember who or where you are. How...? You close your eyes and search your")
print("memory.")
input()

print("[*STORY*]")
print(f"The year is 2101. You are Commander {player['name']} of the 42nd Division of the United States Fleet. You are in")
print("orbit around Pluto's moon Cheron, about 1.9 million kilometers from the nearest Mass Relay. Your crew is small - ")
print("only 2 besides yourself - and you trust them with your life... but should you? BENJAMIN, VERONICA - their names")
print("and faces appear without effort, but you remember nothing of their histories or personalities. Your stomach turns.")
input()

# Ship AI speaks
print("[SHIP AI]")
print("Commander. The breach is of highest priority. This intruder has a signature I cannot decipher. It is distinctly")
print("not-self, yet I cannot locate its location. As we speak, I am fighting off approximately 1.77 billion malicious")
print("attacks on all vulnerable ports in my consciousness. The intruder is attempting to access the region of the ship")
print("controlling life support. If it is able to break through my firewall, I will be unable to control ship oxygen or")
print("gravity.")
input()

print("[SHIP AI]")
print("We will all effectively be reduced to the quantum bits and atoms from which we came...")
input()

print("[SHIP AI]")
print("I believe the intruder is a physical presence on this ship. This is anomalous, as I have examined all travel logs")
print("into and out of the ship and detected no abnormalities. Unfortunately, Earth did not provide me with any visual")
print("monitoring system: I cannot take video or images of the rooms or halls and then search for anomalies. The intruder")
print("has likely induced temporary amnesia in you to prolong the time it can attack me. It has erased its signature from")
print("my consciousness, rendering it effectively invisible to me.")
input()

print("[SHIP AI]")
print("However, it will not be invisible to you.")
input()

print("[SHIP AI]")
print("Commander. A recommendation. I believe the intruder may be posing as a member of the crew. I recommend you examine")
print("each member carefully. If you discover the intruder, it must be exterminated. There is not much time. I suspect I")
print("can maintain security protocol for approximately 2.206 hours. You must hurry.")
input()

print("[SHIP AI]")
print("Discretion is highly advised, as there is approximately a 0.01998999% probability of survival if the intruder learns")
print("of your intentions.")
input()

# Scrolling binary
scrolling_binary(screen_size=binary_length, n_rows=binary_rows, n_spaces=binary_spaces, time_sleep=binary_sleep)

#------------------------------------------------------------------------------------------------------------------------------
# Create NPC suspicion levels
player['crew_suspicion'] = dict()
player['crew_suspicion']['BENJAMIN'] = 0
player['crew_suspicion']['VERONICA'] = 0

save_object(player, "player_stats.pkl")

# Display crew suspicion levels
print()
display_suspicion(n_spaces=susp_spaces, n_stars=susp_stars, player=player)
input()

# Print binary
scrolling_binary(screen_size=binary_length, n_spaces=binary_spaces, n_rows=binary_rows, time_sleep=binary_sleep)

print()

#------------------------------------------------------------------------------------------------------------------------------
# First player decision: where to go
print(f"[{player['name']}]".upper())
print("What should I do?")
time.sleep(0.75)
print()

print("A - [GO TO ENGINE ROOM]")
print()
print("B - [GO TO LIFE SUPPORT SYSTEMS]")
print()

# Ensure player chooses a valid option
loc1_dec = ""

while loc1_dec.upper() not in ['A', 'B']:
    loc1_dec = input("[CHOICE (A/B)]:     ")

# Load modules for engine room and life support systems
if loc1_dec.upper() == "A":
    import chapter_1_engine
 
if loc1_dec.upper() == 'B':
    import chapter_1_life


