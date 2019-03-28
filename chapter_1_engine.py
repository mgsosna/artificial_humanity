########################################################################################################
# ARTIFICIAL HUMANITY
# Chapter 1a: engine room
#
# Matt Grobis
########################################################################################################
import pickle
import time
from custom_functions import *
import random

player = pickle.load(open('player_stats.pkl', 'rb'))

print()
print(
'''[*STORY*]
You holster your laser knife and exit your quarters. The door slides and locks behind you. You are in a well-lit
white hallway. As you walk towards the engine room, the hallway gradually changes to metallic, pipes overhead and
metal grating on the floor and walls. A crew of three is hardly enough to finance fancy white panelling for the
entire ship, you suppose. The door to the engine room opens as you approach and you see BENJAMIN working. He is
wearing the standard mechanic attire - dark green pants and light green shirt. While most of his hair has balded
off already, the little that remains is brown.''')
input()
print("[*STORY*]")
print("BENJAMIN appears distracted and hasn't noticed you; he is hunched over something.")
input()

print(f"[{player['name']}]".upper())
print("A - [QUIETLY APPROACH BENJAMIN TO SEE WHAT HE'S DOING]")
print()
print("B - [SAY HELLO AND START A CONVERSATION]")
print()
print("C - [ATTACK BENJAMIN]")
print()

# Initialize choices
eng_dec1 = ""
eng_dec1_1 = ""
eng_dec1_2 = ""

# These choices can be reached in multiple ways
talk = False
attack = False

while eng_dec1.upper() not in ['A', 'B', 'C']:
    eng_dec1 = input("[CHOICE (A/B/C)]:    ")

# If decide to attack or say hello, set those variables
if eng_dec1.upper() == 'B':
    talk = True

if eng_dec1.upper() == 'C':
    attack = True

