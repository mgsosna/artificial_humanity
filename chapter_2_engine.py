########################################################################################################
# ARTIFICIAL HUMANITY
# Chapter 2b: Engine Room
#
# Matt Grobis
########################################################################################################
# Where you could be coming from:
# - Got no info from VERONICA
# - You know she has a headache
# - You know she has a headache + memory loss
# - You know she has a headache + memory loss + is working on antidote

import pickle
from custom_functions import *
import random

player = pickle.load(open('player_stats.pkl', 'rb'))

# Initialize variables
attack = False
intimidate = False

print()
print("[*STORY*]")
print("Time is running out, indeed. You exit your quarters, absently fingering your laser knife as you walk. You are in a well-lit")
print("white hallway. As you walk towards the engine room, the hallway gradually changes to metallic, pipes overhead and metal")
print("grating on the floor and walls. A crew of three is hardly enough to finance fancy white panelling for the entire ship,")
print("you suppose. The door to the engine room opens as you approach and you see BENJAMIN working. He is wearing the standard")
print("mechanic attire - dark green pants and light green shirt. While most of his hair has balded off already, the little")
print("that remains is brown. BENJAMIN looks up as you enter the room and waves.")
input()

# BENJAMIN talks to you
print("[BENJAMIN]")
print("Commander! Good to see you! How are things?")

# You respond
print(f"[{player['name']}]".upper())
print("A - I'm doing well, BENJAMIN. How's your work going?")
print()
print("B - [ATTACK BENJAMIN]")
print()

# Choice
eng_dec1 = ""
while eng_dec1.upper() not in ['A', 'B']:
    eng_dec1 = input("[CHOICE (A/B)]:   ")

# If attack, change that boolean
if eng_dec1.upper() == 'B':
    attack = True

