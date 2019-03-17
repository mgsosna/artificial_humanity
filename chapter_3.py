########################################################################################################
# ARTIFICIAL HUMANITY
# Chapter 3: finale
#
# Matt Grobis
########################################################################################################
# Load modules
import pickle
import time
from custom_functions import *
import os

# Set global variables
susp_spaces = 30
susp_stars = 8

binary_length = 20
binary_spaces = susp_spaces+1
binary_rows = 5
binary_sleep = 1

# Load player info
player = pickle.load(open('player_stats.pkl', 'rb'))

# Print binary
print()
scrolling_binary(screen_size=binary_length, n_spaces=binary_spaces, n_rows=binary_rows, time_sleep=binary_sleep)

# Display start of chapter two
print()
print(" " * (susp_spaces-6), "*" * 51)
print(" " * (susp_spaces-6), "*" * 20, "CHAPTER 3", "*" * 20)
print(" " * (susp_spaces-6), "*" * 51)
input()

###################################################################################################################################
# The possibilities up to this point:

# BENJAMIN posibilities:
# - You killed him
# - Know he has headache
# - Know he has headache + amnesia
# - Know he has headache + amnesia + not to trust SHIP

# VERONICA possibilities:
# - Know she has headache
# - Know she has headache + amnesia
# - Know she has headache + amnesia + working on antidote



# To keep things simple, we'll summarize the paths into discrete states

distrust_ship = False
all_headaches = False
all_amnesia   = False
antidote      = False
wait          = False
mixed_info    = True    # If you got some weird combination (e.g. Failure + Full_reveal, you're just confused)
team_signal   = False

end_state = 'default'

# You're a killer
# - Trust SHIP. Never heard of reason to not trust SHIP
if player['ch_1']['outcome'] in ['kill_hide', 'kill_lock']:
    end_state = 'killer_first'
    mixed_info = False

elif player['ch_2']['outcome'] in ['kill_hide', 'kill_lock']:
    end_state = 'killer_second'
    mixed_info = False

# You totally failed at getting any info
if player['ch_1']['outcome'] == 'failure' and player['ch_2']['outcome'] == 'failure':
    end_state = 'failure'
    mixed_info = False

# You know everyone has headaches
if player['ch_1']['outcome'] == 'minor_reveal' and player['ch_2']['outcome'] in ['minor_reveal', 'major_reveal']:
    all_headaches = True
    mixed_info = False

if player['ch_1']['outcome'] in ['minor_reveal', 'major_reveal'] and player['ch_2']['outcome'] == 'minor_reveal':
    all_headaches = True
    mixed_info = False

# You know everyone has headaches + amnesia
if player['ch_1']['outcome'] == 'major_reveal' and player['ch_2']['outcome'] == 'major_reveal':
    all_amnesia = True
    mixed_info = False

# You know not to trust SHIP
if (player['ch_1']['room'] == 'engine' and player['ch_1']['outcome'] == 'full_reveal') or (player['ch_2']['room'] == 'engine' and player['ch_2']['outcome'] == 'full_reveal'):
    distrust_ship = True
    mixed_info = False

# You know VERONICA is working on antidote
if (player['ch_1']['room'] == 'life' and player['ch_1']['outcome'] == 'full_reveal') or (player['ch_2']['room'] == 'life' and player['ch_2']['outcome'] == 'full_reveal'):
    antidote = True
    mixed_info = False

# If both full_reveals, then the team signals to you to meet them at Zone D
if distrust_ship == True and antidote == True:
    team_signal = True

####################################################################################################################################
# Chapter start: you're walking towards your quarters

# All headaches - can't escape going to room (but will have additional dialogue option in room)
if all_headaches == True:
    print("[*STORY*]")
    print("Your footsteps are slow, thoughtful as you walk towards your quarters. From your conversations with BENJAMIN and")
    print("VERONICA, you know that both of them had headaches this morning... just like you. Somehow, all crew members awoke")
    print("with migraines. You're not sure what to do with that information, though... maybe SHIP will know.")
    input()

