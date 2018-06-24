########################################################################################################
# ARTIFICIAL HUMANITY
# Chapter 1b: life support
#
# Matt Grobis
########################################################################################################
import pickle
from custom_functions import *
import random
import os
import time

player = pickle.load(open('player_stats.pkl', 'rb'))

print()
print("[*STORY*]")
print("You holster your laser knife and exit your quarters. The door slides and locks behind you. You are in a well-lit")
print("white hallway, and as you walk towards the life support systems, you pass a window peering out at the cosmos. Pluto")
print("looms large below you. You continue walking towards life support, which in this ship also doubles as an infirmary")
print("and biological research station. The ship's designers apparently figured that anything vaguely life-related should")
print("be put in the same room. The door opens automatically as you approach and you enter a room full of fridge-sized")
print("machines, along with a small cramped desk with nothing but a microscope. Several large drums filled with water at")
print("various stages of purification are stuffed into the corner, next to freezers with medical supplies and a row of")
print("cabinets. A carbon scrubber hums quietly as it filters the air. VERONICA is nowhere to be found.")
input()

print(f"[{player['name']}]".upper())
print("A - [SEARCH THE ROOM]")
print()
print("B - [DESTROY THE CARBON SCRUBBER]")
print()

# Initialize choices
life_dec1 = ""         
life_dec1_1 = ""
life_dec1_2 = ""
life_dec1_3 = ""
life_dec1_4 = ""

while life_dec1.upper() not in ['A', 'B']:
    life_dec1 = input("[CHOICE (A/B)]:    ")
        