###########################################################################################################################################
###########################################################################################################################################
###########################################################################################################################################
# A. Quietly approach Benjamin
if eng_dec1.upper() == "A":
    print()
    print(
    '''[*STORY*]
    You step carefully towards BENJAMIN, hiding behind machinery as you squint at what he's holding. It appears to be
    some sort of tablet that he's reading... though it is hard to tell.''')
    input()

    # Try to sneak further, say hello, or attack
    print(f"[{player['name']}]".upper())
    print("A - [GET CLOSER FOR A BETTER VIEW]")
    print("    o Success [75%]: read the tablet.")
    print("    o Failure [25%]: BENJAMIN realizes you snuck up on him.")
    print("B - [SAY HELLO AND START A CONVERSATION]")
    print("C - [ATTACK BENJAMIN]")
    print()

    # Choice
    eng_dec1_1 = ""
    while eng_dec1_1.upper() not in ['A', 'B', 'C']:
        eng_dec1_1 = input("[CHOICE (A/B/C)]:   ")

    # If choice is to talk or attack, set those variables to True
    if eng_dec1_1.upper() == 'B':
        talk = True

    if eng_dec1_1.upper() == 'C':
        attack = True

    #------------------------------------------------------------------------------------------------------------------------
    # A.A. Attempt to sneak further
    if eng_dec1_1.upper() == "A":

        # Random draw
        sneak_outcome = random.sample(range(100), 1)

        #---------------------------------------------------------------------------------------------------------------------
        # A.A1. Failure
        if sneak_outcome < [25]:
            print()
            print(
            '''[FAILURE]
            You step on a loose wrench, which echoes in the room. BENJAMIN spins around, his eyes wide in alarm. The
            tablet instantly goes blank.''')
            input()

            # Increase Benjamin suspicion
            player['crew_suspicion']['BENJAMIN'] += 1
            print("* " * 5, "BENJAMIN suspicion increases by 1.", " *" * 5)
            input()

            # Benjamin responds
            print("[BENJAMIN]")
            print(f"Commander {player['name']}! What are you doing?")
            print()

            # Commander responds
            print(f"[{player['name']}]".upper())
            print("BENJAMIN. I - I just came here to inspect the engines. To check on you. To check on the engines, I mean.")
            input()

            print(
            '''[*STORY*]
            The conversation continues awkwardly for another minute before you excuse yourself. You stand outside the
            the engine room for a few moments before silently heading back to your quarters.''')
            input()

            # Update storyline
            player['ch_1'] = {'room': 'engine',
                              'outcome': 'failure'}
            player['chapter'] = 2
            save_object(player, "player_stats.pkl")

        #------------------------------------------------------------------------------------------------------------------------
        # A.A2. Success
        if sneak_outcome >= [75]:
            print()
            print(
            '''[SUCCESS]
            You carefully avoid stepping on a loose wrench as you tiptoe around BENJAMIN. You look over his shoulder and see...
            BENJAMIN's profile. He is looking at information about himself, his hometown and travel logs. He seems concerned
            and confused.''')
            input()

            # Commander talks to him
            print(f"[{player['name']}]".upper())
            print("BENJAMIN. Is everything ok?")
            input()

            # BENJAMIN nervous
            print(
            f'''[BENJAMIN]
            Commander {player['name']}! I didn't hear you there. I'm sorry. I'm just... I just confused. I woke up with a
            headache. Nothing I can't handle, though, Commander.''')
            input()

            # You respond
            print(
            '''[*STORY*]
            Headache?? Just like you had a headache this morning? You're about to speak but it looks like he's weighing
            whether or not to say something. He can tell you saw him reading his own files. You let the silence stretch on
            until he finally starts talking.''')
            input()

            # BENJAMIN reveals he has amnesia
            print(
            '''[BENJAMIN]
            Sorry, Commander, I... I'm not feeling well. My... my headache is so bad that it's messing with my head. I'm
            having a hard time remembering things. But I promise it won't interfere with my work.''')
            input()

            print(
            '''[*STORY*]
            Headache *and* amnesia?? Your stomach turns. You press BENJAMIN for more details but he seems embarassed and
            doesn't want to elaborate. As far as you can tell, there is no alcohol or intoxicants on the ship, and
            communications with Earth are too limited for him to have been up late about something there. Maybe his memory
            has also been erased? You would ask him facts about himself to test him but you can't remember any facts about
            him, either... could he be the imposter? It's hard to tell, but it doesn't seem like it. You talk absently for a
            few moments before you excuse yourself and return to your quarters, lost in thought.''')

            # Update storyline
            player['ch_1'] = {'room': 'engine',
                              'outcome': 'major_reveal'}
            player['chapter'] = 2
            save_object(player, "player_stats.pkl")