# Mix of info - can't escape going to room
if mixed_info == True:
    print("[*STORY*]")
    print("Your footsteps are slow, thoughtful as you walk towards your quarters. You thought that talking to BENJAMIN and")
    print("VERONICA would clarify things, but you're somehow just more confused now. You're not sure what to do... maybe SHIP")
    print("will know.")

# Killer - can't escape going to room
if end_state in ['killer_first', 'killer_second']:
    print("[*STORY*]")
    print("Your footsteps are purposeful, brisk as you walk towards your quarters. Head high, back straight... presentation")
    print("is important, after all, even if half your crew is lying in pieces in the engine room.")
    input()

# Failure - can't escape going to room
if end_state == 'failure':
    print("[*STORY*]")
    print("Your footsteps are slow, disappointed as you walk towards your quarters. Despite your efforts, there's not much to")
    print("think about. Your conversations with BENJAMIN and VERONICA yielded nothing. You truly don't know how to talk to")
    print("people, it seems. Hopefully SHIP will have answers.")
    input()

#--------------------------------------------------------------
# Major reveal: you have the option of... inputting a place to go? There's a chance you guess correctly? This sounds way too broad..
if all_amnesia == True:
    print("[*STORY*]")
    print("Your footsteps are slow, thoughtful as you walk towards your quarters. You are thoroughly disturbed - you know that")
    print("everyone on the ship awoke this morning with headaches... and SHIP is almost out of time for fighting off the hack.")
    print("How could it have come to this?")
    input()
    print("[*STORY*]")
    print("You pause and try to think of what to do. The options don't look good.")
    print()

    # Choice
    print(f"[{player['name']}]".upper())
    print("A - Head to your quarters.")
    print()
    print("B - [JUST KEEP STANDING THERE]")
    print()

    # Decision
    walk_dec = ''
    while walk_dec.upper() not in ['A', 'B']:
        walk_dec = input("[CHOICE (A/B)]:    ")

    # If go to quarters, load option A
    if walk_dec.upper() == 'A':
        distrust_ship = False

    #------------------------------------------------------------------------------------------------------------------------
    # B. You just keep standing there
    if walk_dec.upper() == 'B':
        print()
        print("[*STORY*]")
        print("You decide not to head back to your quarters, but you have nowhere to be... so you just stand there. You try to")
        print("think, but your mind is still fuzzy. Come on, think... what to do, what to do...")
        input()
        print("[*STORY*]")
        print("It's no use. You don't know what to do. You decide to walk aimlessly. After a few minutes of random wandering,")
        print("you find yourself at the end of a hallway.")
        input()
        print(f"[{player['name']}]".upper())
        print("A - [TURN LEFT]")
        print()
        print("B - [TURN RIGHT]")
        print()

        # Decision
        walk_dec2 = ''
        while walk_dec2.upper() not in ['A', 'B']:
            walk_dec2 = input("[CHOICE (A/B)]:    ")

        #-----------------------------------------------------------------------------------------------------------------------
        # A. Turn left - head towards window. See the white ship
        if walk_dec2.upper() == 'A':
            print()
            print("[*STORY*]")
            print("You decide to turn left. The hallway gradually turns metallic - it looks like you're heading towards the Engine")
            print("Room from a path you normally don't take. You frown... shouldn't you know your ship better than this?")
            input()
            print("[*STORY*]")
            print("There's a window up ahead. You pause and look out. Pluto is below you in all its brown, rocky glory. How often")
            print("have you looked upon it? You stare for a while, your eye tracing the edges of the craters speckling its surface.")
            input()
            print("[*STORY*]")
            print("You jump back. Something just passed in between SHIP and Pluto... *another* ship. White. Small, couldn't hold")
            print("more than two or three people, you'd think. People... is that...?")
            input()
            print("[*STORY*]")
            print("When you stare at it, you realize the ship doesn't really look white at all. It's reflective, somewhat shiny in")
            print("the dark soup of space. The ship is coated in some material you've never seen before. You don't believe in aliens,")
            print("but on second thought maybe it'd be worth updating that belief...")
            input()
            print("[*STORY*]")
            print("As you stare at this ship passing slowly by, you barely notice the gas emanating from a nozzle in the ceiling. By")
            print("the time you notice your vision going blurry, it's too late. You cough and cough... how could this be happening?")
            print("Your headache multiplies as you stumble back down the hallway. SHIP... you remember that SHIP controls air flow")
            print("on board. You fall to the ground and soon forget everything you know about SHIP... then yourself. Your memory is")
            print("wiped clean, a fresh slate, before your brain even forgets how to breathe...")
            input()
            print()
            print()
            print()
            print()
            print("                                            [YOUR QUEST COMES TO AN END]")
            print("                                                     Ending #7")
            print()
            print("                                                      OUTCOMES:")
            print(f"                                                 - {player['name'].upper()} dies")
            if end_state in ['killer_first', 'killer_second']:
                print("                                                 - BENJAMIN dies")
            else:
                print("                                                 - BENJAMIN ???")
            print("                                                 - VERONICA ???")
            print("                                                 - SHIP AI ???")
            print()
            print("                                                       CAUSE:")
            print("                                                  Murdered by SHIP")

            # Update n_completions.pkl
            if 'n_completions.pkl' in os.listdir():
                n_completions = pickle.load(open('n_completions.pkl', 'rb'))
                n_completions += 1

                save_object(n_completions, "n_completions.pkl")

            else:
                n_completions = 1
                save_object(n_completions, "n_completions.pkl")

            quit()


        #-----------------------------------------------------------------------------------------------------------------------
        # B. Turn right and head to Zone D, where VERONICA and BENJAMIN are
        if walk_dec2.upper() == 'B':

            print("This ending has not yet been written! Goodbye :-)")
            pass