###########################################################################################################################################
###########################################################################################################################################
###########################################################################################################################################
# A. Search the room
if life_dec1.upper() == "A":
    print()
    print("[*STORY*]")
    print("You start searching through the cabinets. Nothing out of the ordinary... pipette tips, syringes, boxes of")
    print("vitamins. The drawers at the table are similarly uninformative - just tablet wipes and a few neatly arranged")
    print("pens.")
    input()
    print("[*STORY*]")
    print("Just when you're thinking of giving up, you notice a drawer that has been left ajar. Inside are some")
    print("uncharacteristically disheveled folders and papers. You flick through them and find article after article")
    print("about mental disorders, concussions, blindness.")
    input()
    
    # VERONICA enters
    print("[VERONICA]")
    print("Commander?")
    input()
    
    print("[*STORY*]")
    print("You pause and look up. VERONCIA is standing in the doorway. She is short, with cropped red hair and the")
    print("standard brown uniform. She seems surprised and concerned to see what you're doing.")
    print()
    
    # Response
    print(f"[{player['name']}]".upper())
    print("A - [INTIMIDATION] Have you been looking through these articles?")
    print("    o Success [75%]: VERONICA opens up.")
    print("    o Failure [25%]: VERONICA grows defensive.")
    print()
    print("B - [FRIENDSHIP] Do you know why these articles are out?")
    print("    o Success [90%]: VERONICA shares a little.")
    print("    o Failure [10%]: VERONICA says even less.")
    print()
    print("C - [ATTACK CARBON SCRUBBER]")
    print("    o Success [??%]: ???")
    print("    o Failure [??%]: ???")
    print()
    
    # Decision
    while life_dec1_1.upper() not in ['A', 'B', 'C']:
        life_dec1_1 = input("[CHOICE (A/B/C)]:    ")
        
    #----------------------------------------------------------------------------------------------------------------------
    # A.A. Intimidation
    if life_dec1_1.upper() == "A":

        # Random draw
        intimidate_outcome1 = random.sample(range(100), 1)

        #-------------------------------------------------------------------------------------------------------------
        # A.A1. Intimidate success
        if intimidate_outcome1 < [75]:          
            print()
            print("[SUCCESS]")
            print("VERONICA shuffles her feet uncomfortably. Her brow is furrowed in concentration and she's not meeting")
            print("your gaze.")
            input()
            print("[VERONICA]")
            print("Commander... yes, I have to admit. This morning, I was reading about how the brain works. It is admittedly")
            print("not part of my research, but it's something I was curious about.")
            input()
            print(f"[{player['name']}]".upper())
            print("A - What do you mean 'how the brain works'?")
            print("B - I don't remember you being a researcher.")
            print()
            
            # Decision
            while life_dec1_2.upper() not in ['A', 'B']:
                life_dec1_2 = input("[CHOICE (A/B)]:    ")
        
            # A.A1.A - How brain works
            if life_dec1_2.upper() == "A":             
                print()
                print("[*STORY*]")
                print("VERONICA shifts her feet again. One of the freezers in the room begins making a high-pitched sound and")
                print("you both wince. You doubt the noise would have affected you if you hadn't awoken with that headache.")
                input()
                print("[VERONICA]")
                print("I was trying to find articles about how the brain forms memories. Our ExNet connection to Earth seems")
                print("not to be working, so I was hoping to find something in what little research we have that's physically")
                print("printed. But no luck. To be honest, I awoke with such a headache this morning that I might need to take")
                print("a break. But I won't let it affect my work, Commander.")
                input()
                  
                # End chapter
                print("[*STORY*]")
                print("You consider pressing VERONICA further but decide against it. You instead dismiss her and begin the walk")
                print("back to your quarters. You can't help but wonder why she's researching memory... and how you awoke unable")
                print("to remember anything. Could she be the imposter? Her headache sounds a lot like yours, but it also sounds")
                print("like a cheap way to get out of the conversation and back to her work... but you're also not sure what her")
                print("job actually is. Is she supposed to be doing research? Or is she looking up memories for some other reason?")
                input()
                    
                # Update storyline
                player['ch_1'] = {'room': 'life',
                                  'outcome': 'minor_reveal'}
                player['chapter'] = 2
                save_object(player, "player_stats.pkl")
                  
            #-------------------------------------------------------------------------------------------------------
            # A.A1.B - Questioning researcher
            if life_dec1_2.upper() == "B":
                print()
                print("[*STORY*]")
                print("VERONICA is caught off guard and begins to sweat. She struggles to speak for a few seconds.")
                input()
                print("[VERONICA]")
                print("Com-commander. I don't know how to respond...")
                input()
                print(f"[{player['name']}]".upper())
                print("You mean you're telling me you're not sure whether you're a researcher or not?")
                input()
                print("[VERONICA]")
                print("That seems like an outrageous question, Commander, but to be honest... now that I think about it,")
                print("I can't for the life of me remember what my job title or responsibilities are.... I'm sorry, I")
                print("understand this must sound crazy. But what is my purpose on this ship?")
                input()
                
                # Response
                print(f"[{player['name']}]".upper())
                print("A - [MAKE UP SOMETHING TECHNICAL-SOUNDING]")
                print()
                print("B - I was hoping you'd know because I don't know, either...")
                print()
                
                # Decision
                while life_dec1_3.upper() not in ['A', 'B']:
                    life_dec1_3 = input("[CHOICE (A/B)]:    ")
            
                #-----------------------------------------------------------------------------------------------------------
                # A.A1.B.A - Make up something
                if life_dec1_3.upper() == "A":
                    print()
                    print(f"[{player['name']}]".upper())
                    print("You're an Endospace Radiobiologist studying the effects of long-term exposure to cosmic")
                    print("radiation in space. And if you don't get back to work, you're going to be our first case")
                    print("study on lethal doses.")
                    input()
                    
                    # End chapter
                    print("[*STORY*]")
                    print("Either your imagination spoke the truth or VERONICA doesn't know the truth, either. She nods, wincing")
                    print("slightly from the movement, and then heads to the microscope. You walk past her and out the door.")
                    print("You're tempted to peek back in the room - is she doing anything in there? - but you decide to just")
                    print("head back to your quarters. You can't help but notice how much VERONICA winced any time she moved")
                    print("her head... and it makes your heart beat uncomfortably when you think about what she just asked.")
                    input()
                    
                    # Update storyline
                    player['ch_1'] = {'room': 'life',
                                      'outcome': 'major_reveal'}
                    player['chapter'] = 2
                    save_object(player, "player_stats.pkl")

                #------------------------------------------------------------------------------------------------------------
                # A.A1.B.B - Be honest
                if life_dec1_3.upper() == "B":
                    print()
                    print("[*STORY*]")
                    print("VERONICA raises her eyebrows. She doesn't say anything for a few moments. When she begins to speak,")
                    print("you realize you might have made a mistake.")
                    input()
                    print("[VERONICA]")
                    print("I'm not sure what you mean by that comment, Commander. As my boss and the one in charge, I'd imagine that")
                    print("you know what you're doing. But that sort of question doesn't leave me with much optimism. If you'd please")
                    print("excuse me. I need to get back to work, and I have such a headache. This conversation is only making it")
                    print("worse.")
                    input()

                    # Update suspicion
                    player['crew_suspicion']['VERONICA'] += 1
                    print("* " * 5, "VERONICA suspicion increases by 1.", " *" * 5)
                    input()
                                        
                    # End chapter
                    print("[*STORY*]")
                    print("After a few awkward moments of silence, you dismiss VERONICA to her duties and leave the room. As you walk")
                    print("back to your quarters, you kick yourself for speaking too honestly. If VERONICA is indeed the imposter,")
                    print("then you've just shown her most of your cards. It'll be hard to recover from this one... and what did she")
                    print("mean about that headache? And could she really not remember her work or was she just trying to get out of")
                    print("the conversation?")
                    input()
                    
                    # Update storyline
                    player['ch_1'] = {'room': 'life',
                                      'outcome': 'major_reveal'}
                    player['chapter'] = 2
                    save_object(player, "player_stats.pkl")

        #-------------------------------------------------------------------------------------------------------------
        # A.A2. Intimidate failure
        if intimidate_outcome1 >= [75]:          
            print()
            print("[FAILURE]")
            print("VERONICA raises her eyebrows and folds her arms.")
            input()
            print("[VERONICA]")
            print("What do you mean by that, Commander? This is my office. I have a right to carry out my job just as")
            print("BENJAMIN and you have to yours.")
            input()
            
            # Response
            print(f"[{player['name']}]".upper())
            print("A - No, what I mean is, er, *why* are you reading about this, VERONICA?")
            print()
            print("B - This isn't your office. You're not a researcher.")
            print("    o Success [50%]: ???")
            print("    o Failure [50%]: ???")
            print()
            
            # Decision
            while life_dec1_3.upper() not in ['A', 'B']:
                life_dec1_3 = input("[CHOICE (A/B)]:    ")
            
            #-----------------------------------------------------------------------------------------------------------
            # A.A2.A - Ask why reading
            if life_dec1_3.upper() == "A":
                print()
                print("[*STORY*]")
                print("VERONICA smiles and enters the room. She walks past you and sits down at the desk.")
                input()
                print("[VERONCIA]")
                print("I'm trying to understand mental health in space. Which is why you hired me... don't you remember?")
                print("At any rate... Commander, I should get back to work. Thank you.")
                input()
                
                # Update suspicion
                player['crew_suspicion']['VERONICA'] += 1
                print("* " * 5, "VERONICA suspicion increases by 1.", " *" * 5)
                input()
                
                # End chapter
                print("[*STORY*]")
                print("You don't like her tone of voice, but you don't feel like you have much bargaining power anymore,")
                print("even as the commander of the ship. You would continue the conversation but the more you think about")
                print("it, the less you're even sure what VERONICA's job is supposed to be. Whether that's indicative of")
                print("an imposter or just how bad your memory has become, you're not sure. Maybe you should be the one")
                print("reading up on memory.... You excuse yourself and begin the walk back to your quarters, lost in")
                print("thought.")
                input()
                                
                # Update storyline
                player['ch_1'] = {'room': 'life',
                                  'outcome': 'failure'}
                player['chapter'] = 2
                save_object(player, "player_stats.pkl")
            
            #-----------------------------------------------------------------------------------------------------------
            # A.A2.B - Cast doubt
            if life_dec1_3.upper() == "B":
                
                doubt_outcome = random.sample(range(100), 1)
                
                # A.A2.B1 Doubt failure
                if doubt_outcome < [50]:
                    print()
                    print("[FAILURE]")
                    print("VERONICA smiles a bit. It seems like she knows you have no idea what you're talking about.")
                    input()
                    print("[VERONICA]")
                    print("Commander, I think I need to get back to work. I have a lot to do. May I recommend you take")
                    print("a nap? I think it would help your mental health.")
                    input()
                    
                    # Update suspicion
                    player['crew_suspicion']['VERONICA'] += 1
                    print("* " * 5, "VERONICA suspicion increases by 1.", " *" * 5)
                    input()
            
                    # End chapter
                    print("[*STORY*]")
                    print("You feel like you should be the one issuing the snappy commands, but at this point you're not sure of")
                    print("much anymore. You actually can't remember what VERONICA's job is supposed to be... or - your stomach")
                    print("turns - what she even should look like. This isn't very promising for identifying an imposter.... You")
                    print("start the long walk back to your quarters, vainly searching the empty cabinets of your memories for")
                    print("clues.")
                    input()
                                    
                    # Update storyline
                    player['ch_1'] = {'room': 'life',
                                      'outcome': 'failure'}
                    player['chapter'] = 2
                    save_object(player, "player_stats.pkl")
            
                #---------------------------------------------------------------------------------------------------------
                # A.A2.B2 Doubt success
                if doubt_outcome >= [50]:
                    print()
                    print("[SUCCESS]")
                    print("VERONICA's smile falters. She suddenly doesn't look so confident.")
                    input()
                    print("[VERONICA]")
                    print("Commander... I... I'm not sure what to say. I have no words. I want to defend myself, but...")
                    
                    print(f"[{player['name']}]".upper())
                    print("Yes?")
                    input()                                       
                    
                    print("[VERONICA]")
                    print("I'm going to sound crazy, Commander, but now that I think about it, I can't for the life of me remember")
                    print("what my job title or responsibilities are.... I'm sorry, I understand this must sound crazy. But what")
                    print("is my purpose on this ship?")
                    input()
                    
                    # Response
                    print(f"[{player['name']}]".upper())
                    print("A - [MAKE UP SOMETHING TECHNICAL-SOUNDING]")
                    print("B - I actually can't remember, either... I have such a headache.")
                    print()
                    
                    # Decision
                    while life_dec1_4.upper() not in ['A', 'B']:
                        life_dec1_4 = input("[CHOICE (A/B)]:    ")
            
                    #-------------------------------------------------------------------------------------------------------
                    # A.A2.B2.A - Make up something
                    if life_dec1_4.upper() == "A":
                        print()
                        print(f"[{player['name']}]".upper())
                        print("You're an Endospace Radiobiologist studying the effects of long-term exposure to cosmic")
                        print("radiation in space. And if you don't get back to work, you're going to be our first case")
                        print("study on lethal doses.")
                        input()
                        
                        # End chapter
                        print("[*STORY*]")
                        print("Either your imagination spoke the truth or VERONICA doesn't know the truth, either. She nods, wincing")
                        print("slightly from the movement, and then heads to the microscope. You walk past her and out the door.")
                        print("You're tempted to peek back in the room - is she doing anything in there? - but you decide to just")
                        print("head back to your quarters. You can't help but notice how much VERONICA winced any time she moved")
                        print("her head... and it makes your heart beat uncomfortably when you think about what she just asked.")
                        input()
                        
                        # Update storyline
                        player['ch_1'] = {'room': 'life',
                                          'outcome': 'major_reveal'}
                        player['chapter'] = 2
                        save_object(player, "player_stats.pkl")
            
                        #---------------------------------------------------------------------------------------------------------
                        # A.A1.B.B - Be honest
                        if life_dec1_4.upper() == "B":
                            print()
                            print("[*STORY*]")
                            print("VERONICA raises her eyebrows. She doesn't say anything for a few moments.")
                            input()
                            print("[VERONICA]")
                            print("Did you just say you have a headache?")
                            input()
                            print(f"[{player['name']}]".upper())
                            print("Yes. I've had one since this morning.")
                            input()
                            print("[*STORY*]")
                            print("VERONICA's eyes widen. She walks to you and begins quickly sorting through the articles. After a")
                            print("few moments, she pulls one out and skims it. She then lets out an exclamation and points to a")
                            print("paragraph buried in the appendix. When she speaks, her voice is a whisper.")
                            input()
                            print("[VERONICA]")
                            print("I think I might be onto something. We might be experiencing the effects of a nerve gas that causes")
                            print("temporary amnesia. Its strongest side effect is persistent headaches.")
                            input()
                            print("[VERONICA]")
                            print("I think I know a way to reverse the effects of the toxin. But I'll have to move quickly. Something")
                            print("tells me that if other members of the crew are experiencing amnesia, something serious is happening.")
                            print("With your permission, Commander. I should start working on this.")
                                                                            
                            # End chapter
                            print("[*STORY*]")
                            print("You dismiss VERONICA and she begins reading another article. You watch her for a few moments - you're")
                            print("brimming with questions - but she's right. You leave her to her work and begin walking back to your")
                            print("quarters. You're not sure why you told her in the heat of the moment about your headache, but it")
                            print("seemed to have cracked through a facade VERONICA had been upholding. Would an imposter have actually")
                            print("been surprised to hear that their nerve agent worked? Then again, whatever concoction VERONICA whips")
                            print("up, you're going to have to trust that she's not trying to poison you. But hey, you've already been")
                            print("poisoned once.")
                            input()
                            
                            # Update storyline
                            player['ch_1'] = {'room': 'life',
                                              'outcome': 'full_reveal'}
                            player['chapter'] = 2
                            save_object(player, "player_stats.pkl")
                    
    #--------------------------------------------------------------------------------------------------------------------------        
    # A.B. Friendship        
    if life_dec1_1.upper() == "B":
        
        # Random draw
        friend_outcome = random.sample(range(100), 1)       
            
        #------------------------------------------------------------------------------------------------------------------
        # A.B1. Friendship success
        if friend_outcome < [90]:
            print()
            print("[SUCCESS]")
            print("VERONICA lets out a breath. She seems relieved at your tone of voice. She takes a few moments to think and")
            print("then chooses her words carefully.")
            input()
            print("[VERONICA]")
            print("As the crew's lead biologist - and only biologist, actually - I decided it would be worthwhile to look into")
            print("the effects of space exposure on mental acuity. I understand it's not my exact research, Commander, but")
            print("I think it could prove useful.")
            input()
            
            # Response
            print(f"[{player['name']}]".upper())
            print("A - [FRIENDSHIP] Oh, interesting! So what'd you find?")
            print()
            print("B - [INTIMIDATION] Wait, are YOU the reason I can't remember anything?")
            print("    o Success [50%]: VERONICA opens up.")
            print("    o Failure [50%]: VERONICA grows suspicious.")
            print()
            print("C - [ATTACK CARBON SCRUBBER]")
            print("    o Success [??%]: ???")
            print("    o Failure [??%]: ???")
            print()
            
            # Decision
            while life_dec1_2.upper() not in ['A', 'B', 'C']:
                life_dec1_2 = input("[CHOICE (A/B/C)]:    ")
            
            #--------------------------------------------------------------------------------------------------------------
            # A.B1.A Friendship again
            if life_dec1_2.upper() == 'A':
                print()
                print("[VERONICA]")
                print("I'm glad to hear of your interest, commander. I haven't found much yet. I'm just getting started, really...")
                input()
                
                # Response
                print(f"[{player['name']}]".upper())
                print("A - [FRIENDSHIP] You're just being modest. Let's hear it.")
                print("B - [INTIMIDATION] Why are you hiding things?")
                print()
                
                # Decision
                while life_dec1_3.upper() not in ['A', 'B']:
                    life_dec1_3 = input("[CHOICE (A/B)]:    ")
                
                #-----------------------------------------------------------------------------------------------------------------
                # A.B1.A.A Friendship
                if life_dec1_3.upper() == 'A':
                    print()
                    print("[*STORY*]")
                    print("VERONICA pauses for a few moments. She seems to be weighing something in her mind.")
                    input()
                    print("[VERONICA]")
                    print("I want to learn more about memory loss. I believe it might be a concern for the crew. I don't necessarily")
                    print("believe it's an immediate concern, but it could be something worthwhile to look into. Sometimes I find that")
                    print("I'm forgetful... today might be one of those days. I awoke with such a headache. But if you'll excuse me,")
                    print("Commander, I think I should get back to work.")
                    input()
                    
                    # End chapter
                    print("[*STORY*]")
                    print("Did she just say memory loss? Headache?? You want to press VERONICA further, but the conversation is clearly")
                    print("over. What are the odds that you awake unable to remember anything, and VERONICA is researching memory loss?")
                    print("And that she's experiencing it? Could it be... could she be the cause? You watch her for a few moments and")                    
                    print("try to imagine what an imposter would act like, but it's fruitless. You dismiss her and begin walking back to")
                    print("your quarters, lost in thought.")
                    input()
                    
                    # Update storyline
                    player['ch_1'] = {'room': 'life',
                                      'outcome': 'major_reveal'}
                    player['chapter'] = 2
                    save_object(player, "player_stats.pkl")
            
                #-----------------------------------------------------------------------------------------------------------------
                # A.B1.A.B Intimidation
                if life_dec1_3.upper() == 'B':
                    print()
                    print("[*STORY*]")
                    print("VERONICA's smile falters. That didn't seem like a good idea.")
                    input()
                    print("[VERONICA]")
                    print("Commander, I'm certainly not hiding things. I don't appreciate the accusation. If you'll excuse me, I'd")
                    print("like to get back to work. Thank you.")
                    input()
                    
                    # Update suspicion
                    player['crew_suspicion']['VERONICA'] += 1
                    print("* " * 5, "VERONICA suspicion increases by 1.", " *" * 5)
                    input()
                                        
                    # End chapter
                    print("[*STORY*]")
                    print("No luck. You want to press VERONICA further, but the conversation is clearly over. You regret losing your")
                    print("temper. You can't tell if VERONICA was actually offended, or was trying to preemptively end the conversation.")
                    print("You watch her for a few moments, trying to imagine what an imposter would act like, but it's fruitless. You")
                    print("dismiss her and begin walking back to your quarters, lost in thought.")
                    input()
                    
                    # Update storyline
                    player['ch_1'] = {'room': 'life',
                                      'outcome': 'failure'}
                    player['chapter'] = 2
                    save_object(player, "player_stats.pkl")
                
            #--------------------------------------------------------------------------------------------------------------
            # A.B1.B Intimidation
            if life_dec1_2.upper() == 'B':    
        
                # Random draw
                intimidate_outcome2 = random.sample(range(100), 1) 
        
                #---------------------------------------------------------------------------------------------------------------
                # A.B1.B1. Intimidate success
                if intimidate_outcome2 < [50]:
                    print()
                    print("[SUCCESS]")
                    print("VERONICA is shocked. She stares at you, her mouth open. After what feels like a minute, she finally")
                    print("speaks.")
                    input()
                    print("[VERONICA]")
                    print("Did you just say you can't remember anything?")
                    input()
                    print(f"[{player['name']}]".upper())
                    print("Yes.")
                    input()
                    print("[*STORY*]")
                    print("VERONICA slowly shakes her head, her eyes wide. She walks to you and begins quickly sorting through")
                    print("the articles. After a few moments, she pulls one out and skims it. She then lets out an exclamation")
                    print("and points to a paragraph buried in the appendix. When she speaks, her voice is a whisper.")
                    input()
                    print("[VERONICA]")
                    print("I think I might be onto something. We might be experiencing the effects of a nerve gas that causes")
                    print("temporary amnesia. Its strongest side effect is persistent headaches.")
                    input()
                    print("[VERONICA]")
                    print("I think I know a way to reverse the effects of the toxin. But I'll have to move quickly. Something")
                    print("tells me that if other members of the crew are experiencing amnesia, something serious is happening.")
                    print("With your permission, Commander. I should start working on this.")
                                                                    
                    # End chapter
                    print("[*STORY*]")
                    print("You dismiss VERONICA and she begins reading another article. You watch her for a few moments - you're")
                    print("brimming with questions - but she's right. You leave her to her work and begin walking back to your")
                    print("quarters. You're not sure why you told her in the heat of the moment about your amnesia, but it")
                    print("seemed to have cracked through a facade VERONICA had been upholding. Would an imposter have actually")
                    print("been surprised to hear that their nerve agent worked? Then again, whatever concoction VERONICA whips")
                    print("up, you're going to have to trust that she's not trying to poison you. But hey, you've already been")
                    print("poisoned once.")
                    input()
                    
                    # Update storyline
                    player['ch_1'] = {'room': 'life',
                                      'outcome': 'full_reveal'}
                    player['chapter'] = 2
                    save_object(player, "player_stats.pkl")
                    
                #----------------------------------------------------------------------------------------------------------------
                # A.B1.B2 Intimidate failure
                if intimidate_outcome2 >= [50]:
                    print()
                    print("[FAILURE]")
                    print("VERONICA's smile falters. She stares at you for a few moments. She's not sure what to say.")
                    input()
                    print("[VERONICA]")
                    print("Commander... I don't know where to begin. First, I don't know what you're talking about. If you are having")
                    print("difficulty remembering things, I suggest a nap. Second, I don't appreciate the accusation. I would like to")
                    print("get back to work. Thank you.")
                    input()
                    
                    # Update suspicion
                    player['crew_suspicion']['VERONICA'] += 1
                    print("* " * 5, "VERONICA suspicion increases by 1.", " *" * 5)
                    input()
                                        
                    # End chapter
                    print("[*STORY*]")
                    print("No luck. You want to press VERONICA further, but the conversation is clearly over. You regret losing your")
                    print("temper and revealing so much... what were you thinking? You can't remember... which just makes you even")
                    print("angrier. You also can't tell if VERONICA was actually offended or was just trying to preemptively end")
                    print("the conversation. You watch her for a few moments, trying to imagine what an imposter would act like,")
                    print("but it's fruitless. You dismiss her and begin walking back to your quarters, lost in thought.")
                    input()
                    
                    # Update storyline
                    player['ch_1'] = {'room': 'life',
                                      'outcome': 'failure'}
                    player['chapter'] = 2
                    save_object(player, "player_stats.pkl")                       
        
        #------------------------------------------------------------------------------------------------------------------
        # A.B2. Friendship failure
        if friend_outcome >= [90]:
            print()
            print("[FAILURE]")
            print("VERONICA hesitates. She seems to be weighing something in her mind... but then she shakes her head.")
            input()
            print("[VERONICA]")
            print("I'm sorry, commander. I was working late last night and must have forgotten to put away some reading. I really")
            print("should get back to my work.")
            input()
            
            # Response
            print(f"[{player['name']}]".upper())
            print("A - [HONESTY] Your work has to do with cerebral functioning? I don't remember that.")
            print()
            print("B - [INTIMIDATION] Why are you hiding things from me?")
            print("    o Success [50%]: VERONICA opens up.")
            print("    o Failure [50%]: VERONICA grows suspicious.")
            print()
            
            # Decision
            while life_dec1_2.upper() not in ['A', 'B']:
                life_dec1_2 = input("[CHOICE (A/B)]:    ")
            
            #--------------------------------------------------------------------------------------------------------------
            # A.B2.A Honesty
            if life_dec1_2.upper() == 'A':
                print()
                print("[*STORY*]")
                print("Your comment makes VERONICA pause. She seems to be thinking for a lot longer than you'd expect her to for")
                print("a seemingly simple question.")
                input()
                print("[VERONICA]")
                print("It's interesting that you said that, Commander. I'm the crew biologist, aren't I? It'd be natural for me")
                print("to be studying something biology-related, wouldn't it?")
                input()
                
                # Response
                print(f"[{player['name']}]".upper())
                print("A - [HONESTY] Um, sure. I don't really remember what you study anyway.")
                print()
                print("B - [INTIMIDATION] I don't like this. What's going on?")
                print("    o Success [50%]: VERONICA opens up.")
                print("    o Failure [50%]: VERONICA grows suspicious.")
                print()
                
                # Decision
                while life_dec1_3.upper() not in ['A', 'B']:
                    life_dec1_3 = input("[CHOICE (A/B)]:    ")
                    
                #---------------------------------------------------------------------------------------------------------------
                # A.B2.A.A Honesty again
                if life_dec1_3.upper() == 'A':
                    print()
                    print("[*STORY*]")
                    print("Again, VERONICA is staring at you like you're crazy. Or maybe she's the crazy one... you wonder what a confused")
                    print("robot would look like, but that's the vibe you're currently getting.")
                    input()
                    print("[VERONICA]")
                    print("I'm sorry... Commander, don't take this the wrong way, but you seem to not remember my work very well. I'm not")
                    print("saying that as an insult. Just that... well, to be honest... no, I shouldn't say anything. Well, I'll say...")
                    print("sorry, Commander. It's hard for me to think clearly. I woke up with such a headache this morning. I'm having")
                    print("a bit of a hard time focusing. But at any rate... I really should get back to work.")
                    input()
                    
                    # End chapter
                    print("[*STORY*]")
                    print("You watch VERONICA for a few moments but she doesn't want to say anything further, and it seems she even regrets")
                    print("what she already said. Did she mention that she had a headache? Could it be the same as yours...? Then again,")
                    print("wouldn't an imposter have no idea about the life of the person it was impersonating? You look at VERONICA again")
                    print("but now it's just getting awkward. You dismiss her and begin walking back to your quarters. Now that you think")
                    print("about it, you're not sure why you shared that you don't remember her work... maybe it was a bad idea to reveal")
                    print("your cards like that. We'll see what happens, you suppose...")
                    input()
                    
                    # Update storyline
                    player['ch_1'] = {'room': 'life',
                                      'outcome': 'minor_reveal'}
                    player['chapter'] = 2
                    save_object(player, "player_stats.pkl")
                
                #--------------------------------------------------------------------------------------------------------------
                # A.B2.A.B Intimidation
                if life_dec1_3.upper() == 'B':
                     
                    # Random draw
                    intimidate_outcome2 = random.sample(range(100), 1)
                
                    #----------------------------------------------------------------------------------------------------------
                    # A.B2.B1 Intimidate success
                    if intimidate_outcome2 < [50]:
                        print()
                        print("[SUCCESS]")
                        print("VERONICA looks at you for a few moments in silence. Finally, she lets out a long sigh. She closes her")
                        print("eyes and slowly rubs her forehead.")
                        input()
                        print("[VERONICA]")
                        print("I'm sorry, Commander. You... did you say you can't remember my research?")
                        input()
                        print(f"[{player['name']}]".upper())
                        print("Yes. As the commander, I have a lot of responsibilities and this slipped my mind. So please enlighten me.")
                        input()
                        print("[*STORY*]")
                        print("VERONICA pauses again for a few seconds. It seems she's weighing how much to say... but then she sighs")
                        print("again.")
                        input()
                        print("[VERONICA]")
                        print("I'm going to sound crazy, Commander, but now that I think about it, I can't for the life of me remember")
                        print("what my job title or responsibilities are.... I'm sorry, I understand this must sound crazy. I just have")
                        print("such a headache... if you don't mind, I would really like to get to my work so I can rest sooner.")
                        input()
                        
                        # End chapter
                        print("[*STORY*]")
                        print("A headache? Memory loss?? You try to question VERONICA further but she won't reveal more. She looks heartily")
                        print("embarrassed... maybe you shouldn't have been snappy. You dismiss VERONICA and she nods, wincing slightly from")
                        print("the movement, then heads to the microscope. You begin the walk back to your quarters, lost in thought.")
                        input()
                        
                        # Update storyline
                        player['ch_1'] = {'room': 'life',
                                          'outcome': 'major_reveal'}
                        player['chapter'] = 2
                        save_object(player, "player_stats.pkl")
                           
                    #----------------------------------------------------------------------------------------------------------
                    # A.B2.B2 Intimidate failure
                    if intimidate_outcome2 >= [50]:
                        print()
                        print("[FAILURE]")
                        print("VERONICA's smile falters. That didn't seem like a good idea.")
                        input()
                        print("[VERONICA]")
                        print("Commander, nothing is going on besides me not being able to work. I don't appreciate the accusation. If you'll")
                        print("excuse me, I'd like to get back to work. Thank you.")
                        input()
                        
                        # Update suspicion
                        player['crew_suspicion']['VERONICA'] += 1
                        print("* " * 5, "VERONICA suspicion increases by 1.", " *" * 5)
                        input()
                                            
                        # End chapter
                        print("[*STORY*]")
                        print("No luck. You want to press VERONICA further, but the conversation is clearly over. You regret losing your temper.")
                        print("You can't tell if VERONICA was actually offended, or was trying to preemptively end the conversation. You watch")
                        print("her for a few moments, trying to imagine what an imposter would act like, but it's fruitless. You dismiss her and")
                        print("begin walking back to your quarters, lost in thought.")
                        input()
                        
                        # Update storyline
                        player['ch_1'] = {'room': 'life',
                                          'outcome': 'failure'}
                        player['chapter'] = 2
                        save_object(player, "player_stats.pkl")              
            
            #--------------------------------------------------------------------------------------------------------------
            # A.B2.B Intimidation
            if life_dec1_2.upper() == 'B':
                
                # Random draw
                intimidate_outcome2 = random.sample(range(100), 1)
                
                #----------------------------------------------------------------------------------------------------------
                # A.B2.B1 Intimidate success
                if intimidate_outcome2 < [50]:
                    print()
                    print("[SUCCESS]")
                    print("VERONICA's eyes grow wide. She quickly looks away and her face grows red. She's... embarrassed? It takes")
                    print("her a few moments before she starts speaking again.")
                    input()
                    print("[VERONICA]")
                    print("I'm sorry, Commander. I should have been honest from the start. I... I woke up with a migraine and it")
                    print("hurts so much that I'm having a hard time thinking about anything else. I could barely remember my")
                    print("responsibilities, which is why I'm late to my post. I sincerely apologize.")
                    input()
                                                                    
                    # End chapter
                    print("[*STORY*]")
                    print("A headache? Memory loss?? You try to question VERONICA further but she won't reveal more. She looks heartily")
                    print("embarrassed... maybe you shouldn't have been snappy. You dismiss VERONICA and she nods, wincing slightly from")
                    print("the movement, then heads to the microscope. You begin the walk back to your quarters, lost in thought.")
                    input()
                    
                    # Update storyline
                    player['ch_1'] = {'room': 'life',
                                      'outcome': 'major_reveal'}
                    player['chapter'] = 2
                    save_object(player, "player_stats.pkl")
                    
                #----------------------------------------------------------------------------------------------------------
                # A.B2.B2 Intimidate failure
                if intimidate_outcome2 >= [50]:
                    print()
                    print("[FAILURE]")
                    print("VERONICA's smile falters. That didn't seem like a good idea.")
                    input()
                    print("[VERONICA]")
                    print("Commander, I'm certainly not hiding things. I don't appreciate the accusation. If you'll excuse me, I'd")
                    print("like to get back to work. Thank you.")
                    input()
                    
                    # Update suspicion
                    player['crew_suspicion']['VERONICA'] += 1
                    print("* " * 5, "VERONICA suspicion increases by 1.", " *" * 5)
                    input()
                                        
                    # End chapter
                    print("[*STORY*]")
                    print("No luck. You want to press VERONICA further, but the conversation is clearly over. You regret losing your")
                    print("temper. You can't tell if VERONICA was actually offended, or was trying to preemptively end the conversation.")
                    print("You watch her for a few moments, trying to imagine what an imposter would act like, but it's fruitless. You")
                    print("dismiss her and begin walking back to your quarters, lost in thought.")
                    input()
                    
                    # Update storyline
                    player['ch_1'] = {'room': 'life',
                                      'outcome': 'failure'}
                    player['chapter'] = 2               
                    save_object(player, "player_stats.pkl")                    
        
    #-------------------------------------------------------------------------------------------------------------------------------
    # A.C + A.B1.C Attack carbon scrubber (while VERONICA is in the room)
    if (life_dec1_1.upper() == 'C') or (life_dec1_1.upper() == 'B' and life_dec1_2.upper() == 'C'):
        
        # Random draw
        attack_outcome = random.sample(range(100), 1)
    
        #---------------------------------------------------------------------------------------------------------------------------     
        # A.C1 Attack success
        if attack_outcome < [1]:
            print()
            print("[SUCCESS]")
            print("'Nothing's wrong,' you mumble incoherently. Before VERONICA can respond, you grab a wrench from a nearby box and leap")
            print("towards the scrubber. You hit it again and again! You can barely hear VERONICA shouting over your adrenaline, and you")
            print("vaguely notice her trying to stop you, but to no avail. The outer shell of the scrubber pops off and reveals two thin")
            print("gas tanks inside. You keep hitting the tanks and barely notice that VERONICA has run out of the room, her hands over")
            print("her ears.")
            input()
            print("[*STORY*]")
            print("With one particularly vigorous swing, you momentarily hear a high-pitched whine before the tank explodes. Your vision")
            print("and hearing go, and the room starts to fill with smoke. As you slip into unconsciousness, you're strangely satisfied.")
            print("Try getting out of this one, imposter...")
            input()
            print()
            print()
            print()
            print("                                            [YOUR QUEST COMES TO AN END]")
            print("                                                     Ending #1")
            print()
            print("                                                      OUTCOMES:")
            print(f"                                                 - {player['name'].upper()} dies")
            print("                                                 - BENJAMIN dies")
            print("                                                 - VERONICA dies")
            print("                                                 - SHIP AI dies")
            print()
            print("                                                       CAUSE:")
            print("                                         Explosion from pressurized air tank")
            
            # Update n_completions.pkl
            if 'n_completions.pkl' in os.listdir():
                n_completions = pickle.load(open('n_completions.pkl', 'rb'))              
                n_completions += 1
                
                save_object(n_completions, "n_completions.pkl")
                
            else:
                n_completions = 1
                save_object(n_completions, "n_completions.pkl")
            
            quit()
        
        #---------------------------------------------------------------------------------------------------------------------------
        # A.C2. Attack failure
        if attack_outcome >= [1]:
            print()
            print("[FAILURE]")
            print("'Nothing's wrong,' you mumble incoherently. Before VERONICA can respond, you grab a wrench from a nearby box and leap")
            print("towards the scrubber. You hit it again and again! You can barely hear VERONICA shouting over your adrenaline, until")
            print("suddenly she hits you in the head with something heavy and metallic. Your adrenaline could cover the gunshots of pain")
            print("your headache gave you with each clang of the wrench against the scrubber's metal plate, but a hit to the head is too")
            print("much. You slump to the ground and quickly lose consciousness.")
            input()
            
            # Update suspicion
            player['crew_suspicion']['VERONICA'] += 3
            print("* " * 5, "VERONICA suspicion increases by 3.", " *" * 5)
            input()
                                
            # Update storyline
            player['ch_1'] = {'room': 'life',
                              'outcome': 'massive_failure'}
            player['chapter'] = 2
            save_object(player, "player_stats.pkl")

