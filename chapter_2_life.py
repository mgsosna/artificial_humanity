########################################################################################################
# ARTIFICIAL HUMANITY
# Chapter 2a: life support systems
#
# Matt Grobis
########################################################################################################
# Where you could be coming from:
# - Got no info from BENJAMIN
# - You know he has a headache
# - You know he has a headache + memory loss
# - You know he has a headache + memory loss + suspects the Ship AI
# - You killed BENJAMIN and locked the door
# - You killed BENJAMIN and hid the body

import pickle
from custom_functions import *
import random
import os

# Initialize booleans
intimidate = False
attack = False

print()
player = pickle.load(open('player_stats.pkl', 'rb'))

print()
print("[*STORY*]")
print("Time is running out, indeed. You exit your quarters, absently fingering your laser knife as you walk. You are in a well-")
print("lit white hallway, and as you walk towards the life support systems, you pass a window peering out at the cosmos. Pluto")
print("looms large below you. You continue walking towards life support, which in this ship also doubles as an infirmary and")
print("biological research station. The ship's designers apparently figured that anything vaguely life-related should be put in")
print("the same room. The door opens automatically as you approach and you enter a room full of fridge-sized machines, along with")
print("a small cramped desk with nothing but a microscope. VERONICA is sitting at the microscope but looks up as you enter. She is")
print("short, with cropped red hair and the standard brown uniform.")
input()      

# VERONICA talks to you
print("[VERONICA]")
print("Good morning, Commander.")
input()
print("[*STORY*]")
print("VERONICA seems stressed. Her smile is tight-lipped and you seem to be distracting her from something important.")
input()

# You respond
print(f"[{player['name']}]".upper())
print("A - [FRIENDSHIP] Good morning, VERONICA! How's your work going?")
print()
print("B - [INTIMIDATION] Why are you so stressed? Are you hiding something?")
print("    o Success [50%]: VERONICA opens up.")
print("    o Failure [50%]: VERONICA grows defensive.")
print()
print("C - [ATTACK VERONICA]")
print()

# Decision
life_dec1 = ''
while life_dec1.upper() not in ['A', 'B', 'C']:
    life_dec1 = input("[CHOICE (A/B/C)]:    ")
    
# If intimidate or attack, flip the boolean
if life_dec1.upper() == 'B':
    intimidate = True

if life_dec1.upper() == 'C':
    attack = True