#---------------------------------------------------------------------------------------------------------------------------
# A. Friendship
if eng_dec1.upper() == 'A':
    print()
    
    # BENJAMIN says he's from Iowa
    print("[BENJAMIN]")
    print("Can't complain! As a native Iowan, as long as there's food on the table, life's good... even if the food is space rations.")
    input()

    # You respond
    print(f"[{player['name']}]".upper())
    print("A - [FRIENDSHIP] Haha, sure thing. Was the food good in Iowa?")
    print()
    print("B - [INTIMIDATION] You seem awfully chipper. What's going on?")
    print("    o Success [75%]: BENJAMIN opens up")
    print("    o Failure [25%]: BENJAMIN withdraws")
    print()
    print("C - [ATTACK BENJAMIN]")
    print()

    # Choice
    eng_dec1_1 = ""
    while eng_dec1_1.upper() not in ['A', 'B', 'C']:
        eng_dec1_1 = input("[CHOICE (A/B/C)]:   ")
        
    # If intimidate or attack, change that boolean        
    if eng_dec1_1.upper() == 'B':
        intimidate = True
    
    if eng_dec1_1.upper() == 'C':
        attack = True

    #---------------------------------------------------------------------------------------------------------------------------------
    # A.A Friendship again
    if eng_dec1_1.upper() == 'A':
        
        # BENJAMIN misspeaks and says he's from Ohio
        print("[BENJAMIN]")
        print("Oh yes! Ears of corn, fresh apples, nice glass of milk... everything from Ohio tastes like Heaven.")
        input()       
        print("[*STORY*]")
        print("BENJAMIN pauses, still smiling. His eyes grow wide... then his smile fades a bit and he coughs.")
        input()
        print("[BENJAMIN]")
        print("But, uh, enough about me, Commander. Where are you from again?")
        input()
        print(f"[{player['name']}]".upper())
        print("Hang on, BENJAMIN. Didn't you just say you're from Iowa?")
        input()
        print("[*STORY*]")
        print("BENJAMIN's smile returns but now it's forced, almost panicked. He coughs again.")
        input()
        print("[BENJAMIN]")
        print("S-sorry, Commander. Sometimes I misspeak when I get nervous...")
        input()
        
        # You respond
        print(f"[{player['name']}]".upper())
        print("A - [FRIENDSHIP] What's there to be nervous about, buddy? We're all on the same team!")
        print()
        print("B - [INTIMIDATION] You've got five seconds to explain what's going on, asshole.")
        print()
        print("C - [ATTACK BENJAMIN]")
        print()
             
        # Choice
        eng_dec1_2 = ""
        while eng_dec1_2.upper() not in ['A', 'B', 'C']:
            eng_dec1_2 = input("[CHOICE (A/B/C)]:   ")
            
        # If attack, change that boolean
        if eng_dec1_2.upper() == 'C':
            attack = True
            
        #-------------------------------------------------------------------------------------------------------------------
        # A.A.A/B Friendship *again*... or intimidation
        if eng_dec1_2.upper() == 'A' or eng_dec1_2.upper() == 'B':
            print()
            print("[*STORY*]")
            
            if eng_dec1_2.upper() == 'A':
                print("BENJAMIN eyes you for a moment before bursting into tears. You're surprised and immediately hug him. After")
                print("a few seconds, BENJAMIN wipes his eyes and looks up.")
                input()
                
            if eng_dec1_2.upper() == 'B':
                print("Your voice startles BENJAMIN and he bursts into tears. You watch him cry for a few seconds before he finally")
                print("wipes his eyes and looks up.")
                input()
            
            print("[BENJAMIN]")
            print("I'm sorry, Commander. It's just all been overwhelming. I woke up with such a headache, and... I know this'll")
            print("sound crazy, but I...")
            input()
            print("[*STORY*]")
            print("BENJAMIN glances around before starting to whisper.")
            input()
            print("[BENJAMIN]")
            print("...I just can't remember anything, Commander. My past. What I'm supposed to be doing here. Even, really, who you")
            print("are. And to be honest...")
            input()
            print("[*STORY*]")
            print("BENJAMIN's voice is so quiet at this point that you have to lean in to hear him.")
            input()
            print("[BENJAMIN]")
            print("I don't trust the ship. I might not remember anything, but I know a thing or two about electronics. I get the")
            print("feeling that I'm being watched... and not by a person.")
            input()
                                    
            # End chapter (based on what happened in chapter one)
            if player['ch_1']['outcome'] == 'failure':
                print("[*STORY*]")
                print("Headache? Hazy memory?? That sounds uncomfortably like what you were feeling this morning... and still continue to feel.")
                print("BENJAMIN laughs nervously; his voice sounds strained, and he quickly wipes away another tear. Could he really mean what")
                print("he said? How would he know? You search your memory but, as usual, it comes up empty-handed. If you can't trust the Ship")
                print("AI... your thoughts wander to VERONICA and how little information she was willing to share... can you trust either of them?")
                print("You absently dismiss BENJAMIN and start the long, cold walk back to your quarters.")
                input()
                
            if player['ch_1']['outcome'] == 'minor_reveal':
                print("[*STORY*]")
                print("Headache? Hazy memory?? That sounds uncomfortably like what you were feeling this morning... and still continue to feel.")
                print("VERONICA mentioned that she had a headache, too. Your heart drops. Somehow, all crew members awoke with a headache this")
                print("morning... and at least you and BENJAMIN are having trouble remembering things. You consider telling BENJAMIN about")
                print("VERONICA... but you decide to keep quiet. Your attention is brought back to the present as BENJAMIN laughs nervously;")
                print("his voice sounds strained, and he quickly wipes away another tear. Could he really mean what he said about the ship? How")
                print("would he know? You search your memory but, as usual, it comes up empty-handed. If you can't trust the Ship AI... you slowly")
                print("begin walking back to your quarters, your stomach in knots.")
                input()
            
            if player['ch_1']['outcome'] == 'major_reveal':
                print("[*STORY*]")
                print("Your jaw drops. Headache? Memory loss?? That's exactly what VERONICA said she was experiencing, and that you've been feeling")
                print("all day. Your heart starts racing. Somehow, all crew members awoke today with no recollection of who they really are... and head")
                print("pain. Suddenly, you feel a lot less safe than you felt before. Your thoughts tiptoe cautiously, hesitantly, to the Ship AI... could")
                print("BENJAMIN really mean what he just said? How would he know? You search your memory but, as usual, it comes up empty-handed. If you")
                print("can't trust the Ship AI... you absently dismiss BENJAMIN and slowly start walking back to your quarters. This is going to require some")
                print("thinking, if you can stop your hands from shaking first.")
                input()
            
            if player['ch_1']['outcome'] == 'full_reveal':
                print("[*STORY*]")
                print("Your jaw drops. Headache? Memory loss?? That's exactly what VERONICA said she was experiencing, and that you've been feeling")
                print("all day. Your heart starts racing. Somehow, all crew members awoke today with no recollection of who they really are... and head")
                print("pain. Suddenly, you feel a lot less safe than you felt before. Your thoughts tiptoe cautiously, hesitantly, to the Ship AI... could")
                print("BENJAMIN really mean what he just said? How would he know? You search your memory but, as usual, it comes up empty-handed. If you")
                print("can't trust the Ship AI... your thoughts turn to VERONICA and her work for an antidote. Will she finish in time? Can SHIP even be") 
                print("trusted in allowing VERONICA to finish? You absently dismiss BENJAMIN and slowly start walking back to your quarters. This is going")
                print("to require some thinking, if you can stop your hands from shaking first.")
                input()
                       
            # Update storyline
            player['ch_2'] = {'room': 'engine',
                              'outcome': 'full_reveal'} 
            player['chapter'] = 3
            save_object(player, "player_stats.pkl")
           