#-----------------------------------------------------------------------------------------------------------------------------
# You distrust SHIP. Maybe we make it so there's no way you go to your room. Or... you *could*, but would then have to include
# dialogue options for that level of knowledge
if distrust_ship == True:

    print("Still working on this part...")
    print()
    print("This ending has not yet been written! Goodbye :-)")


    pass



#-----------------------------------------------------------------------------------------------------------------------------
# The default is that you head to the room and get screwed
if distrust_ship == False:

    # You enter the room
    print("[*STORY*]")
    print("The doors to your quarters open as you approach.")
    input()
    print("[SHIP AI]")
    print("Good morning, Commander. Status report: Danger. I estimate the intruder will break through my firewall in 0.149")
    print("hours. I have been unable to counteract the attack. Probability of resisting intruder...")
    print("0.000000000000000000000000000000018%. Preparations must be made for failure. Cryogenic escape pods are still")
    print("active and I advise abandoning ship.")
    input()

    # Killer
    if end_state == 'killer_first':
        print("[SHIP AI]")
        print("From my readings of VERONICA's heartbeat, I see you did not kill her, as advised. This is unacceptable. Commander...")
        print("my calculations determine that your failure has significantly decreased probability of survival. VERONICA is the")
        print("imposter.")
        input()

    if end_state == 'killer_second':
        print("[SHIP AI]")
        print("From my readings of BENJAMIN's heartbeat and the elevation of yours at the time of his death, I deduce that you")
        print("killed BENJAMIN. Excellent idea, Commander. Unfortunately, my calculations determine that VERONICA should also")
        print("have been killed. VERONICA is the imposter. Probability: 99%.")
        input()

    # Failure, all headaches, all amnesia, or mixed info
    if end_state == 'failure' or all_headaches == True or all_amnesia == True or mixed_info == True:
        print("[SHIP AI]")
        print("It appears you were unable to determine whether BENJAMIN or VERONICA is the imposter, correct?")
        input()

        # Mixed info and failure end here
        print("[*STORY*]")
        print("You swallow. After a few moments, you mumble 'That's correct.'")
        input()

        # Reveal headaches info to SHIP
        if all_headaches == True:
            print(f"[{player['name']}]".upper())
            print("SHIP. I *did* learn something potentially valuable, however. Everyone on the crew awoke this morning with")
            print("headaches... both VERONICA and BENJAMIN revealed that when I spoke with them, and I've had a migraine all day.")
            print("Do you know what could be the cause?")
            input()
            print("[SHIP]")
            print("Processing...")
            input()
            print("[SHIP]")
            print("This new information is believed to be inconsequential. Irrelevance Score: 99/100. A suggested route to solve this")
            print("problem is to perform a controlled experiment where headaches are experimentally administered to crew members and")
            print("the productivity and fates of all crew members are recorded. This should be done at least 10,000 times.")
            input()

        # Reveal amnesia info to SHIP
        if all_amnesia == True:
            print(f"[{player['name']}]".upper())
            print("SHIP. I *did* learn something potentially valuable, however. Everyone on the crew awoke this morning with")
            print("headaches... as well as with amnesia. Both VERONICA and BENJAMIN have it... and I do, too. Do you know what could")
            print("be the cause?")
            input()
            print("[SHIP]")
            print("Processing...")
            input()
            print("[SHIP]")
            print("This new information is believed to be inconsequential. Irrelevance Score: 99/100. A suggested route to solve this")
            print("problem is to perform a controlled experiment where headaches are experimentally administered to crew members and")
            print("the productivity and fates of all crew members are recorded. This should be done at least 10,000 times.")
            input()
            print("[*STORY*]")
            print("Did you hear that correctly?? How could this possibly be irrelevant?")
            input()

    # Ship asks you what to do
    print("[*STORY*]")
    print("SHIP is silent for a few moments. Finally, it speaks.")
    input()
    print("[SHIP]")
    print("What is your final command?")
    input()

    # Respond
    print(f"[{player['name']}]".upper())
    print("A - I'll use the escape pod.")
    print()
    print("B - Time to take my own life, then.")
    print()

    if all_headaches == True or all_amnesia == True:
        print("C - Screw you, SHIP! This can't be the end!")
        print()

    # Decision
    conv_dec1 = ''
    if all_headaches == False and all_amnesia == False:
        while conv_dec1.upper() not in ['A', 'B']:       # Limited to options presented
            conv_dec1 = input("[CHOICE (A/B)]:    ")
    else:
        while conv_dec1.upper() not in ['A', 'B', 'C']:  # User can input C only if all_headaches == True or all_amnesia == True
            conv_dec1 = input("[CHOICE (A/B/C)]:    ")

    #---------------------------------------------------------------------------------------------------------------------------
    # A. Escape pod
    if conv_dec1.upper() == 'A':
        print()
        print("[SHIP AI]")
        print("Excellent choice, Commander. I have set a course for Earth. The escape pod number is A One Zero Nine Three Three")
        print("Eight Seven One Eight One Nine Four Two Eight One Three Six. Goodbye.")
        input()
        print("[*STORY*]")
        print("You exit your quarters and walk to the escape pods. The walk is silent - it's hard to believe anything is happening")
        print("at all. You are then standing in front of the escape pods. There are little entryways for you to crawl into a padded")
        print("space. Once you're inside, this friendly coffin-shaped vessel will send you on your space voyage.")
        input()
        print("[*STORY*]")
        print("You look at the three vessels. Which one were you supposed to use again?")
        input()

        # Respond
        print(f"[{player['name']}]".upper())
        print("A - Pod A10931871819428136")
        print("B - Pod A10933871819428136")
        print("C - Pod A10933877819428136")
        print()

        # Decision
        conv_dec2 = ''
        while conv_dec2.upper() not in ['A', 'B', 'C']:
            conv_dec2 = input("[CHOICE (A/B/C)]:    ")

        # It doesn't matter; they're all a trap
        print()
        print("[*STORY*]")
        print("You climb into the escape pod and the hatch closes with a hiss behind you. You fumble around a little until you're")
        print("comfortable, then let out a breath. Everything is dark except for the soft green glow of a monitor above your head.")
        print("'Escape procedure commencing,' a voice says. After a few seconds, a rumble slowly grows and then there's a pop as")
        print("you're ejected from the ship. You press a few buttons on the monitor above you and the pod begins to fill with a")
        print("soft gas that will put you to sleep for your voyage. In the small window in front of you, you see SHIP in all its")
        print("glory, Pluto in the background. Au revoir, SHIP...")
        input()
        print("[*STORY*]")
        print("...hold on a minute.")
        input()
        print("[*STORY*]")
        print("With a start, you notice a small white ship between SHIP and Pluto. What is that? Is that the intruder after all?")
        print("Your vision starts getting blurry. Well, at any rate... you're safe. You slowly drift away into slumber....")
        input()
        input("...")
        print()
        print("[*STORY*]")
        print("You slowly start to awaken. You're starving and so, so cold. What... where are you?")
        input()
        print("[*STORY*]")
        print("As your vision slowly sharpens, you see nothing but space in the window in front of you. This shouldn't be")
        print("happening. Why aren't you waking up on Earth? What's going on?")
        input()
        print("[*STORY*]")
        print("Your questions are never answered as you slowly starve in the pod, choking on the recirculating carbon dioxide.")
        print("Your last thoughts, repeated endlessly, are whether you got in the right pod...")
        input()
        print()
        print()
        print()
        print()
        print("                                            [YOUR QUEST COMES TO AN END]")
        print("                                                     Ending #4")
        print()
        print("                                                      OUTCOMES:")
        print(f"                                                 - {player['name'].upper()} dies")
        if end_state in ['killer_first', 'killer_second']:
            print("                                                 - BENJAMIN dies")
        else:
            print("                                                 - BENJAMIN ???")
        print("                                                 - VERONICA ???")
        print("                                                 - SHIP AI ???")
        print()
        print("                                                       CAUSE:")
        print("                                                  Lost in space...")

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
    # B. Take own life
    if conv_dec1.upper() == 'B':
        print()
        print("[*STORY*]")
        print("SHIP is silent for a few moments before responding.")
        input()
        print("[SHIP AI]")
        print("Excellent choice, Commander. You are likely to experience less pain at a death at your own hands than one from")
        print("asphyxiation or starvation. Goodbye.")
        input()
        print("[*STORY*]")
        print("You pull out the laser knife. You don't want to do this, but SHIP's right. At least you can do this honorably.")
        input()
        print("[*STORY*]")
        print("You raise the knife and plunge it into your guts. It hurts - a lot - but the pain quickly fades as darkness sets")
        print("in. Your only regret is that you never found the imposter...")
        input()
        print()
        print()
        print()
        print()
        print("                                            [YOUR QUEST COMES TO AN END]")
        print("                                                     Ending #5")
        print()
        print("                                                      OUTCOMES:")
        print(f"                                                 - {player['name'].upper()} dies")
        if end_state in ['killer_first', 'killer_second']:
            print("                                                 - BENJAMIN dies")
        else:
            print("                                                 - BENJAMIN lives")

        print("                                                 - VERONICA lives")
        print("                                                 - SHIP AI lives")
        print()
        print("                                                       CAUSE:")
        print("                                              Death at your own hands...")

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
    # C. Question SHIP
    if conv_dec1.upper() == 'C':
        print()
        print("[*STORY*]")
        print("SHIP is silent. You wait for SHIP to respond... but the silence drags on.")
        input()
        print(f"[{player['name']}]".upper())
        print("SHIP?")
        input()
        print("[*STORY*]")
        print("It's no use. SHIP doesn't respond. You grab your laser knife and head for the door.")
        input()
        print("[*STORY*]")
        print("Except... the door doesn't open. You're shocked. You can't remember anything of your past, but this seems to")
        print("definitely new: you feel like you've never experienced your door not opening - it should recognize the")
        print("identifier chip in your bicep. You feel a sinking feeling in your stomach. This can't be good.")
        input()
        print("[*STORY*]")
        print("You don't know the time, but this should be about when SHIP predicted it would be unable to fend off the")
        print("attacker. But why is your door locked? Did SHIP initiate a security lockdown before it lost control? Or is this")
        print("something the intruder is doing? You listen carefully, but the door was designed to muffle all noise on either")
        print("side of it: no way to tell what's going on out there. You sit back on your bed and try to think this one through")
        print("but you have such a headache...")
        input()
        print("[*STORY*]")
        print("You can't stop thinking about how all crew members awoke today with headaches. How could this have happened? If")
        print("there was an imposter, why wouldn't they have just killed you? Could you have misread BENJAMIN or VERONICA? You")
        print("hold your head in your hands and close your eyes... there has to be a way out of this...")
        input()
        print("...")
        input()
        print("[*STORY*]")
        print("An hour passes... then two... then twelve. You're locked in your room and your headache is growing worse. When")
        print("is the last time you ate? You're starting to get thirsty. Your thoughts are slowly becoming morbid but you try")
        print("not to think about it... SHIP still isn't responding, and your laser knife was useless against the door.")
        input()
        print("...")
        input()
        print("[*STORY*]")
        print("It's been days. SHIP never responded to you, the door is still locked, and you can't hear anything outside the")
        print("room. Gravity has remained normal, and you can still breathe... but you're so delirious that you wish the end")
        print("would come sooner. You can barely think straight...")
        input()
        print("...")
        input()
        print("[*STORY*]")
        print("You've been drifting in and out of consciousness for the last day. Were you always in the room? You feel the")
        print("trickles of memories returning to you, but you can't tell the difference between reality and dreams of a starved")
        print("brain. Your vision stopped working, but you find yourself mysteriously devoid of hunger or thirst this close to")
        print("the end...")
        input()
        print("[*STORY*]")
        print("As you drift away for the final time, you hear the door open.")
        input()
        print("[VERONICA]")
        print("Commander?")
        input()
        print()
        print()
        print()
        print()
        print("                                            [YOUR QUEST COMES TO AN END]")
        print("                                                     Ending #6")
        print()
        print("                                                      OUTCOMES:")
        print(f"                                                 - {player['name'].upper()} dies")
        if end_state in ['killer_first', 'killer_second']:
            print("                                                 - BENJAMIN dies")
        else:
            print("                                                 - BENJAMIN ???")
        print("                                                 - VERONICA lives")
        print("                                                 - SHIP AI ???")
        print()
        print("                                                       CAUSE:")
        print("                                               Thirst and starvation")

        # Update n_completions.pkl
        if 'n_completions.pkl' in os.listdir():
            n_completions = pickle.load(open('n_completions.pkl', 'rb'))
            n_completions += 1

            save_object(n_completions, "n_completions.pkl")

        else:
            n_completions = 1
            save_object(n_completions, "n_completions.pkl")

        quit()


