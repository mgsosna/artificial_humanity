########################################################################################################
# ARTIFICIAL HUMANITY
# Chapter 2b: Engine Room, attempted to break carbon scrubber
#
# Matt Grobis
########################################################################################################
# Where you could be coming from:
# - Tried destroying the carbon scrubber but failed

import pickle
from custom_functions import *
import random
import os

player = pickle.load(open('player_stats.pkl', 'rb'))

# Initialize variables
attack = False

print()
print("[*STORY*]")
print("You stumble down hall. Ugh... head. Everything blurry... hallway get darker as you closer to engine room... dark")
print("is good. Oof. Door open automa-, ugh, uh... door open... as you in. BENJAMIN there. Or, at least... someone who")
print("look BENJAMIN. Mechanic clothes. Hair. BENJAMIN look up as you enter.")
input()

# BENJAMIN talks to you
print("[BENJAMIN]")
print("Commander! Uh, good to see you. Are...?")
input()
print("[*STORY*]")
print("Ringing in ears. Not sure what else he said.")
input()

# You respond
print(f"[{player['name']}]".upper())
print("A - How are you?")
print("B - Have you seen VERONICA? Don't trust anything she says.")
print("C - Attack BENJAMIN")
print()

# Choice
eng_dec1 = ""
while eng_dec1.upper() not in ['A', 'B', 'C']:
    eng_dec1 = input("[CHOICE (A/B/C)]:   ")

# If attack, change that boolean
if eng_dec1.upper() == 'C':
    attack = True
    
#------------------------------------------------------------------------------------------------------------------------------
# A. "How are you?"
if eng_dec1.upper() == 'A':
    print()
    print(f"[{player['name']}]".upper())
    print("Hubhyou? Ffff. Ugnh.")
    input()
    print("[*STORY*]")
    print("It hurt to lift head, but you look up to look BENJAMIN. He so blurry. Focus on his face. He say something. He")
    print("look... suspicious? Like he sad? Don't be sad, BENJAMIN. We need... find... imposter.")
    input()
    print(f"[{player['name']}]".upper())
    print("Gttahlpme. Fn...fsfsss....")
    input()
    print(f"[{player['name']}]".upper())
    print("...")
    input()
    print(f"[{player['name']}]".upper())
    print("Imp... impuhster...")
    input()
    
#-----------------------------------------------------------------------------------------------------------------------------
# B. "Don't trust VERONICA"
if eng_dec1.upper() == 'B':
    print()
    print(f"[{player['name']}]".upper())
    print("Dnttrst VRNCUH! She's... ughhh...")
    input()
    print(f"[{player['name']}]".upper())
    print("...")
    input()
    print(f"[{player['name']}]".upper())
    print("She's... lying...")
    input()
    print("[*STORY*]")
    print("It hurt to lift head, but you look up to look BENJAMIN. He so blurry. Focus on his face. He say something. He")
    print("look... suspicious? Like he sad? Don't be sad, BENJAMIN. We need... stop... VERONICA.")
    input() 
    
#------------------------------------------------------------------------------------------------------------------------
# All paths (except attacking) end this way
if attack == False:
    print("[VERONICA]")
    print("I think we know perfectly well what needs to be done.")
    input()
    print("[*STORY*]")
    print("Uh oh. Lift head, see VERONICA next to BENJAMIN. That... not good.")
    input()
    print("[VERONICA]")
    print(f"BENJAMIN, I believe {player['name']} is not capable of appropriately governing this ship. Do you agree?")
    input()
    print("[BENJAMIN]")    
    print("I agree.")
    input()
    print("[VERONICA]")
    print("I am therefore assuming control of this ship. The first order of business is to exterminate the threat to")
    print("this ship. Do you agree?")
    input()
    print("[BENJAMIN]")
    print("I agree, Captain.")
    input()
    print(f"[{player['name']}]".upper())
    print("No... bad 'dea.")
    input()
    print("[VERONICA]")
    print(f"Oh, {player['name']}, you're not a member of the crew anymore. In fact, you're the threat that needs to be")
    print("eradicated. BENJAMIN, if I may have your help?")
    input()
    print("[*STORY*]")
    print("Everything too blurry for you to see what about to happen, but you see BENJAMIN hold something shining in")
    print("hand. Feel heat from here... heat get closer.")
    input()
    
    # How you go
    print(f"[{player['name']}]".upper())
    print("A - Accept fate")
    print("B - You not taking me alive!")
    print()
    
    # Choice
    eng_dec1_3 = ""
    while eng_dec1_3.upper() not in ['A', 'B']:
        eng_dec1_3 = input("[CHOICE (A/B)]:   ")

    # Accept fate
    if eng_dec1_3.upper() == 'A':
        print()
        print("[*STORY*]")
        print("You close eyes and pray. You can't remember if religious or not. Pray to... who? To space. Suddenly, you feel")
        print("stab of hot pain! You fall, and hot pain stabs again and again as you fade away. You hope space heard your")
        print("prayers.")
        input()
    
    # Go out swinging
    if eng_dec1_3.upper() == 'B':
        print()
        print("[*STORY*]")
        print("No way they take you! You pull out laser knife and throw self at BENJAMIN. Heat of laser knife in hand almost")
        print("as hot as heat from them... your eyes closed as you slash and slash! After few moments, you realize everything")
        print("quiet... you open eyes.")
        input()
        print("[VERONICA]")
        print(f"Keep the eyes open next time, {player['name']}. Maybe it'll work out for you in Hell.")
        input()
        print("[*STORY*]")
        print("With big swing, bright light cut across your vision as BENJAMIN strikes you with own laser knife. You fall and")
        print("see VERONICA standing few feet away. Imposter! Imposter! Imposter... vision fades to dark.")
        input()
        
    # Either way, you get this ending
    input(".")
    input(".")
    input(".")   
    print()
    print("                                            [YOUR QUEST COMES TO AN END]")
    print("                                                     Ending #2")
    print()
    print("                                                      OUTCOMES:")
    print(f"                                                 - {player['name'].upper()} dies")
    print("                                                 - BENJAMIN lives")
    print("                                                 - VERONICA lives")
    print("                                                 - SHIP AI lives")
    print()
    print("                                                       CAUSE:")
    print("                                             BENJAMIN and VERONICA mutiny")
    
    # Update n_completions.pkl
    if 'n_completions.pkl' in os.listdir():
        n_completions = pickle.load(open('n_completions.pkl', 'rb'))              
        n_completions += 1
        
        save_object(n_completions, "n_completions.pkl")
        
    else:
        n_completions = 1
        save_object(n_completions, "n_completions.pkl")
                
    quit()
    