#---------------------------------------------------------------------------------------------------------------------------------
# B. Intimidation
if intimidate == True:
    
    # Random draw
    intimidate_outcome = random.sample(range(100), 1)
    
    #----------------------------------------------------------------------------------------------------------------------------
    # B1. Intimidate success
    if intimidate_outcome < [75]:
        print()
        print("[SUCCESS]")
        print("BENJAMIN's smile falters. He seems to think for a moment before answering.")
        input()
        print("[BENJAMIN]")
        print("Nothing is going on, Commander. Back in Ohio, we're all just used to being this friendly. I'm not sure what to say,")
        print("honestly!")
        input()
        
        # You respond
        print(f"[{player['name']}]".upper())
        print("A - [INTIMIDATION] Didn't you say you're from Iowa?")
        print("    o Success [50%]: BENJAMIN opens up")
        print("    o Failure [50%]: BENJAMIN withdraws")
        print()
        print("B - [ATTACK BENJAMIN]")
        print()
        
        # Choice
        eng_dec1_1 = ""
        while eng_dec1_1.upper() not in ['A', 'B']:
            eng_dec1_1 = input("[CHOICE (A/B)]:   ")
            
        # If attack, change the boolean
        if eng_dec1_1.upper() == 'B':
            attack = True
            
        #-----------------------------------------------------------------------------------------------------------------------
        # B1.A Intimidate again
        if eng_dec1_1.upper() == 'A':
            
            # Random draw
            intimidate_outcome2 = random.sample(range(100), 1)
            
            #-------------------------------------------------------------------------------------------------------------------
            # B1.A1 Intimidate success
            if intimidate_outcome2 < [50]:
                print()
                print("[SUCCESS]")
                print("BENJAMIN looks at you for a moment, his mouth open. He closes his eyes, rubs his forehead, and then begins to")
                print("speak.")
                input()
                print("[BENJAMIN]")
                print("Commander... I... I don't know what to say. Er, yes, I said I was from Iowa - I mean, that I *am* from Iowa. But")
                print("what I meant to say - ")
                input()
                print(f"[{player['name']}]".upper())
                print("Cut the crap, BENJAMIN. Give me the truth.")
                input()
                print("[*STORY*]")
                print("BENJAMIN is again speechless. He looks like he's trying to find any way to exit the conversation... but he finally")
                print("closes his eyes and sighs.")
                input()
                print("[BENJAMIN]")
                print("I'm sorry, Commander. I haven't been fully honest. I... I've been having a really strange day. I... I'm having trouble")
                print("remembering really simple things. Where I'm from. Why I'm here, what I'm supposed to be doing. I've got such a crazy")
                print("headache, I can barely think straight. But I won't let it affect my work, Commander.")
                input()

                # End chapter (based on what happened in chapter one)
                if player['ch_1']['outcome'] == 'failure':
                    print("[*STORY*]")
                    print("Headache? Hazy memory?? That sounds uncomfortably like what you were feeling this morning... and still continue to feel.")
                    print("You make some idle chat with BENJAMIN for a minute before dismissing him and slowly beginning the walk back to your")
                    print("quarters. Having a hazy memory sure sounds like something an imposter would say... but on second thought, you're not")
                    print("sure. Your thoughts wander back to VERONICA and how little information she was willing to share...")
                    input()
                    
                if player['ch_1']['outcome'] == 'minor_reveal':
                    print("[*STORY*]")
                    print("Headache? Hazy memory?? That sounds uncomfortably like what you were feeling this morning... and still continue to feel.")
                    print("VERONICA mentioned that she had a headache, too. Your heart drops. Somehow, all crew members awoke with a headache this")
                    print("morning... and at least you and BENJAMIN are having trouble remembering things. You consider telling BENJAMIN about")
                    print("VERONICA... but you decide to keep quiet. You dismiss BENJAMIN and slowly begin walking back to your quarters, a knot")
                    print("in your stomach.")
                    input()
                
                if player['ch_1']['outcome'] == 'major_reveal':
                    print("[*STORY*]")
                    print("Now it's your turn for your mouth to drop. Headache? Memory loss?? That's exactly what VERONICA said she was experiencing,")
                    print("and that you've been feeling all day. Your heart starts racing. Somehow, all crew members awoke today with no recollection")
                    print("of who they really are... and head pain. Suddenly, you feel a lot less safe than you felt before. You absently dismiss")
                    print("BENJAMIN and slowly start walking back to your quarters. This is going to require some thinking, if you can stop your hands")
                    print("from shaking first.")
                    input()
                
                if player['ch_1']['outcome'] == 'full_reveal':
                    print("[*STORY*]")
                    print("Now it's your turn for your mouth to drop. Headache? Memory loss?? That's exactly what VERONICA said she was experiencing,")
                    print("and that you've been feeling all day. Your heart starts racing. Somehow, all crew members awoke today with no recollection")
                    print("of who they really are... and head pain. Suddenly, you feel a lot less safe than you felt before, and your thoughts rush")
                    print("back to VERONICA and her work on an antidote. It can't come quickly enough... but will it come in time? You absently dismiss")
                    print("BENJAMIN and slowly start walking back to your quarters. This is going to require some thinking, if you can stop your hands")
                    print("from shaking first.")
                    input()
                    
                # Update storyline
                player['ch_2'] = {'room': 'engine',
                                  'outcome': 'major_reveal'}
                player['chapter'] = 3
                save_object(player, "player_stats.pkl")
                
            #-------------------------------------------------------------------------------------------------------------------
            # B1.A2 Intimidate failure
            if intimidate_outcome2 >= [50]:
                print()
                print("[FAILURE]")
                print("BENJAMIN winces a moment but then smirks. He shrugs.")
                input()
                print("[BENJAMIN]")
                print("Sorry, Commander. I'm just have a slow day. Woke up with a big headache... been misspeaking. Accidentally wrote down")
                print("the wrong screws in the engine report earlier, too. Sorry I'm slurring things.")
                input()
                print(f"[{player['name']}]".upper())
                print("Cut the crap, BENJAMIN. Give me the truth.")
                input()
                print("[*STORY*]")
                print("BENJAMIN actually turns around and starts quietly humming a tune! The nerve!")
                input()
                print("[BENJAMIN]")
                print("I'm not lying, Commander. Please give it a break. I'd like to get back to work, captain. Sorry.")
                input()
                
                # Update suspicion
                player['crew_suspicion']['BENJAMIN'] += 1
                print("* " * 5, "BENJAMIN suspicion increases by 1.", " *" * 5)
                input()
                
                # End chapter (based on what happened in chapter one)
                if player['ch_1']['outcome'] == 'failure':
                    print("[*STORY*]")
                    print("You're convinced BENJAMIN is full of it, but there's nothing more to be said. You noticed he mentioned a headache...")
                    print("that sounds an awful like what you woke up with this morning. You want to press him further but it won't do any good.")
                    print("Can *anyone* on this damn crew be honest and straightforward with you? A dark shiver passes down your heart as you")
                    print("entertain the thought of there being two imposters on board...")
                    input()
                        
                if player['ch_1']['outcome'] == 'minor_reveal':
                    print("[*STORY*]")
                    print("A headache?? That sounds uncomfortably like what you were feeling this morning... and still continue to feel. VERONICA")
                    print("mentioned that she had a headache, too. Your heart drops. Somehow, all crew members awoke with a headache this morning...")
                    print("You consider telling BENJAMIN about VERONICA but you decide to keep quiet. You dismiss BENJAMIN and slowly begin walking")
                    print("back to your quarters, a knot in your stomach.")
                    input()
                
                if player['ch_1']['outcome'] == 'major_reveal':
                    print("[*STORY*]")
                    print("A headache?? That sounds uncomfortably like what you were feeling this morning... and still continue to feel. VERONICA")
                    print("mentioned that she had a headache, too. Your heart drops. Somehow, all crew members awoke with a headache this morning...")
                    print("and at least you and VERONICA also have memory loss. BENJAMIN's memory doesn't sound too great, either, but getting the")
                    print("facts wrong sounds like something an imposter would do, too. Suddenly, you feel a lot less safe than you felt before. You")
                    print("absently dismiss BENJAMIN and slowly start walking back to your quarters. This is going to require some thinking...")
                    input()
                
                if player['ch_1']['outcome'] == 'full_reveal':
                    print("[*STORY*]")
                    print("A headache?? That sounds uncomfortably like what you were feeling this morning... and still continue to feel. VERONICA")
                    print("mentioned that she had a headache, too. Your heart drops. Somehow, all crew members awoke with a headache this morning...")
                    print("and at least you and VERONICA also have memory loss. BENJAMIN's memory doesn't sound too great, either, but getting the")
                    print("facts wrong sounds like something an imposter would do, too. Suddenly, you feel a lot less safe than you felt before. Your")
                    print("thoughts dart back to VERONICA and her work on an antidote. It can't come quickly enough... but will it come in time? You")
                    print("absently dismiss BENJAMIN and slowly start walking back to your quarters. This is going to require some thinking... if you")
                    print("can stop your hands from shaking first.")
                    input()
                    
                # Update storyline
                player['ch_2'] = {'room': 'engine',
                                  'outcome': 'minor_reveal'}
                player['chapter'] = 3
                save_object(player, "player_stats.pkl")
                 
    #----------------------------------------------------------------------------------------------------------------------------
    # B2. Intimidate failure
    if intimidate_outcome >= [75]:
        print()
        print("[FAILURE]")
        print("BENJAMIN winces a moment but then smirks. He shrugs.")
        input()
        print("[BENJAMIN]")
        print("Sorry, Commander. I'm just have a slow day. I don't appreciate your tone of voice... that would never fly back in")
        print("Iowa. Now if you excuse me, I'd like to get back to work. Sorry.")
        input()
        
        # Update suspicion
        player['crew_suspicion']['BENJAMIN'] += 1
        print("* " * 5, "BENJAMIN suspicion increases by 1.", " *" * 5)
        input()
        
        # End chapter (based on what happened in chapter one)
        if player['ch_1']['outcome'] == 'failure':
            print("[*STORY*]")
            print("You're convinced BENJAMIN is full of it, but there's nothing more to be said. You want to press him further but it")
            print("won't do any good. Can *anyone* on this damn crew be honest and straightforward with you? A dark shiver passes down")
            print("your heart as you entertain the thought of there being two imposters on board...")
            input()
                
        if player['ch_1']['outcome'] == 'minor_reveal':
            print("[*STORY*]")
            print("You're convinced BENJAMIN is full of it, but there's nothing more to be said. You want to press him further but it")
            print("won't do any good. Does he have a headache like VERONICA and you? You watch him for a few moments - he actually turns")
            print("around and starts working and humming a tune... the nerve! - but it's hard to tell. He's already acting like he's been")
            print("dismissed, but you dismiss him anyway and slowly begin walking back to your quarters.")
            input()
            
        if player['ch_1']['outcome'] == 'major_reveal':
            print("[*STORY*]")
            print("You're convinced BENJAMIN is full of it, but there's nothing more to be said. You want to press him further but it")
            print("won't do any good. Does he have a headache like VERONICA and you? Can he remember anything? It's unsettling that you")
            print("and VERONICA have headaches and memory loss but it doesn't seem like BENJAMIN does... or does he? You watch him for")
            print("a few moments - he actually turns around and starts working and humming a tune... the nerve! - but it's hard to tell.")
            print("He's already acting like he's dismissed, but you dismiss him anyway and slowly begin walking back to your quarters.")
            input()   
          
        if player['ch_1']['outcome'] == 'full_reveal':
            print("[*STORY*]")
            print("You're convinced BENJAMIN is full of it, but there's nothing more to be said. You want to press him further but it")
            print("won't do any good. Does he have a headache like VERONICA and you? Can he remember anything? It's unsettling that you")
            print("and VERONICA have headaches and memory loss but it doesn't seem like BENJAMIN does... or does he? You watch him for")
            print("a few moments - he actually turns around and starts working and humming a tune... the nerve! - but it's hard to tell.")
            print("VERONICA's memory antidote can't come fast enough. BENJAMIN is already acting like he's dismissed, but you dismiss him")
            print("anyway and slowly begin walking back to your quarters.")
            input()   
            
        # Update storyline
        player['ch_2'] = {'room': 'engine',
                          'outcome': 'failure'}
        player['chapter'] = 3
        save_object(player, "player_stats.pkl")
    