#----------------------------------------------------------------------------------------------------------------------
# A. Friendship
if life_dec1.upper() == "A":
    print()
    print("[*STORY*]")
    print("VERONICA's smile becomes a little more genuine, but she's still clearly stressed.")
    input()
    print("[VERONICA]")
    print("Work is going well, Commander. It's going as well as it always does.")
    input()
    print("[*STORY*]")
    print("VERONICA is quiet for a few moments and you realize she's done talking.")
    input()
    
    # Response
    print(f"[{player['name']}]".upper())
    print("A - [FRIENDSHIP] That's good to hear! What are your latest findings?")
    print()
    print("B - [INTIMIDATION] Why are you so stressed? Are you hiding something?")
    print("    o Success [50%]: VERONICA opens up.")
    print("    o Failure [50%]: VERONICA grows defensive.")
    
    # Decision
    life_dec1_1 = ''
    while life_dec1_1.upper() not in ['A', 'B']:
        life_dec1_1 = input("[CHOICE (A/B)]:    ")
        
    # If intimidate, go to "uninformative intimidate"
    if life_dec1_1.upper() == 'B':
        intimidate = True

    #-------------------------------------------------------------------------------------------------------------------
    # A.A Friendship - friendship
    if life_dec1_1.upper() == 'A':
        print()
        print("[*STORY*]")
        print("VERONICA smiles slightly, despite herself. She leans back in her chair and thinks for a few moments, choosing her")
        print("words carefully.")
        input()
        print("[VERONICA]")
        print("As the crew's lead biologist - and only biologist, actually - I decided it would be worthwhile to look into the")
        print("effects of space exposure on mental acuity. I understand it's not my exact research, Commander, but I think it")
        print("could prove useful.")
        input()
        
        # Response
        print(f"[{player['name']}]".upper())
        print("A - [FRIENDSHIP] Oh, interesting! So what'd you find?")
        print()
        print("B - [INTIMIDATION] Wait, are YOU the reason I can't remember anything?")
        print("    o Success [75%]: VERONICA opens up.")
        print("    o Failure [25%]: VERONICA grows suspicious.")
        print()
        print("C - [ATTACK VERONICA]")
        print()
        
        # Decision
        life_dec1_2 = ''
        while life_dec1_2.upper() not in ['A', 'B', 'C']:
            life_dec1_2 = input("[CHOICE (A/B/C)]:    ")
            
        # If attack, change the boolean
        if life_dec1_2.upper() == 'C':
            attack = True
    
        #--------------------------------------------------------------------------------------------------------------
        # A.A.A Friendship again
        if life_dec1_2.upper() == 'A':
            print()
            print("[VERONICA]")
            print("I'm glad to hear of your interest, commander. I haven't found much yet. I'm just getting started, really...")
            input()
            
            # Response
            print(f"[{player['name']}]".upper())
            print("A - [FRIENDSHIP] You're just being modest. Let's hear it.")
            print()
            print("B - [INTIMIDATION] Why are you hiding things? Stop lying to me.")
            print()
            
            # Decision
            life_dec1_3 = ''
            while life_dec1_3.upper() not in ['A', 'B']:
                life_dec1_3 = input("[CHOICE (A/B)]:    ")
        
            #-----------------------------------------------------------------------------------------------------------------
            # A.A.A.A. Friendship
            if life_dec1_3.upper() == 'A':
                print()
                print("[*STORY*]")
                print("VERONICA pauses for a few moments. She seems to be weighing something in her mind.")
                input()
                print("[VERONICA]")
                print("I'm trying to learn more about memory loss. I believe it might be a concern for the crew. I don't necessarily")
                print("believe it's an immediate concern, but it could be something worthwhile to look into. Sometimes I find that")
                print("I'm forgetful... today might be one of those days. But if you'll excuse me, Commander, I think I should get")
                print("back to work. I have such a headache and I'll need to finish this before I can rest.")
                input()
                
                # End chapter (based on what happened in chapter one)                      
                if player['ch_1']['outcome'] in ['kill_hide', 'kill_lock']:
                    print("[*STORY*]")
                    print("Headache? That sounds like what you were feeling this morning... and still continue to feel. Your hand")
                    print("itches for the knife in your pocket but you hold back. You make some idle chat with VERONICA for a minute")
                    print("before dismissing her and beginning the walk back to your quarters. Having a hazy memory sure sounds like")
                    print("something an imposter would say, but SHIP may have more insights...")
                    input()
                
                if player['ch_1']['outcome'] == 'failure':
                    print("[*STORY*]")
                    print("A headache? That sounds a bit like what you were feeling this morning... and still continue to feel. You make some")
                    print("idle chat with VERONICA for a minute before dismissing her and slowly beginning the walk back to your quarters. A")
                    print("headache sounds like an excuse just to quickly end the conversation, just how BENJAMIN didn't want to talk to you.")
                    print("Though maybe that's because you're so awkward. Did VERONICA not want to talk to you because you're awkward?...")
                    print("you because you're awkward?...")
                    input()
                
                if player['ch_1']['outcome'] == 'minor_reveal':
                    print("[*STORY*]")
                    print("A headache?? That sounds like what you were feeling this morning... and still continue to feel. BENJAMIN mentioned")
                    print("that he had a headache, too. Your heart drops. Somehow, all crew members awoke with a headache this morning... you")
                    print("consider telling VERONICA about BENJAMIN but you decide to keep quiet. You dismiss VERONICA and slowly begin walking")
                    print("back to your quarters, a knot in your stomach.")
                    input()
                    
                if player['ch_1']['outcome'] == 'major_reveal':
                    print("[*STORY*]")
                    print("A headache?? That sounds uncomfortably like what you were feeling this morning... and still continue to feel. BENJAMIN")
                    print("mentioned that he had a headache, too. Your heart drops. Somehow, all crew members awoke with a headache this morning...")
                    print("and at least you and BENJAMIN also have memory loss. Suddenly, you feel a lot less safe than you felt before. You")
                    print("absently dismiss VERONICA and slowly start walking back to your quarters. This is going to require some thinking...")
                    input()
                    
                if player['ch_1']['outcome'] == 'full_reveal':
                    print("[*STORY*]")
                    print("A headache?? That sounds uncomfortably like what you were feeling this morning... and still continue to feel. BENJAMIN")
                    print("mentioned that he had a headache, too. Your heart drops. Somehow, all crew members awoke with a headache this morning...")
                    print("and at least you and BENJAMIN also have memory loss. Suddenly, you feel a lot less safe than you felt before. Your")
                    print("thoughts dart back to BENJAMIN and what he said about trusting the Ship. Could the Ship somehow be related to the fact")
                    print("that everyone had memory loss?? You absently dismiss VERONICA and slowly begin walking back to your quarters. This is")
                    print("going to require some thinking... if you can stop your hands from shaking first.")
                    input()
                    
                # Update storyline
                player['ch_2'] = {'room': 'life',
                                  'outcome': 'minor_reveal'}
                player['chapter'] = 3
                save_object(player, "player_stats.pkl")
    
            #-----------------------------------------------------------------------------------------------------------------
            # A.A.A.B Intimidation (stop lying to me)
            if life_dec1_3.upper() == 'B':
                print()
                print("[*STORY*]")
                print("VERONICA's smile falters. Maybe that was a bad idea.")
                input()
                print("[VERONICA]")
                print("Commander, I'm certainly not hiding things or lying to you. I don't appreciate the accusation. If you'll excuse me, I")
                print("need to get back to work. Thank you.")
                input()
                            
                # Update suspicion
                player['crew_suspicion']['VERONICA'] += 1
                print("* " * 5, "VERONICA suspicion increases by 1.", " *" * 5)
                input()
                                    
                # End chapter
                print("[*STORY*]")
                print("No luck. You want to press VERONICA further, but the conversation is clearly over. You regret losing your temper.")
                print("You can't tell if VERONICA was actually offended, or was trying to preemptively end the conversation. You watch her")
                print("for a few moments, trying to imagine what an imposter would act like, but it's fruitless. You dismiss her and begin")
                print("walking back to your quarters, lost in thought.")
                input()
                
                # Update storyline
                player['ch_2'] = {'room': 'life',
                                  'outcome': 'failure'}
                player['chapter'] = 3
                save_object(player, "player_stats.pkl")

        #-------------------------------------------------------------------------------------------------------------------------
        # A.A.B Intimidation ("you're the reason I can't remember anything")
        if life_dec1_2.upper() == 'B':
            
            # Random draw
            intimidate_outcome = random.sample(range(100), 1)
            
            #---------------------------------------------------------------------------------------------------------------
            # A.A.B1 Intimidate success
            if intimidate_outcome < [75]:
                print()
                print("[SUCCESS]")
                print("VERONICA is shocked. She stares at you, her mouth open. After what feels like a minute, she finally speaks.")
                input()
                print("[VERONICA]")
                print("Did you just say you can't remember anything?")
                input()
                print(f"[{player['name']}]".upper())
                print("Yes.")
                input()
                print("[*STORY*]")
                print("VERONICA slowly shakes her head, her eyes wide. She glances at the microscope and then the pile of articles")
                print("next to her. The top one has a paragraph that's been highlighted yellow. VERONICA thinks for a few moments")
                print("and then begins to speak, her voice a whisper.")
                input()
                print("[VERONICA]")
                print("I think you and I may be experiencing the effects of a nerve gas that causes temporary amnesia. Its strongest")
                print("effect is persistent headaches.")
                input()
                
                # Think about how you killed BENJAMIN
                if player['ch_1']['outcome'] in ['kill_hide', 'kill_lock']:
                    print("[*STORY*]")
                    print("You wonder if BENJAMIN also had a headache or amnesia in the moments before you stabbed him repeatedly. Just")
                    print("the thought of violence makes you smile, and you have to hold back a big laugh. After a moment you settle your")
                    print("racing heart, lick your lips, and turn back to VERONICA.")
                    input()
                    print(f"[{player['name']}]".upper())
                    print("Do you know how to cure the amnesia?")
                    input()
                                
                # Respond: "hm, interesting"
                if player['ch_1']['outcome'] == 'failure':
                    print("[*STORY*]")
                    print("You wonder if BENJAMIN also has a headache or amnesia, but you learned nothing when you talked to him. Either")
                    print("he has something to hide or you're *really* hit-or-miss when it comes to getting information from your crew.")
                    input()
                    print(f"[{player['name']}]".upper())
                    print("Do you know how to cure the amnesia?")
                    input()
                              
                # Respond: "Benjamin had a headache!" 
                if player['ch_1']['outcome'] == 'minor_reveal':
                    print(f"[{player['name']}]".upper())
                    print("BENJAMIN has a headache, too.")
                    input()
                    print("[*STORY*]")
                    print("VERONICA is silent for a few moments. She looks at her microscope again and slowly shakes her head.")
                    input()
                    print("[VERONICA]")
                    print("I know; I talked with him twenty minutes ago.")
                    input()
                    print("[*STORY*]")
                    print("You wait for VERONICA to say more but she's silent. You wonder if BENJAMIN can't remember anything, either...")
                    print("that would explain some things. You'll have to think about it later.")
                    input()
                    print(f"[{player['name']}]".upper())
                    print("Do you know how to cure the amnesia?")
                    input()
                    
                # Respond: "Benjamin had a headache and amnesia, too!"
                if player['ch_1']['outcome'] in ['major_reveal', 'full_reveal']:
                    print(f"[{player['name']}]".upper())
                    print("BENJAMIN has a headache and memory loss, too.")
                    input()
                    print("[*STORY*]")
                    print("VERONICA is silent for a few moments. She looks at her microscope again and slowly shakes her head.")
                    input()
                    print("[VERONICA]")
                    print("I know; I talked with him twenty minutes ago. It would have been strange for only part of the crew to have")
                    print("headaches and memory loss.")
                    input()
                    
                    if player['ch_1']['outcome'] == 'major_reveal':
                        print("[*STORY*]")
                        print("You feel a knot in your stomach. Everyone in the crew has headaches and amnesia. Either there's someone else on")
                        print("board, SHIP is wrong, or VERONICA and BENJAMIN are lying to you... but the last option surprisingly seems the")
                        print("least likely.")
                        input()              
                        print(f"[{player['name']}]".upper())
                        print("Do you know how to cure the amnesia?")
                        input()
                     
                    if player['ch_1']['outcome'] == 'full_reveal':
                        print("[*STORY*]")
                        print("You feel a knot in your stomach. Everyone in the crew has headaches and amnesia. Either there's someone else on")
                        print("board, SHIP is wrong, or VERONICA and BENJAMIN are lying to you... but the last option surprisingly seems the")
                        print("least likely. You think back to what BENJAMIN said about how he doesn't trust the ship, and suddenly you start")
                        print("sharing his suspicions.")
                        input()              
                        print(f"[{player['name']}]".upper())
                        print("BENJAMIN... suspects SHIP. He thinks we shouldn't trust the AI. I think I agree.")
                        input()
                        print("[*STORY*]")
                        print("VERONICA stares at you for a few seconds. Clearly BENJAMIN didn't tell that to her. You stare back at her,")
                        print("thinking the same thing. Finally, she speaks.")
                        input()
                        print("[VERONICA]")
                        print("How are we going to get home if we can't trust SHIP? God damn it...")
                        input()
                        print(f"[{player['name']}]".upper())
                        print("First things first. Do you have any way to fight this amnesia?")
                        input()
                        print("[VERONICA]")
                        print("I do. I've been researching a way to reverse the effects of the toxin, and I suspect I'm close to finishing. I")
                        print("need probably two more hours.")
                        input()
                        print("[*STORY*]")
                        print("SHIP said there's only about an hour left until it can't hold off the malicious attack... but could that really")
                        print("be true? What if there actually wasn't an attack happening right now?")
                        input()
                        print(f"[{player['name']}]".upper())
                        print("Work as fast as you can, VERONICA. I'll work on SHIP. Be careful... anything could happen in the next hour.")
                        input()
                            
                        # Update storyline
                        player['ch_2'] = {'room': 'life',
                                          'outcome': 'full_reveal'}
                        player['chapter'] = 3
                        save_object(player, "player_stats.pkl")
                            
                #---------------------------------------------------------------------------------------------------------------------
                # All other storylines converge
                if player['ch_1']['outcome'] != 'full_reveal':                   
                    print("[VERONICA]")
                    print("I do. I've been researching a way to reverse the effects of the toxin, and I suspect I'm close to finishing. I")
                    print("need probably two more hours.")
                    input()
                    print("[*STORY*]")
                    print("SHIP said there's only about an hour left until it can't hold off the malicious attack... your memory is useless")
                    print("but you doubt SHIP's often been wrong on complex calculations. If SHIP were to fail and a malicious actor gained")
                    print("control... you doubt any of the crew would survive for very long. Or something more sinister would happen... for")
                    print("now, we just need to keep moving.")
                    input()
                    print(f"[{player['name']}]".upper())
                    print("Work as fast as you can, VERONICA. The sooner our memories return, the better.")
                    input()
    
                    # Update storyline
                    player['ch_2'] = {'room': 'life',
                                      'outcome': 'full_reveal'}
                    player['chapter'] = 3
                    save_object(player, "player_stats.pkl")
            
            #----------------------------------------------------------------------------------------------------------------
            # A.A.B2 Intimidate failure ('you're the reason I can't remember anything')
            if intimidate_outcome >= [75]:
                print()
                print("[FAILURE]")
                print("VERONICA's smile falters. She stares at you for a few moments, unsure of what to say.")
                input()
                print("[VERONICA]")
                print("Commander... I don't know where to begin. First, I don't appreciate the accusation.")
                input()
                
                # Response
                print(f"[{player['name']}]".upper())
                print("A - I can accuse whoever I want!")
                print()
                print("B - Sorry. I lost my temper.")
                print()
                print("C - [ATTACK VERONICA]")
                print()
                
                # Decision
                life_dec1_3 = ''
                while life_dec1_3.upper() not in ['A', 'B']:
                    life_dec1_3 = input("[CHOICE (A/B)]:    ")
                    
                # If attack, flip the boolean
                if life_dec1_3.upper() == 'C':
                    attack = True
                
                #-----------------------------------------------------------------------------------------------------------
                # A.A.B2.A Don't back down
                if life_dec1_3.upper() == 'A':
                    print()
                    print("[*STORY*]")
                    print("VERONICA's eyes narrow. She turns from you and gets back to work.")
                    input()
                    print("[VERONICA]")
                    print("If you're having difficulty remembering things, I suggest a nap. Now please excuse me; I'm very busy.")
                    input()
                
                    # Update suspicion
                    player['crew_suspicion']['VERONICA'] += 1
                    print("* " * 5, "VERONICA suspicion increases by 1.", " *" * 5)
                    input()
                                    
                    # End chapter
                    print("[*STORY*]")
                    print("No luck. You want to press VERONICA further, but the conversation is clearly over. You regret losing your")
                    print("temper and revealing so much... what were you thinking? You can't remember... which just makes you even")
                    print("angrier. You also can't tell if VERONICA was actually offended or was just trying to preemptively end the")
                    print("conversation. You watch her for a few moments, trying to imagine what an imposter would act like, but it's")
                    print("fruitless. You dismiss her (though she's already acting like she's been dismissed) and begin walking back")
                    print("to your quarters, lost in thought.")
                    input()
                
                    # Update storyline
                    player['ch_2'] = {'room': 'life',
                                      'outcome': 'failure'}
                    player['chapter'] = 3
                    save_object(player, "player_stats.pkl")                       
        
                #-----------------------------------------------------------------------------------------------------------
                # A.A.B2.B Apologize
                if life_dec1_3.upper() == 'B':
                    print()
                    print("[*STORY*]")
                    print("VERONICA watches you for a few moments. She seems to be weighing a few options for what to say. Finally, she")
                    print("speaks.")
                    input()
                    print("[VERONICA]")
                    print("I'm sorry, Commander. I should have been honest from the start. I... I woke up with a migraine and it hurts")
                    print("so much that I'm having a hard time thinking about anything else. I'm having a hard time focusing, and I can")
                    print("barely remember my tasks for the day. I apologize for being curt, but I just want to finish my work so I can")
                    print("rest.")
                    input()
                    
                    # End chapter (based on what happened in chapter one)                       
                    if player['ch_1']['outcome'] in ['kill_hide', 'kill_lock']:
                        print("[*STORY*]")
                        print("Headache? Hazy memory?? That sounds like what you were feeling this morning... and still continue to feel. Your")
                        print("hand itches for the knife in your pocket but you hold back. You make some idle chat with VERONICA for a minute")
                        print("before dismissing her and beginning the walk back to your quarters. Having a hazy memory sure sounds like something")
                        print("an imposter would say, but SHIP may have more insights...")
                        input()
                    
                    if player['ch_1']['outcome'] == 'failure':
                        print("[*STORY*]")
                        print("Headache? Hazy memory?? That sounds uncomfortably like what you were feeling this morning... and still continue to feel.")
                        print("You make some idle chat with VERONICA for a minute before dismissing her and slowly beginning the walk back to your")
                        print("quarters. Having a hazy memory sure sounds like something an imposter would say... but on second thought, you're not")
                        print("sure. Your thoughts wander back to BENJAMIN and how little information he was willing to share...")
                        input()
                        
                    if player['ch_1']['outcome'] == 'minor_reveal':
                        print("[*STORY*]")
                        print("Headache? Hazy memory?? That sounds uncomfortably like what you were feeling this morning... and still continue to feel.")
                        print("BENJAMIN mentioned that he had a headache, too. Your heart drops. Somehow, all crew members awoke with a headache this")
                        print("morning... and at least you and VERONICA are having trouble remembering things. You consider telling VERONICA about")
                        print("BENJAMIN... but you decide to keep quiet. You dismiss VERONICA and slowly begin walking back to your quarters, a knot")
                        print("in your stomach.")
                        input()
                    
                    if player['ch_1']['outcome'] == 'major_reveal':
                        print("[*STORY*]")
                        print("Your jaw drops. Headache? Memory loss?? That's exactly what BENJAMIN said he was experiencing, and that you've been")
                        print("feeling all day. Your heart starts racing. Somehow, all crew members awoke today with no recollection of who they really")
                        print("are... and head pain. Suddenly, you feel a lot less safe than you felt before. You absently dismiss VERONICA and slowly")
                        print("start walking back to your quarters. This is going to require some thinking, if you can stop your hands from shaking")
                        print("first.")
                        input()
                    
                    if player['ch_1']['outcome'] == 'full_reveal':
                        print("[*STORY*]")
                        print("Your jaw drops. Headache? Memory loss?? That's exactly what BENJAMIN said he was experiencing, and that you've been")
                        print("feeling all day. Your heart starts racing. Somehow, all crew members awoke today with no recollection of who they really")
                        print("are... and head pain. Suddenly, you feel a lot less safe than you felt before, and your thoughts rush back to BENJAMIN")
                        print("and what he said about trusting SHIP. If you can't trust SHIP, and everyone is experiencing amnesia and head pain...")
                        print("you absently dismiss VERONICA and start walking back to your quarters. This is going to require some thinking, if you")
                        print("can stop your hands from shaking first.")
                        input()
                        
                    # Update storyline
                    player['ch_2'] = {'room': 'life',
                                      'outcome': 'major_reveal'}
                    player['chapter'] = 3
                    save_object(player, "player_stats.pkl")