##################################################################################################################################
# If you're not the killer...
if end_state not in ['killer_first', 'killer_second']:

    # Walking through the halls back to your quarters


    print("This ending hasn't been written yet! Goodbye :-)")

    pass




# BEST OPTION: wait until VERONICA has the antidote, shut down the SHIP AI somehow

# Maybe we can make it so the player can guess a place to go (or they have to type it in). Most places don't work out /
# are uninformative. Need some way to reward players that are more informed than others.





# Maybe you're walking back to your quarters. If you're uninformed, you'll talk to SHIP and all the storylines end with death.

# But if you know that both BENJAMIN and VERONICA have headaches... maybe you'll have the option to do something different

# If you know that both BENJAMIN and VERONICA have headaches + amnesia, you'll have an additional option

# If you know not to trust SHIP, you have fourth option

# If you have know not to trust SHIP + antidote, you





# So how is this all going to end?
# - The countdown from the SHIP AI is fake. The Ship has already been hacked.
#   o You need some way to confirm that the Ship is lying to you. You should go to Zone D (where the Ship said there's been a
#     drop in air pressure)

# - There also needs to be some way to kill the Ship AI. If it really controls gravity and air pressure, then it's the one in
#   control, and you definitely don't want to piss it off / kill it.





# You need to think about whether *you're* the imposter who poisoned everyone. Is there some way to confirm you're not? Or that's
# an open question that narrator struggles with. Could leave it open to interpretation by the player