#----------------------------------------------------------------------------------------------------------------------------
# If you decide to attack
if attack == True:
    print()
    print("[*STORY*]")
    print("No more games! You grab laser knife and launch at BENJAMIN... he gasp, but he move so fast and step aside from")
    print("your knife. Why... so fast? Or you slow? You attack again! Swing with knife.")
    input()
    print("[VERONICA]")
    print("That's quite enough.")
    input()
    print("[*STORY*]")
    print("Uh oh. Lift head, see VERONICA next to BENJAMIN. He pulls out own laser knife. That... not good.")
    input()
    
    # How you go
    print(f"[{player['name']}]".upper())
    print("A - Haha, what a funny joke, right?")
    print("B - VERONICA's the imposter!")
    
    # Choice
    eng_dec1_2 = ""
    while eng_dec1_2.upper() not in ['A', 'B']:
        eng_dec1_2 = input("[CHOICE (A/B)]:   ")
    
    # A. Funny joke
    if eng_dec1_2.upper() == 'A':
        print()
        print(f"[{player['name']}]".upper())
        print("Yugys... jok! Jstjoke... ugh. I.. not... ugh... notrly trykll BNJMN... hah...")
        input()
    
    # B. VERONICA's the imposter!
    if eng_dec1_2.upper() == 'B':
        print()
        print(f"[{player['name']}]".upper())
        print("BEN! Dnttrst... VRNCA... she evil! Ugh.. she... don't.. notrsther...")
        input()
    
    # Either way, get the mutiny  
    print("[VERONICA]")
    print(f"BENJAMIN, I believe {player['name']} is not capable of appropriately governing this ship. Do you agree?")
    input()
    print("[BENJAMIN]")    
    print("I agree.")
    input()
    print("[VERONICA]")
    print("I am therefore assuming control of this ship. The first order of business is to exterminate the threat to")
    print("this ship. Do you agree?")
    input()
    print("[BENJAMIN]")
    print("I agree, Captain.")
    input()
    print(f"[{player['name']}]".upper())
    print("No... bad 'dea.")
    input()
    print("[VERONICA]")
    print(f"Oh, {player['name']}, you're not a member of the crew anymore. In fact, you're the threat that needs to")
    print("be eradicated. BENJAMIN, if I may have your help? {player['name']}, drop your weapon.")
    input()
    print("[*STORY*]")
    print("Everything too blurry for you to see what about to happen, but you see BENJAMIN hold something shining in")
    print("hand. Feel heat from here... heat get closer.")
    input()
    
    # How you go
    print(f"[{player['name']}]".upper())
    print("A - Accept fate")
    print("B - You not taking me alive!")
    
    # Choice
    eng_dec1_3 = ""
    while eng_dec1_3.upper() not in ['A', 'B']:
        eng_dec1_3 = input("[CHOICE (A/B)]:   ")
    
    # Accept fate
    if eng_dec1_3.upper() == 'A':
        print()
        print("[*STORY*]")
        print("You close eyes and pray, still holding knife. You can't remember if religious or not. Pray to... who? To space.")
        print("Suddenly, you feel stab of hot pain! You fall, and hot pain stabs again and again as you fade away. You hope")
        print("space heard your prayers.")
        input()
    
    # Go out swinging
    if eng_dec1_3.upper() == 'B':
        print()
        print("[*STORY*]")
        print("No way they take you! You throw self at BENJAMIN again! Close eyes as you slash, slash, kill! After few moments,")
        print("you realize everything quiet... you open eyes.")
        input()
        print("[VERONICA]")
        print(f"Keep the eyes open next time, {player['name']}. Maybe it'll work out for you in Hell.")
        input()
        print("[*STORY*]")
        print("With big swing, bright light cut across your vision as BENJAMIN strikes you with own laser knife. You fall and")
        print("see VERONICA standing few feet away. Imposter! Imposter! Imposter... vision fades to dark.")
        input()
        
    # Either way, you get this ending
    input(".")
    input(".")
    input(".")   
    print()
    print("                                            [YOUR QUEST COMES TO AN END]")
    print("                                                     Ending #2")
    print()
    print("                                                      OUTCOMES:")
    print(f"                                                 - {player['name'].upper()} dies")
    print("                                                 - BENJAMIN lives")
    print("                                                 - VERONICA lives")
    print("                                                 - SHIP AI lives")
    print()
    print("                                                       CAUSE:")
    print("                                             BENJAMIN and VERONICA mutiny")
    
    # Update n_completions.pkl
    if 'n_completions.pkl' in os.listdir():
        n_completions = pickle.load(open('n_completions.pkl', 'rb'))              
        n_completions += 1
        
        save_object(n_completions, "n_completions.pkl")
        
    else:
        n_completions = 1
        save_object(n_completions, "n_completions.pkl")
            
    quit()
    