#-----------------------------------------------------------------------------------------------------------------------------------
# B. Destroy carbon scrubber
if life_dec1.upper() == 'B':
    print()
    print("[*STORY*]")
    print("For such a critical component of the ship, the carbon scrubber is remarkably poorly defended. Probably because the designers")
    print("didn't consider animosity from the crew... You pull a pipette tip from one of the drawers and with a few well-placed pushes,")
    print("the outer shell of the scrubber pops off. Inside is a mess of pipes and two thin gas tanks, both incredibly cold.")
    input()
    
    # Response
    print(f"[{player['name']}]".upper())
    print("A - Unscrew one of the tanks.")
    print("B - Just start hitting stuff.")
    print()
    
    # Decision
    while life_dec1_1.upper() not in ['A', 'B']:
        life_dec1_1 = input("[CHOICE (A/B)]:    ")
        
    #------------------------------------------------------------------------------------------------------------------------
    # B.A. Unscrew one of the tanks
    if life_dec1_1.upper() == 'A':
        print()
        print("[*STORY*]")
        print("You begin unscrewing the tank, but it's secured surprisingly tightly. You glance around the room and spot a wrench in")
        print("a box in the corner. You grab it and start working on the screws.")
        input()
        print("[*STORY*]")
        print("As the screws start to give way, you momentarily hear a high-pitched whine before the tank explodes. Your vision and")
        print("hearing go, and as the room starts to fill with smoke and you slip into unconsciousness, you wonder why you thought")
        print("this was a good idea...")
        input()
        print()
        print()
        print()
        print()
        print("                                            [YOUR QUEST COMES TO AN END]")
        print("                                                     Ending #1")
        print()
        print("                                                      OUTCOMES:")
        print(f"                                                 - {player['name'].upper()} dies")
        print("                                                 - BENJAMIN dies")
        print("                                                 - VERONICA dies")
        print("                                                 - SHIP AI dies")
        print()
        print("                                                       CAUSE:")
        print("                                         Explosion from pressurized air tank")
        
        # Update n_completions.pkl
        if 'n_completions.pkl' in os.listdir():
            n_completions = pickle.load(open('n_completions.pkl', 'rb'))              
            n_completions += 1
            
            save_object(n_completions, "n_completions.pkl")
            
        else:
            n_completions = 1
            save_object(n_completions, "n_completions.pkl")
            
        quit()
    #-------------------------------------------------------------------------------------------------------------------------
    # B.B. Start hitting stuff
    if life_dec1_1.upper() == 'B':
        print()
        print("[*STORY*]")
        print("Screw it, life is short. Let's make it shorter. You glance around the room and spot a wrench in a box in the corner.")
        print("You grab it and start hitting the tanks and shouting like a crazy person. Which you are.")
        input()
        print("[*STORY*]")
        print("With one particularly vigorous swing, you momentarily hear a high-pitched whine before the tank explodes. Your vision")
        print("and hearing go, and the room starts to fill with smoke. As you slip into unconsciousness, you're strangely satisfied.")
        print("Try getting out of this one, imposter...")
        input()
        input(".")
        input(".")
        input(".")
        print()
        print("                                            [YOUR QUEST COMES TO AN END]")
        print("                                                     Ending #1")
        print()
        print("                                                      OUTCOMES:")
        print(f"                                                 - {player['name'].upper()} dies")
        print("                                                 - BENJAMIN dies")
        print("                                                 - VERONICA dies")
        print("                                                 - SHIP AI dies")
        print()
        print("                                                       CAUSE:")
        print("                                         Explosion from pressurized air tank")
        
        # Update n_completions.pkl
        if 'n_completions.pkl' in os.listdir():
            n_completions = pickle.load(open('n_completions.pkl', 'rb'))              
            n_completions += 1
            
            save_object(n_completions, "n_completions.pkl")
            
        else:
            n_completions = 1
            save_object(n_completions, "n_completions.pkl")
            
        quit()
            
            