###########################################################################################################################################
###########################################################################################################################################
###########################################################################################################################################
# B. Talk to BENJAMIN
# - This can occur immediately (eng_dec1 == 'B') or after trying to quietly approach Benjamin (eng_dec1 == 'A')
if talk == True:

    # Commander talks to him
    print()
    print(f"[{player['name']}]".upper())
    print("BENJAMIN. How are you?")
    input()

    # Benjamin responds
    print("[BENJAMIN]")
    print(f"Commander {player['name']}. Things are, uh, well. Nominal.")
    input()

    print("[*STORY*]")
    print("BENJAMIN looks nervous. His eyes keep darting to a tablet on the table, and he awkwardly fumbles to turn it off.")
    print("He coughs and winces slightly.")
    input()

    # Conversation options
    print(f"[{player['name']}]".upper())
    print("A - [INTIMIDATION] You better tell me what's going on.")
    print("    o Success [50%]: BENJAMIN spills the beans.")
    print("    o Failure [50%]: BENJAMIN gets defensive and suspicious.")
    print()
    print("B - [FRIENDSHIP] Are you feeling ok?")
    print("    o Success [75%]: BENJAMIN tells part of the story.")
    print("    o Failure [25%]: BENJAMIN doesn't share much.")
    print()
    print("C - [HONESTY] There's an imposter on board posing as a human. Is it you?")
    print("    o Success [1%]:  ???")
    print("    o Failure [99%]: ???")
    print()
    print("D - [ATTACK BENJAMIN]")
    print()

    # Decision
    eng_dec1_2 = ""
    while eng_dec1_2.upper() not in ['A', 'B', 'C', 'D']:
        eng_dec1_2 = input("[CHOICE (A/B/C/D)]:   ")

    # If decide to attack, set that variable to True
    if eng_dec1_2.upper() == 'D':
        attack = True

    #----------------------------------------------------------------------------------------------------------------
    # B.A. Intimidation
    if eng_dec1_2.upper() == "A":

        # Random draw
        intimidate_outcome = random.sample(range(100), 1)

        # B.A1. Failure
        if intimidate_outcome >= [50]:
            print()
            print("[FAILURE]")
            print("BENJAMIN is startled by your anger... but his face turns red and he clenches his fists.")
            input()
            print("[BENJAMIN]")
            print("Commander, I apologize but I don't think I deserve that tone of voice. I'm - I - I need to - I'm sorry but I need")
            print("to get back to work.")

            # Update suspicion
            player['crew_suspicion']['BENJAMIN'] += 1
            print("* " * 5, "BENJAMIN suspicion increases by 1.", " *" * 5)
            input()

            # Update storyline
            player['ch_1'] = {'room': 'engine',
                              'outcome': 'failure'}
            player['chapter'] = 2
            save_object(player, "player_stats.pkl")

        #------------------------------------------------------------------------------------------------------------
        # B.A2. Success
        if intimidate_outcome < [50]:
            print()
            print("[SUCCESS]")
            print("BENJAMIN is startled by your anger. He stumbles back and stutters, struggling to find his words.")
            input()
            print("[BENJAMIN]")
            print("I, I... I'm sorry, Captain. I'm not feeling like myself. I just have such a headache. But... I promise this won't")
            print("impact my work.")
            input()

            # Push BENJAMIN a little further
            print(f"[{player['name']}]".upper())
            print("A - [INTIMIDATION] You're acting this strange because of a headache?")
            print("    o Success [80%]: BENJAMIN tells you everything.")
            print("    o Failure [20%]: BENJAMIN grows defensive and suspicious.")
            print()
            print("B - [FRIENDSHIP] A headache? What happened?")
            print()

            eng_dec1_3 = ""
            # Decision
            while eng_dec1_3.upper() not in ['A', 'B']:
                eng_dec1_3 = input("[CHOICE (A/B)]:    ")

            # B.A2.A. Intimidate again
            if eng_dec1_3.upper() == 'A':

                # Random draw
                intimidate_outcome2 = random.sample(range(100), 1)

                #-----------------------------------------------------------------------------------------------------------------
                # B.A2.A1. Success
                if intimidate_outcome2 < [80]:
                    print()
                    print("[SUCCESS]")
                    print("BENJAMIN visibly begins to sweat. You can't remember if you're a tough commander or not... when this is all")
                    print("over, you should try intimidation more often.")
                    input()
                    print("[BENJAMIN]")
                    print("Captain. I sincerely apologize. I - I know this sounds crazy, but I have such a headache. I can't...")
                    input()
                    print("[BENJAMIN]")
                    print("My head hurts so bad I can't remember anything. It's just a fog. I don't know why. But I promise you. It won't")
                    print("affect my work.")
                    input()

                    # End chapter
                    print("[*STORY*]")
                    print("BENJAMIN is beet red at this point and mumbles about wanting to get back to work. You permit him and then begin")
                    print("the walk back to your quarters. BENJAMIN's headache sounds just like yours this morning. As far as you can tell,")
                    print("there is no alcohol or intoxicants on the ship, so he can't have a hangover. His headache is strange, indeed...")
                    print("but his words about being unable to remember anything - just like you - make your skin crawl.")
                    input()

                    # Update storyline
                    player['ch_1'] = {'room': 'engine',
                                      'outcome': 'major_reveal'}
                    player['chapter'] = 2
                    save_object(player, "player_stats.pkl")

                #-----------------------------------------------------------------------------------------------------------------
                # B.A2.A2. Failure
                if intimidate_outcome2 >= [80]:
                    print()
                    print("[FAILURE]")
                    print("BENJAMIN frowns.")
                    input()
                    print("[BENJAMIN]")
                    print("Captain, I'm sorry but I'm just not feeling well. This won't impact my work. With respect... I don't understand")
                    print("the aggression towards me. May I get back to work and do my job?")
                    input()

                    # End chapter
                    print("[*STORY*]")
                    print("Part of you feels like making BENJAMIN do push-ups, but you can't remember if that's what you would normally do...")
                    print("or if commanders normally do... lost in thought, it takes you a few moments to realize that BENJAMIN is staring at")
                    print("you. You dismiss him and slowly begin the walk back to your quarters. BENJAMIN's headache sounds just like yours")
                    print("from this morning. As far as you can tell, there is no alcohol or intoxicants on the ship, so he can't have a")
                    print("hangover. You wish you could have gotten more information... but it seems you pushed him too far.")
                    input()

                    # Update suspicion
                    player['crew_suspicion']['BENJAMIN'] += 1
                    print("* " * 5, "BENJAMIN suspicion increases by 1.", " *" * 5)
                    input()

                    # Update storyline
                    player['ch_1'] = {'room': 'engine',
                                      'outcome': 'minor_reveal'}
                    player['chapter'] = 2
                    save_object(player, "player_stats.pkl")

            #-------------------------------------------------------------------------------------------------------------------
            # B.A2.B. Friendly
            if eng_dec1_3.upper() == 'B':
                print()
                print("[*STORY*]")
                print("BENJAMIN relaxes a little.")
                input()
                print("[BENJAMIN]")
                print("Yes, captain. I'm sorry. Nothing I can't handle. I just woke up this morning with such a headache. You know as")
                print("well as I do that there's nothing to drink on the ship! So I don't know how it happened. My memory's a little")
                print("hazy... but it'll come back to me. I think I'm feeling better already.")
                input()

                # End chapter
                print("[*STORY*]")
                print("Headache? Hazy memory?? That sounds uncomfortably like what you were feeling this morning... and still continue")
                print("to feel. You make some idle chat with BENJAMIN for a minute before dismissing him and slowly beginning the walk")
                print("back to your quarters. Having a hazy memory sure sounds like something an imposter would say... but on second")
                print("thought, you're not sure.")
                input()

                # Update storyline
                player['ch_1'] = {'room': 'engine',
                                  'outcome': 'major_reveal'}
                player['chapter'] = 2
                save_object(player, "player_stats.pkl")

    #-------------------------------------------------------------------------------------------------------------------
    # B.B. Friendly straight away
    if eng_dec1_2.upper() == 'B':

        # Random draw
        friendly_outcome = random.sample(range(100), 1)

        # B.B1. Failure
        if friendly_outcome < [25]:
            print()
            print("[FAILURE]")
            print("BENJAMIN stiffens a little.")
            input()
            print("[BENJAMIN]")
            print("I'm sorry, captain. Just a little out of it. Going to get back to work now, if that's ok. Thank you, though.")
            input()

            # End chapter
            print("[*STORY*]")
            print("Your friendliness didn't seem to work. You watch BENJAMIN for a minute while he works - his movements seem mostly")
            print("normal, but he's a little more rigid than you'd expect. More... tender? Disorganized? Whatever it is, something")
            print("doesn't seem quite right. You excuse yourself and walk back to your quarters, lost in thought.")
            input()

            # Update storyline
            player['ch_1'] = {'room': 'engine',
                              'outcome': 'failure'}
            player['chapter'] = 2
            save_object(player, "player_stats.pkl")

        #---------------------------------------------------------------------------------------------------------------------
        # B.B2. Success
        if friendly_outcome >= [25]:
            print()
            print("[*STORY*]")
            print("BENJAMIN relaxes a little.")
            input()
            print("[BENJAMIN]")
            print("Yes, captain. I'm sorry. Nothing I can't handle. I just woke up this morning with such a headache. You know as")
            print("well as I do that there's nothing to drink on the ship! So I don't know how it happened.")
            input()

            # End chapter
            print("[*STORY*]")
            print("A headache? You make some idle chat with BENJAMIN for a few minutes before dismissing him and slowly beginning")
            print("the walk back to your quarters. BENJAMIN's headache sounds just like yours from this morning... and he wasn't")
            print("kidding about how there's nothing to drink on the ship. So maybe he's telling the truth about his headache...")
            print("hard to tell.")
            input()

            # Update storyline
            player['ch_1'] = {'room': 'engine',
                              'outcome': 'minor_reveal'}
            player['chapter'] = 2
            save_object(player, "player_stats.pkl")

    #----------------------------------------------------------------------------------------------------------------
    # B.C. Honesty
    if eng_dec1_2.upper() == "C":

        # Random draw
        earnest_outcome = random.sample(range(100), 1)

        # B.C1. Success
        if earnest_outcome < [1]:
            print()
            print("[SUCCESS]")
            print("BENJAMIN's eyes go wide. He mouthes a few words silently before turning away and rubbing his forehead.")
            input()
            print("[BENJAMIN]")
            print("Commander. Wow. I... I've actually been worried about the same thing. I can't remember anything. My head hurts")
            print("so much. But I *know* I have a file on my tablet about...")
            input()
            print("[*STORY*]")
            print("BENJAMIN pauses, his eyes glancing around. He leans in close to you and begins to whisper.")
            input()
            print("[BENJAMIN]")
            print("I think we have to be really careful on this ship. Be very, very careful with what you say aloud. The ship - it")
            print("listens. And I don't think it means us well.")
            input()

            # End chapter
            print("[*STORY*]")
            print("BENJAMIN laughs nervously and then makes some idle chat for a few minutes. His voice seems strained. Could he")
            print("really mean what he said? How would he know? You search your memory but as usual, it comes up empty-handed.")
            print("If you can't trust the Ship AI... you dismiss BENJAMIN and walk slowly back to your quarters.")
            input()

            # Update storyline
            player['ch_1'] = {'room': 'engine',
                              'outcome': 'full_reveal'}
            player['chapter'] = 2
            save_object(player, "player_stats.pkl")

        #-----------------------------------------------------------------------------------------------------------------
        # B.C2. Failure
        if earnest_outcome >= [1]:
            print()
            print("[FAILURE]")
            print("BENJAMIN's eyes go wide for a moment... but then the moment passes and he regains his composure.")
            input()
            print("[BENJAMIN]")
            print("Commander. Of all the things I was expecting you to say, that wasn't one of them. I really should get back")
            print("to work...")
            input()
            print("[*STORY*]")
            print("BENJAMIN pauses for a few moments, like he's debating something. His eyes search you before he shrugs.")
            input()
            print("[BENJAMIN]")
            print("All I'll say is that we should keep our heads down, do our work, and we'll soon be home. Never know who might")
            print("be listening in on us... Headquarters, State. Maybe even aliens!")
            input()

            # Try one more time
            print(f"[{player['name']}]".upper())
            print("A - [HONESTY] Wait, what do you mean? Tell me, please.")
            print("    o Success [33%]: BENJAMIN spills the beans.")
            print("    o Failure [67%]: BENJAMIN keeps his distance.")
            print()
            print("B - [FRIENDSHIP] Aliens? Haha come on, BENJAMIN.")
            print("    o Success [50%]: BENJAMIN tells you a little more.")
            print("    o Failure [50%]: BENJAMIN keeps his distance.")
            print()

            eng_dec1_2_1 = ""

            # Decision
            while eng_dec1_2_1.upper() not in ['A', 'B']:
                eng_dec1_2_1 = input("[CHOICE (A/B)]:    ")

            #-----------------------------------------------------------------------------------------------
            # B.C2.A. Honesty
            if eng_dec1_2_1.upper() == "A":

                # Random draw
                earnest_outcome2 = random.sample(range(100), 1)

                #--------------------------------------------------------------------------------------------------------------
                # B.C2.A1. Success
                if earnest_outcome2 < [33]:
                    print()
                    print("[SUCCESS]")
                    print("BENJAMIN's cocky smile fades a little. He glances around and then leans in.")
                    input()
                    print("[BENJAMIN]")
                    print("Commander. When I woke up this morning, I couldn't remember anything... and my head hurt like nothing else. I")
                    print("have to admit... I'm not even quite sure who you are... captain. I think we should be very careful with what")
                    print("we say aloud. The ship - it listens. And I don't think it means us well.")
                    input()

                    # End chapter
                    print("[*STORY*]")
                    print("BENJAMIN laughs nervously and then makes some idle chat for a few minutes. His voice seems strained. Could he")
                    print("really mean what he said? How would he know? You search your memory but as usual, it comes up empty-handed. If")
                    print("you can't trust the Ship AI... you dismiss BENJAMIN and walk slowly back to your quarters, lost in thought.")
                    input()

                    # Update storyline
                    player['ch_1'] = {'room': 'engine',
                                      'outcome': 'full_reveal'}
                    player['chapter'] = 2
                    save_object(player, "player_stats.pkl")

                #---------------------------------------------------------------------------------------------------------------
                # B.C2.A2. Failure
                if earnest_outcome2 >= [33]:
                    print()
                    print("[FAILURE]")
                    print("BENJAMIN smirks and looks away. After a few moments, he speaks again.")
                    input()
                    print("[BENJAMIN]")
                    print("Commander, I have a lot of work to do, and my head hurts like nothing else. Would it be alright if I returned")
                    print("to it?")
                    input()

                    # End chapter
                    print("[*STORY*]")
                    print("A headache? Could that be like yours? You watch him for a few moments but the conversation is clearly over.")
                    print("You dismiss BENJAMIN. You can't tell if you're frustrated or disappointed... being earnest as a commander")
                    print("is always a gamble, but it had felt worth it with him. As he returns to work, you notice he's wincing")
                    print("slightly as he works, his eyes occasionally squinting at his bench. Some headache, indeed... you walk back to")
                    print("your quarters, lost in thought.")
                    input()

                    # Update storyline
                    player['ch_1'] = {'room': 'engine',
                                      'outcome': 'minor_reveal'}
                    player['chapter'] = 2
                    save_object(player, "player_stats.pkl")

            #---------------------------------------------------------------------------------------------------------------------------
            # B.C2.B. Friendship
            if eng_dec1_2_1.upper() == "B":

                # Random draw
                friendly_outcome2 = random.sample(range(100), 1)

                #---------------------------------------------------------------------------------------------------------------
                # B.C2.B1. Success
                if friendly_outcome2 < [50]:
                    print()
                    print("[SUCCESS]")
                    print("BENJAMIN's cocky smile fades into a more genuine one. He shrugs, glances around, and then leans in.")
                    input()
                    print("[BENJAMIN]")
                    print("Commander. Just a word of caution, one, er, friend to another. Speaking as colleagues... I've got a bit of a")
                    print("headache, that's all. Can't remember how I got it. Promise it's not any booze... you know as well as I do that")
                    print("there's nothing to drink on the ship.")
                    input()

                    # End chapter
                    print("[*STORY*]")
                    print("BENJAMIN laughs and then makes some idle chat for a few minutes. He does look like he has a headache; he winces")
                    print("every now and then while he's talking. His headache sounds a bit like what you had this morning... but how could")
                    print("he not remember how we got it? You dismiss BENJAMIN and walk slowly back to your quarters, lost in thought.")
                    input()

                    # Update storyline
                    player['ch_1'] = {'room': 'engine',
                                      'outcome': 'minor_reveal'}
                    player['chapter'] = 2
                    save_object(player, "player_stats.pkl")

                #-------------------------------------------------------------------------------------------------------------------
                # B.C2.B2. Failure
                if friendly_outcome2 >= [50]:
                    print()
                    print("[FAILURE]")
                    print("The friendly overture just causes BENJAMIN to inch away slowly. Are you really that awkward?")
                    input()
                    print("[BENJAMIN]")
                    print("Commander, uh... I have a lot of work to do. Would you mind if I got back to it?")
                    input()

                    # End chapter
                    print("[*STORY*]")
                    print("You dismiss BENJAMIN. You can't tell if you're frustrated or disappointed... being friendly as a commander is")
                    print("always a gamble, but it had felt worth it with him. There's no point trying to say anything further; the moment")
                    print("is already awkward enough. You walk slowly back to your quarters... awkwardly.")
                    input()

                    # Update storyline
                    player['ch_1'] = {'room': 'engine',
                                      'outcome': 'failure'}
                    player['chapter'] = 2
                    save_object(player, "player_stats.pkl")