#--------------------------------------------------------------------------------------------------------------------------------
# B. Intimidate (ask about work)
if intimidate == True:
    
    # Random draw
    intimidate_outcome = random.sample(range(100), 1)
    
    #----------------------------------------------------------------------------------------------------------------------------
    # B1. Intimidate success
    if intimidate_outcome < [50]:
        print()
        print("[SUCCESS]")
        print("VERONICA pauses. She seems to be weighing her options... which definitely makes it seem she's hiding something.")
        input()
        print(f"[{player['name']}]".upper())
        print("Come on, VERONICA. Tell me what's going on.")
        input()
        print("[VERONICA]")
        print("Ok. Sorry, Commander. It's just been a strange day... I awoke with a huge headache. But anyway, I've been looking")
        print("into memory loss. I think it could be a concern for the crew.")
        input()

        # Think about how you killed BENJAMIN
        if player['ch_1']['outcome'] in ['kill_hide', 'kill_lock']:
            print("[*STORY*]")
            print("You wonder if BENJAMIN also had a headache in the moments before you stabbed him repeatedly. Just the thought")
            print("of violence makes you smile, and you have to hold back a big laugh. After a moment you settle your racing")
            print("heart. You lick your lips as you wonder why VERONICA is studying memory loss...")
            input()
        
        # Don't have any info on BENJAMIN
        if player['ch_1']['outcome'] == 'failure':
            print("[*STORY*]")
            print("Headache? Could hers be like what you had this morning, and continue to have? You wonder if BENJAMIN has head")
            print("pain as well, but good luck getting any information out of him after that last conversation... you also can't")
            print("help but wonder why she's studying memory loss.")
            input()
        
        # Know BENJAMIN has a headache
        if player['ch_1']['outcome'] == 'minor_reveal':
            print("[*STORY*]")
            print("Headache?? Your heart drops. Somehow, all crew members awoke with a headache this morning... you also find it")
            print("unsettling that she's researching memory loss while you can't remember a thing.")
            input()
        
        # Know BENJAMIN has a headache and memory loss
        if player['ch_1']['outcome'] == 'major_reveal':
            print("[*STORY*]")
            print("Headache?? Your heart drops. Somehow, all crew members awoke with a headache this morning... and at least you")
            print("and BENJAMIN have memory loss. Could VERONICA be the imposter...? You find it unsettling that she's researching")
            print("memory loss while you can't remember a thing.")
            input()
        
        # Full reveal from BENJAMIN
        if player['ch_1']['outcome'] == 'full_reveal':
            print("[*STORY*]")
            print("Headache?? Your heart drops. Somehow, all crew members awoke with a headache this morning... and at least you")
            print("and BENJAMIN have memory loss. Could VERONICA be the imposter...? You think back to what BENJAMIN said about")
            print("not trusting SHIP and you find yourself even more confused than before. You also find it unsettling that she's")
            print("researching memory loss while you can't remember a thing.")
            input()
        
        # All storylines reconverge
        print(f"[{player['name']}]".upper())
        print("A - [FRIENDSHIP] Why are you researching memory loss?")
        print()
        print("B - [INTIMIDATION] Are you the reason I can't remember anything?")
        print()
        print("C - [ATTACK VERONICA]")
        input()

        # Decision
        life_dec1_1 = ''
        while life_dec1_1.upper() not in ['A', 'B', 'C']:
            life_dec1_1 = input("[CHOICE (A/B/C)]:    ")

        # If attack, flip the boolean
        if life_dec1_1.upper() == 'C':
            attack = True

        #-----------------------------------------------------------------------------------------------------------------------
        # B1.A Friendship
        if life_dec1_1.upper() == 'A':
            print()
            print("[*STORY*]")
            print("VERONICA watches you for a few moments. She seems to be weighing a few options for what to say. Finally, she")
            print("speaks.")
            input()
            print("[VERONICA]")
            print("Commander... I've been having a strange day. I... I awoke with a migraine that hurts so much that I'm having")
            print("a hard time thinking about anything else. I can barely focus or remember my tasks for the day... or even what")
            print("I was doing yesterday or the day before that. I've dedicated the morning to researching my symptoms. If you'll")
            print("excuse me, Commander. I really just want to finish my work and rest.")
            input()
                  
            # End chapter - killed BENJAMIN
            if player['ch_1']['outcome'] in ['kill_hide', 'kill_lock']: 
                print("[*STORY*]")
                print("It seems like there's more to the story, but that's as much as you'll get out of VERONICA now. You consider")
                print("telling VERONICA about how much fun you had sending BENJAMIN to the afterlife, but it doesn't feel like the")
                print("right time. You dismiss her and begin the slow walk back to your quarters, quietly singing to yourself.")
                input()
                     
            # End chapter - have no info on BENJAMIN
            if player['ch_1']['outcome'] == 'failure': 
                print("[*STORY*]")
                print("It seems like there's more to the story, but that's as much as you'll get out of VERONICA now. You dismiss")
                print("her and begin the slow walk back to your quarters, your stomach in knots. There's much to think about...")
                input()
                
            # End chapter - do have some info on BENJAMIN
            if player['ch_1']['outcome'] in ['minor_reveal', 'major_reveal', 'full_reveal']:
                print("[*STORY*]")
                print("It seems like there's more to the story, but that's as much as you'll get out of VERONICA now. You consider")
                print("telling VERONICA about your conversation with BENJAMIN, but it doesn't feel like the right time. You dismiss")
                print("VERONICA and begin the slow walk back to your quarters, your stomach in knots. There's much to think about...")
                input()
            
            # Update storyline
            player['ch_2'] = {'room': 'life',
                              'outcome': 'major_reveal'}
            player['chapter'] = 3
            save_object(player, "player_stats.pkl")
        
        #-----------------------------------------------------------------------------------------------------------------------
        # B1.B Intimidation
        if life_dec1_1.upper() == 'B':
            print()
            print("[*STORY*]")
            print("VERONICA is shocked. She stares at you, her mouth open. After what feels like a minute, she finally speaks.")
            input()
            print("[VERONICA]")
            print("Did you just say you can't remember anything?")
            input()
            print(f"[{player['name']}]".upper())
            print("Yes.")
            input()
            print("[*STORY*]")
            print("VERONICA slowly shakes her head, her eyes wide. She glances at the microscope and then the pile of articles")
            print("next to her. The top one has a paragraph that's been highlighted yellow. VERONICA thinks for a few moments")
            print("and then begins to speak, her voice a whisper.")
            input()
            print("[VERONICA]")
            print("I think you and I may be experiencing the effects of a nerve gas that causes temporary amnesia. Its strongest")
            print("effect is persistent headaches.")
            input()
            
            # Think about how you killed BENJAMIN
            if player['ch_1']['outcome'] in ['kill_hide', 'kill_lock']:
                print("[*STORY*]")
                print("You wonder if BENJAMIN also had a headache or amnesia in the moments before you stabbed him repeatedly. Just")
                print("the thought of violence makes you smile, and you have to hold back a big laugh. After a moment you settle your")
                print("racing heart, lick your lips, and turn back to VERONICA.")
                input()
                print(f"[{player['name']}]".upper())
                print("Do you know how to cure the amnesia?")
                input()
                            
            # Respond: "hm, interesting"
            if player['ch_1']['outcome'] == 'failure':
                print("[*STORY*]")
                print("You wonder if BENJAMIN also has a headache or amnesia, but you learned nothing when you talked to him. Either")
                print("he has something to hide or you're *really* hit-or-miss when it comes to getting information from your crew.")
                input()
                print(f"[{player['name']}]".upper())
                print("Do you know how to cure the amnesia?")
                input()
                          
            # Respond: "Benjamin had a headache!" 
            if player['ch_1']['outcome'] == 'minor_reveal':
                print(f"[{player['name']}]".upper())
                print("BENJAMIN has a headache, too.")
                input()
                print("[*STORY*]")
                print("VERONICA is silent for a few moments. She looks at her microscope again and slowly shakes her head.")
                input()
                print("[VERONICA]")
                print("I know; I talked with him twenty minutes ago.")
                input()
                print("[*STORY*]")
                print("You wait for VERONICA to say more but she's silent. You wonder if BENJAMIN can't remember anything, either...")
                print("that would explain some things. You'll have to think about it later.")
                input()
                print(f"[{player['name']}]".upper())
                print("Do you know how to cure the amnesia?")
                input()
                
            # Respond: "Benjamin had a headache and amnesia, too!"
            if player['ch_1']['outcome'] in ['major_reveal', 'full_reveal']:
                print(f"[{player['name']}]".upper())
                print("BENJAMIN has a headache and memory loss, too.")
                input()
                print("[*STORY*]")
                print("VERONICA is silent for a few moments. She looks at her microscope again and slowly shakes her head.")
                input()
                print("[VERONICA]")
                print("I know; I talked with him twenty minutes ago. It would have been strange for only part of the crew to have")
                print("headaches and memory loss.")
                input()
                
                if player['ch_1']['outcome'] == 'major_reveal':
                    print("[*STORY*]")
                    print("You feel a knot in your stomach. Everyone in the crew has headaches and amnesia. Either there's someone else on")
                    print("board, SHIP is wrong, or VERONICA and BENJAMIN are lying to you... but the last option surprisingly seems the")
                    print("least likely.")
                    input()              
                    print(f"[{player['name']}]".upper())
                    print("Do you know how to cure the amnesia?")
                    input()
                 
                if player['ch_1']['outcome'] == 'full_reveal':
                    print("[*STORY*]")
                    print("You feel a knot in your stomach. Everyone in the crew has headaches and amnesia. Either there's someone else on")
                    print("board, SHIP is wrong, or VERONICA and BENJAMIN are lying to you... but the last option surprisingly seems the")
                    print("least likely. You think back to what BENJAMIN said about how he doesn't trust the ship, and suddenly you start")
                    print("sharing his suspicions.")
                    input()              
                    print(f"[{player['name']}]".upper())
                    print("BENJAMIN... suspects SHIP. He thinks we shouldn't trust the AI. I think I agree.")
                    input()
                    print("[*STORY*]")
                    print("VERONICA stares at you for a few seconds. Clearly BENJAMIN didn't tell that to her. You stare back at her,")
                    print("thinking the same thing. Finally, she speaks.")
                    input()
                    print("[VERONICA]")
                    print("How are we going to get home if we can't trust SHIP? God damn it...")
                    input()
                    print(f"[{player['name']}]".upper())
                    print("First things first. Do you have any way to fight this amnesia?")
                    input()
                    print("[VERONICA]")
                    print("I do. I've been researching a way to reverse the effects of the toxin, and I suspect I'm close to finishing. I")
                    print("need probably two more hours.")
                    input()
                    print("[*STORY*]")
                    print("SHIP said there's only about an hour left until it can't hold off the malicious attack... but could that really")
                    print("be true? What if there actually wasn't an attack happening right now?")
                    input()
                    print(f"[{player['name']}]".upper())
                    print("Work as fast as you can, VERONICA. I'll work on SHIP. Be careful... anything could happen in the next hour.")
                    input()
                    
                    # Update storyline
                    player['ch_2'] = {'room': 'life',
                                      'outcome': 'full_reveal'}
                    player['chapter'] = 3
                    save_object(player, "player_stats.pkl")
                        
            #---------------------------------------------------------------------------------------------------------------------
            # All other story lines converge
            if player['ch_1']['outcome'] != 'full_reveal':
                
                print("[VERONICA]")
                print("I do. I've been researching a way to reverse the effects of the toxin, and I suspect I'm close to finishing. I")
                print("need probably two more hours.")
                input()
                print("[*STORY*]")
                print("SHIP said there's only about an hour left until it can't hold off the malicious attack... your memory is useless")
                print("but you doubt SHIP's often been wrong on complex calculations. If SHIP were to fail and a malicious actor gained")
                print("control... you doubt any of the crew would survive for very long. Or something more sinister would happen... for")
                print("now, we just need to keep moving.")
                input()
                print(f"[{player['name']}]".upper())
                print("Work as fast as you can, VERONICA. The sooner our memories return, the better.")
                input()

                # Update storyline
                player['ch_2'] = {'room': 'life',
                                  'outcome': 'full_reveal'}
                player['chapter'] = 3
                save_object(player, "player_stats.pkl")

    #----------------------------------------------------------------------------------------------------------------------------
    # B2. Intimidate failure
    if intimidate_outcome >= [50]:
        print()
        print("[FAILURE]")
        print("VERONICA pauses and frowns. Maybe that wasn't a good idea.")
        input()
        print("[VERONICA]")         
        print("My work is stressful, Commander. All of our jobs entail stress, and I don't appreciate you unloading yours onto")
        print("me.")
        
        # Response
        print(f"[{player['name']}]".upper())
        print("A - I can do whatever I want!")
        print()
        print("B - Sorry. I lost my temper.")
        print()
            
        # Decision
        life_dec1_1 = ''
        while life_dec1_1.upper() not in ['A', 'B']:
            life_dec1_1 = input("[CHOICE (A/B)]:    ")
            
        #-----------------------------------------------------------------------------------------------------------
        # B2.A Don't back down
        if life_dec1_1.upper() == 'A':
            print()
            print("[*STORY*]")
            print("VERONICA's eyes narrow. She turns from you and gets back to work.")
            input()
            print("[VERONICA]")
            print("If you're having difficulty dealing with your stress, I suggest a nap. Now please excuse me; I'm very busy.")
            input()
        
            # Update suspicion
            player['crew_suspicion']['VERONICA'] += 1
            print("* " * 5, "VERONICA suspicion increases by 1.", " *" * 5)
            input()
                            
            # End chapter
            print("[*STORY*]")
            print("No luck. You want to press VERONICA further, but the conversation is clearly over. You regret losing your")
            print("temper... what were you thinking? You can't remember... which just makes you even angrier. You also can't")
            print("tell if VERONICA was actually offended or was just trying to preemptively end the conversation. You watch")
            print("her for a few moments, trying to imagine what an imposter would act like, but it's fruitless. You dismiss")
            print("her (though she's already acting like she's been dismissed) and begin walking back to your quarters, lost")
            print("in thought.")
            input()
        
            # Update storyline
            player['ch_2'] = {'room': 'life',
                              'outcome': 'failure'}
            player['chapter'] = 3
            save_object(player, "player_stats.pkl")  
        
        #-----------------------------------------------------------------------------------------------------------
        # B2.B Apologize
        if life_dec1_1.upper() == 'B':
            print()
            print("[*STORY*]")
            print("VERONICA watches you for a few moments. She seems to be weighing a few options for what to say. Finally, she")
            print("speaks.")
            input()
            print("[VERONICA]")
            print("I'm sorry, Commander. I've just been having a strange day. I... I woke up with a migraine and it hurts so")
            print("much that I'm having a hard time thinking about anything else. I'm having a hard time focusing, and I can")
            print("barely remember my tasks for the day. I apologize for being curt, but I just want to finish my work so I can")
            print("rest.")
            input()
            
            # End chapter (based on what happened in chapter one)
            if player['ch_1']['outcome'] in ['kill_hide', 'kill_lock']:
                print("[*STORY*]")
                print("Headache? Hazy memory?? That sounds like what you were feeling this morning... and still continue to feel. Your")
                print("hand itches for the knife in your pocket but you hold back. You make some idle chat with VERONICA for a minute")
                print("before dismissing her and beginning the walk back to your quarters. Having a hazy memory sure sounds like something")
                print("an imposter would say, but SHIP may have more insights...")
                input()
                           
            if player['ch_1']['outcome'] == 'failure':
                print("[*STORY*]")
                print("Headache? Hazy memory?? That sounds uncomfortably like what you were feeling this morning... and still continue")
                print("to feel. You make some idle chat with VERONICA for a minute before dismissing her and slowly beginning the walk")
                print("back to your quarters. Having a hazy memory sure sounds like something an imposter would say... but on second")
                print("thought, you're not sure. Your thoughts wander back to BENJAMIN and how little information he was willing to")
                print("share...")
                input()
                
            if player['ch_1']['outcome'] == 'minor_reveal':
                print("[*STORY*]")
                print("Headache? Hazy memory?? That sounds uncomfortably like what you were feeling this morning... and still continue")
                print("to feel. BENJAMIN mentioned that he had a headache, too. Your heart drops. Somehow, all crew members awoke with")
                print("a headache this morning... and at least you and VERONICA are having trouble remembering things. You consider")
                print("telling VERONICA about BENJAMIN... but you decide to keep quiet. You dismiss VERONICA and slowly begin walking")
                print("back to your quarters, a knot in your stomach.")
                input()
            
            if player['ch_1']['outcome'] == 'major_reveal':
                print("[*STORY*]")
                print("Your jaw drops. Headache? Memory loss?? That's exactly what BENJAMIN said he was experiencing, and that you've been")
                print("feeling all day. Your heart starts racing. Somehow, all crew members awoke today with no recollection of who they really")
                print("are... and head pain. Suddenly, you feel a lot less safe than you felt before. You absently dismiss VERONICA and slowly")
                print("start walking back to your quarters. This is going to require some thinking, if you can stop your hands from shaking")
                print("first.")
                input()
            
            if player['ch_1']['outcome'] == 'full_reveal':
                print("[*STORY*]")
                print("Your jaw drops. Headache? Memory loss?? That's exactly what BENJAMIN said he was experiencing, and that you've been")
                print("feeling all day. Your heart starts racing. Somehow, all crew members awoke today with no recollection of who they really")
                print("are... and head pain. Suddenly, you feel a lot less safe than you felt before, and your thoughts rush back to BENJAMIN")
                print("and what he said about trusting SHIP. If you can't trust SHIP, and everyone is experiencing amnesia and head pain...")
                print("you absently dismiss VERONICA and start walking back to your quarters. This is going to require some thinking, if you")
                print("can stop your hands from shaking first.")
                input()
                
            # Update storyline
            player['ch_2'] = {'room': 'life',
                              'outcome': 'major_reveal'}
            player['chapter'] = 3
            save_object(player, "player_stats.pkl")     
                 
#-------------------------------------------------------------------------------------------------------------------------------
# Attack VERONICA
if attack == True:
    print()
    print("[*STORY*]")
    print("You slowly walk towards VERONICA, your hand on the knife in your pocket. Her eyes dart to your pocket and then back up")
    print("to you.")
    input()
    print("[*STORY*]")
    print("You attack! You leap at VERONICA, pulling out the laser knife and swinging down at her. She rolls out of the way, faster")
    print("than you'd expected, and pulls out her own laser knife. Where did she...? Too late to think now. You swing at her again")
    print("but she blocks your arm and swiftly cuts across your ribs, tearing your uniform. Before you can react, she's behind you")
    print("and you feel a sudden sharp, burning feeling in your back. You look down and see the knife protruding from your chest.")
    print("You fall to your knees as the darkness rushes in, and your last thoughts are that at least you caught the imposter...")
    input()
    input(".")
    input(".")
    input(".")   
    print()
    print("                                            [YOUR QUEST COMES TO AN END]")
    print("                                                     Ending #3")
    print()
    print("                                                      OUTCOMES:")
    print(f"                                                 - {player['name'].upper()} dies")
    print("                                                 - BENJAMIN lives")
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
                
                
                
                
  