#---------------------------------------------------------------------------------------------------------------------------------
# C. Attack BENJAMIN
if attack == True:   
    print()
    print("[*STORY*]")
    print("You've had enough of this! You grab your laser knife and launch at BENJAMIN. You catch him completely unaware.")
    print("True to your training, you hack and slash until BENJAMIN - or what used to be him if you put all the parts back")
    print("together - is lying on the ground. The knife cauterizes fairly well, but the blood that did manage to seep out")
    print("is dark red. If BENJAMIN is - was - the imposter, it was either remarkably lifelike or an actual person. If only")
    print("you could remember anything from before this morning... you search your memory for anything related to BENJAMIN")
    print("but nothing comes up. Maybe he was the imposter after all.")
    input()
    print("[*STORY*]")
    print("You notice his tablet is lying on the table. Hm... that would be a good source of info to see if BENJAMIN is who")
    print("he says he is. You try to open it, but it's impossible to unlock. It won't budge for you; it really needs to be")
    print("BENJAMIN. Unless...")
    input()
    print("[*STORY*]")
    print("You reach down and grab one of BENJAMIN's hands, the one that you sliced off in the melee. You put his index")
    print("finger on the fingerprint scanner and the tablet lights up.")
    input()
    print("[*STORY*]")
    print("Below you are the files BENJAMIN was looking at when he turned off his tablet. It's his personal log, the file")
    print("from StarFleet. It's information about himself, things that he should obviously have known. Hometown. StarFleet")
    print("division. Years of education and awards and degrees. Why would he have been looking at this? You furrow your brow")
    print("as you look at his hometown - Granville, Ohio - and remember he said he was from Iowa.")
    input()
    print("[*STORY*]")              
    print("You'll have to think about this later. You sheath your knife, wipe your hands off with an oily rag, and head back")
    print("to the door. You pause for a moment.")
    input()
    
    # Choice
    print()
    print(f"[{player['name']}]".upper())
    print("A - [LOCK THE DOOR TO THE ENGINE ROOM]")
    print()
    print("B - [KEEP THE DOOR UNLOCKED BUT HIDE BENJAMIN'S BODY]")
    print()
    print("C - [DO NOTHING - YOU'VE KILLED ONCE AND YOU CAN KILL AGAIN]")
    print()
    
    room_dec = ""
    # Decision
    while room_dec.upper() not in ['A', 'B', 'C']:
        room_dec = input("[CHOICE (A/B/C)]:    ")
       
    #--------------------------------------------------------------------------------------------------------------------------
    # C.A. Lock the door
    if room_dec.upper() == 'A':
        print()
        print("[*STORY*]")
        print("You go to the control panel by the door and enter administrative mode. A few moments of tapping on the screen")
        print("and the door closes quietly with a hiss. You hear the grinding of the bolts securing the door in place. No")
        print("one's getting in. You smile slightly and head back to your quarters.")
        input()
        
        # Update storyline
        player['ch_2'] = {'room': 'engine',
                          'outcome': 'kill_lock'} 
        player['chapter'] = 3
        save_object(player, "player_stats.pkl")
        
    #-----------------------------------------------------------------------------------------------------------------------    
    # C.B. Hide BENJAMIN's body
    if room_dec.upper() == 'B':
        print()
        print("[*STORY*]")
        print("You walk back towards BENJAMIN's body. You can't remember if you've ever handled a corpse, but the ease with")
        print("which you carry his body parts and chuck them behind some old machinery suggests that you're well-versed in")
        print("handling the dead. You smile slightly and begin the walk back to your quarters.")
        input()
    
        # Update storyline
        player['ch_2'] = {'room': 'engine',
                          'outcome': 'kill_hide'}
        player['chapter'] = 3
        save_object(player, "player_stats.pkl")
     
    #------------------------------------------------------------------------------------------------------------------------
    # C.C. Do nothing
    if room_dec.upper() == 'C':
        print()
        print("[*STORY*]")
        print("You shrug. Whatever. You walk back to your quarters and hum a cheerful tune.")
        input()
        
        # Update storyline
        player['ch_2'] = {'room': 'engine',
                          'outcome': 'kill_nothing'}
        player['chapter'] = 3
        save_object(player, "player_stats.pkl")
    