###########################################################################################################################################
###########################################################################################################################################
###########################################################################################################################################
# C. Attack BENJAMIN
# - This can occur these ways:
#    o Immediately (eng_dec1 == 'C')
#    o After trying to quietly approach BENJAMIN (eng_dec1 == 'A', eng_dec1_1 == 'C')
#    o After talking to BENJAMIN (eng_dec1 == 'B', eng_dec1_2 == 'D')
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
    print("You grab his tablet and try to open it, but it's impossible to unlock. It won't budge for you; it really needs to")
    print("be BENJAMIN. Unless...")
    input()
    print("[*STORY*]")
    print("You reach down and grab one of BENJAMIN's hands, the one that you sliced off in the melee. You put his index")
    print("finger on the fingerprint scanner and the tablet lights up.")
    input()
    print("[*STORY*]")
    print("Below you are the files BENJAMIN was looking at when you came in. It's his personal log, the file from StarFleet.")
    print("It's information about himself, things that he should obviously have known. Hometown. StarFleet division. Years of")
    print("education and awards and degrees. Why would he have been looking at this?")
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

    # C.A. Lock the door
    if room_dec.upper() == 'A':
        print()
        print("[*STORY*]")
        print("You go to the control panel by the door and enter administrative mode. A few moments of tapping on the screen")
        print("and the door closes quietly with a hiss. You hear the grinding of the bolts securing the door in place. No")
        print("one's getting in. You smile slightly and head back to your quarters.")
        input()

        # Update storyline
        player['ch_1'] = {'room': 'engine',
                          'outcome': 'kill_lock'}
        player['chapter'] = 2
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
        player['ch_1'] = {'room': 'engine',
                          'outcome': 'kill_hide'}
        player['chapter'] = 2
        save_object(player, "player_stats.pkl")

    #------------------------------------------------------------------------------------------------------------------------
    # C.C. Do nothing
    if room_dec.upper() == 'C':
        print()
        print("[*STORY*]")
        print("You shrug. Whatever. You walk back to your quarters and hum a cheerful tune.")
        input()

        # Update storyline
        player['ch_1'] = {'room': 'engine',
                          'outcome': 'kill_nothing'}
        player['chapter'] = 2
        save_object(player, "player_stats.pkl")
