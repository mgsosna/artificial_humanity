########################################################################################################
# Carissa story
# Chapter 2a: life support, BENJAMIN dead
#
# Matt Grobis
########################################################################################################
# Where you could be coming from:
# - BENJAMIN dead, door locked

import pickle
from custom_functions import *
import random
import os

print()
player = pickle.load(open('player_stats.pkl', 'rb'))

print()
print("[*STORY*]")
print("Time is running out, indeed. You exit your quarters, absently fingering your laser knife as you walk. You are in")
print("a well-lit white hallway, and as you walk towards the life support systems, you pass a window peering out at the")
print("cosmos. Pluto looms large below you. You continue walking towards life support, which in this ship also doubles as")
print("a biological research station and infirmary. If you had a moral compass, the infirmary is where you would send")
print("crew members if they were feeling unwell, but unfortunately your moral compass looks more like a bloody knife, and")
print("you sure love using it. The door to the infirmary opens as you approach, and you enter a room full of fridge-sized")
print("machines, along with a small cramped desk with nothing but a microscope. VERONICA is sitting at the microscope but")
print("looks up as you enter. She is short, with cropped red hair and the standard brown uniform. If she's a human, her")
print("blood is probably red, too.")
input()    

# VERONICA talks to you
print("[VERONICA]")
print("Good morning, Commander.")
input()
print("[*STORY*]")
print("VERONICA seems stressed. Her smile is tight-lipped and you seem to be distracting her from something important.")
print("Her hand is clutching the table.")
input() 

# You respond
print(f"[{player['name']}]".upper())
print("A - [FRIENDSHIP] Good morning, VERONICA! How's your work going?")
print()
print("B - [ATTACK VERONICA]")
print()

# Decision
life_dec1 = ''
while life_dec1.upper() not in ['A', 'B']:
    life_dec1 = input("[CHOICE (A/B)]:    ")
    
# If attack, flip the boolean
if life_dec1.upper() == 'B':
    attack = True
    
#---------------------------------------------------------------------------------------------------------------------------------   
# Friendship
if life_dec1.upper() == 'A':
    print()
    print("[*STORY*]")
    print("A vein in VERONICA's neck bulges at your voice. She looks at you and slowly narrows her eyes.")
    input()
    print("[VERONICA]")
    print("Who *are* you? How... how could you kill BENJAMIN and then walk into this room like nothing happened? Are you")
    print("an idiot? Did you seriously think I wouldn't see his body??")
    input()
    
    # You respond
    print(f"[{player['name']}]".upper())
    print("A - It seemed like a good idea at the time.")
    print()
    print("B - BENJAMIN's an imposter and you probably are, too!")
    print()
    print("C - Hah... huhaha... hauahahaha HAHAUHAUAHAUHAA!!!!!!")
    print()
    
    # Decision
    life_dec1_1 = ''
    while life_dec1_1.upper() not in ['A', 'B', 'C']:
        life_dec1_1 = input("[CHOICE (A/B/C)]:    ")
 
    #---------------------------------------------------------------------------------------------------------------------------
    # B.A. Seemed like good idea
    if life_dec1_1.upper() == 'A':
        print()
        print("[*STORY*]")
        print("VERONICA scowls at you in disbelief.")
        input()
        print("[VERONICA]")
        print("You're crazy, you know that? A god damn maniac.")
        input()
        print(f"[{player['name']}]".upper())
        print("No, I'm actually the only one on the ship who's making sense... I'm trying to *save* all of us...")
        input()
        
        # Flip the boolean
        attack = True
      
    #---------------------------------------------------------------------------------------------------------------------------
    # B.B Benjamin's an imposter
    if life_dec1_1.upper() == 'B':
        print()
        print("[*STORY*]")
        print("VERONICA scowls at you in disbelief.")
        input()
        print("[VERONICA]")
        print("Imposter?? What the hell are you talking about? If you mean someone who's trying to sabotage the crew, you fit")
        print("the bill pretty well!")
        input()
        print(f"[{player['name']}]".upper())
        print("No, I'm actually the only one on the ship who's making sense... I'm trying to *save* all of us...")
        input()
    
        # Flip the boolean
        attack = True
        
    #----------------------------------------------------------------------------------------------------------------------------
    # B.C Maniacal laughter
    if life_dec1_1.upper() == 'C':
        print()
        print("[*STORY*]")
        print("Your laughter rises until it fills the room. You're shouting, screaming with laughter. Everything is so funny!")
        print("Life is meaningless! The only way to achieve meaning is to depart from sanity!!")
        input()
        print("[*STORY*]")
        print("When you finally calm down, you open your eyes to see VERONICA scowling at you.")
        input()
        print("[VERONICA]")
        print("You're crazy, you know that? A god damn maniac.")
        input()
        print(f"[{player['name']}]".upper())
        print("No, I'm actually the only one on the ship who's making sense... I'm trying to *save* all of us...")
        input()
        
        # Flip the boolean
        attack = True   
    
#---------------------------------------------------------------------------------------------------------------------------------
# Attack VERONICA
if attack == True:
    print()
    print("[*STORY*]")
    print("You stare at VERONICA, your hand on the knife in your pocket. Her eyes dart to your pocket and then back up to you.")
    input()
    print("[*STORY*]")
    print("You attack! You leap at VERONICA, pulling out the laser knife and swinging down at her. She rolls out of the way,")
    print("faster than you'd expected, and pulls out her own laser knife. Where did she...? Too late to think now. You swing")
    print("at her again but she blocks your arm and swiftly cuts across your ribs, tearing your uniform. Before you can react,")
    print("she's behind you and you feel a sudden sharp, burning feeling in your back. You look down and see the knife")
    print("protruding from your chest. You fall to your knees as the darkness rushes in, and your last thoughts are that you")
    print("didn't get to see the color of her blood...")
    input()
    print()
    print()
    print()   
    print()
    print("                                            [YOUR QUEST COMES TO AN END]")
    print("                                                     Ending #3")
    print()
    print("                                                      OUTCOMES:")
    print(f"                                                 - {player['name'].upper()} dies")
    print("                                                 - BENJAMIN dies")
    print("                                                 - VERONICA lives")
    print("                                                 - SHIP AI lives")
    print()
    print("                                                       CAUSE:")
    print("                                                 VERONICA kills you")
    
    # Update n_completions.pkl
    if 'n_completions.pkl' in os.listdir():
        n_completions = pickle.load(open('n_completions.pkl', 'rb'))              
        n_completions += 1
        
        save_object(n_completions, "n_completions.pkl")
        
    else:
        n_completions = 1
        save_object(n_completions, "n_completions.pkl")
            
    
    quit()

