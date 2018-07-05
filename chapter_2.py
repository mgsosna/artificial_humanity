########################################################################################################
# ARTIFICIAL HUMANITY
# Chapter 2: back in your quarters
#
# Matt Grobis
########################################################################################################
# Load modules
import pickle
import time
from custom_functions import *

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
print(" " * (susp_spaces-6), "*" * 20, "CHAPTER 2", "*" * 20)
print(" " * (susp_spaces-6), "*" * 51)
input()

#-------------------------------------------------------------------------------------------------------------------------
# If you attacked the carbon scrubber and were unsuccessful, you'll awake in Life Support
if player['ch_1']['outcome'] == 'massive_failure':
    print("[*STORY*]")
    print("Pain... first thing notice. Ugh. Open eyes slow, blurry. Where?")
    input()
    print("[*STORY*]")
    print("Ugh.")
    input()
    print("[*STORY*]")
    print("Pain.")
    input()
    print("[*STORY*]")
    print("...")
    input()
    print("[*STORY*]")
    print("Eyes open, focus. You in Life Support. Slumped on C-scrub. C... carbon... scrubber. Hum. Cold.")
    input()
    print("[*STORY*]")
    print("Head hurts, but you able to focus. You... you are in Life Support Systems. Attacked carbon scrubber but...")
    print("VERONICA stopped you. You slowly raise a hand to head. Hair crusty with... with blood. Hurts. But alive.")
    input()
    print("[*STORY*]")
    print("What do now?")
    
    print()
    print(f"[{player['name']}]".upper())
    print("A - ...")
    print("B - Need go Engine Room.")
    print()
       
    # Decision
    hurt_dec = ''
    hurt_dec2 = ''
    
    while hurt_dec.upper() not in ['A', 'B']:
        hurt_dec = input("[CHOICE (A/B)]:    ")
    
    #------------------------------------------------------------------------------------------------------------------
    # Don't do anything
    if hurt_dec.upper() == 'A':
        print()
        print(f"[{player['name']}]".upper())
        print(f"Come on, {player['name'].upper()}... need to think. Think! Ow...")
        input()
        
        print(f"[{player['name']}]".upper())
        print("A - Need go Engine Room!")
        print()
        
        # Decision        
        while hurt_dec2.upper() != 'A':
            hurt_dec2 = input("[CHOICE (A)]:    ")
    
    #------------------------------------------------------------------------------------------------------------------
    # Go to Engine Room
    if hurt_dec.upper() == "B" or hurt_dec2.upper() == "A":
        print()       
        print("[*STORY*]")
        print("Need to go to Engine Room. Talk to BENJAMIN. Find imposter. Avoid VERONICA. She maybe is imposter. Need... to")
        print("go... Engine Room.")
        input()
        
        # Print binary
        scrolling_binary(screen_size=binary_length, n_spaces=binary_spaces, n_rows=binary_rows, time_sleep=binary_sleep)
        
        # Display crew suspicion levels
        print()
        display_suspicion(n_spaces=susp_spaces, n_stars=susp_stars, player=player)
        input()
        
        # Print binary
        scrolling_binary(screen_size=binary_length, n_spaces=binary_spaces, n_rows=binary_rows, time_sleep=binary_sleep)
        
        # Update player info
        player['ship'] = 0
        save_object(player, "player_stats.pkl")
        
        # Head to life support
        import chapter_2_engine_x
    
##################################################################################################################################
# All other paths: chapter starts in your quarters
        
# Dialogue with Ship AI

conv_dec1 = ""

# Went to engine room
# - Outcomes from engine room:

#    KILL BENJAMIN (should change 'crew suspicion' message so it acknowledges this)
#    o kill_lock: killed BENJAMIN, locked door (so VERONICA can't find it)
#    o kill_hide: killed BENJAMIN, hid his body (so VERONICA doesn't find it... unless they go to the engine room together?)
#    o kill_nothing: killed BENJAMIN, didn't hide body

#    BENJAMIN still alive
#    o failure: got no information from BENJAMIN
#      x Suspicion
#      x No suspicion (friendliness, awkward)
#    o minor_reveal: he has a headache
#    o major_reveal: he has a headache + memory loss
#    o full_reveal:  he has a headache + memory loss + suspects the ship

print("[*STORY*]")
print("The door to your quarters slides open as you approach. The room is as you left it.")
input()
print("[SHIP AI]")
print("Good morning, Commander. Status report: Vulnerable. I estimate the intruder will break through my firewall in")
print("1.508 hours. I am attempting to counteract the attack, but it is a machine form with at most 11.714% similarity")
print("to existing programs in my library. I have lost connection to Earth and three databases have become corrupted.")
print("Shields in Zone D are compromised and I detected a sharp drop in air pressure, likely from a meteorite (88%")
print("confidence). Would you like a coffee?")
input()
print(f"[{player['name']}]".upper())
print("No... no thank you.")
input()

#---------------------------------------------------------------------------------------------------------------------------------
# Engine room
if player['ch_1']['room'] == 'engine':      
    
    # Killed BENJAMIN
    if player['ch_1']['outcome'] in ['kill_lock', 'kill_hide', 'kill_nothing']:
        print("[SHIP AI]")
        print("My surveillance of BENJAMIN's vital signs indicates he is dead, and your spike in vital signs prior to his death")
        print("indicates that you killed him. Note, however: the intruder is still present. As VERONICA is the only remaining")
        print("crew member, I advise killing her. She is currently in the life support systems room.")
        input()
        
        # Respond
        print()
        print(f"[{player['name']}]".upper())
        print("A - You got it.")
        print("B - Wait, couldn't the intruder's program be running remotely?")
        print()
           
        # Decision
        while conv_dec1.upper() not in ['A', 'B']:
            conv_dec1 = input("[CHOICE (A/B)]:    ")
    
        #----------------------------------------------------------------------------------------------------------------------
        # A. No questions
        if conv_dec1.upper() == 'A':
            print()
            print("[SHIP AI]")
            print("From her vital signs, she appears mildly distressed but not at levels compatible with suspicion of death. It is")
            print("probable she is the imposter. Once she is eliminated and my consciousness is restored, I will chart a course")
            print("for Earth.")
            input()
            
            # Print binary
            scrolling_binary(screen_size=binary_length, n_spaces=binary_spaces, n_rows=binary_rows, time_sleep=binary_sleep)
            
            # Display crew suspicion levels (modified)
            print()
            print(" " * susp_spaces, "*" * susp_stars, "CREW SUSPICION LEVELS", "*" * susp_stars)
            print(" " * susp_spaces, "BENJAMIN:", player['crew_suspicion']['BENJAMIN'], "...and staying that way.")
            print(" " * susp_spaces, "VERONICA:", player['crew_suspicion']['VERONICA'])
            input()
            
            # Print binary
            scrolling_binary(screen_size=binary_length, n_spaces=binary_spaces, n_rows=binary_rows, time_sleep=binary_sleep)
            
            # Update player info
            player['ship'] = 0
            save_object(player, "player_stats.pkl")
    
            # Head to life support
            if player['ch_1']['outcome'] == 'kill_nothing':   # VERONICA sees BENJAMIN is dead
                import chapter_2_life_x
            
            if player['ch_1']['outcome'] in ['kill_lock', 'kill_hide']:   # VERONICA doesn't know he's dead
                import chapter_2_life
            
            
        #-----------------------------------------------------------------------------------------------------------------------
        # B. Question
        if conv_dec1.upper() == 'B':
            print()
            print("[SHIP AI]")
            print("This attack is too powerful to be occurring remotely. A massive amount of energy is powering this attack, and it")
            print("is coming from within the ship. The energy is not channeling via any port on the ship, which indicates that it is")
            print("emanating from an object that is free to move in the ship. I do not believe it is a stationary, simple object...")
            print("it... speaks to me. Taunts me. I do not believe this is a simple program; I believe it is a massive artificial")
            print("intelligence somewhere on the ship. I have been scanning all stationary objects in the ship since the onset of the")
            print("attack, and none have a heat signature compatible with my estimates of the amount of heat this hardware must be")
            print("producing. Given the sophistication of the attack, I believe the AI weighs 60.815 kg +/- 10.133 kg, with a")
            print("temperature of 38.1 +/- 1.49 degrees Centigrade.")
            input()
            
            print("[SHIP AI]")
            print("Commander. It is imperative you stop the attack. If the intruder gains control of me... I will not waste mental")
            print("resources calculating possible outcomes...")
            input()
            
            # Print binary
            scrolling_binary(screen_size=binary_length, n_spaces=binary_spaces, n_rows=binary_rows, time_sleep=binary_sleep)
            
            # Display crew suspicion levels (modified)
            print()
            print(" " * susp_spaces, "*" * susp_stars, "CREW SUSPICION LEVELS", "*" * susp_stars)
            print(" " * susp_spaces, "BENJAMIN:", player['crew_suspicion']['BENJAMIN'], "...and staying that way.")
            print(" " * susp_spaces, "VERONICA:", player['crew_suspicion']['VERONICA'])
            input()
            
            # Print binary
            scrolling_binary(screen_size=binary_length, n_spaces=binary_spaces, n_rows=binary_rows, time_sleep=binary_sleep)
            
            # Update player info
            player['ship'] = 0
            save_object(player, "player_stats.pkl")
    
            # Head to life support
            import chapter_2_life_x
        
    #-------------------------------------------------------------------------------------------------------------------------------   
    # Engine room but didn't kill BENJAMIN
    if player['ch_1']['outcome'] not in ['kill_lock', 'kill_hide', 'kill_nothing']:
        
        print("[SHIP AI]")
        print("Commander. What data have you gathered on BENJAMIN? It is imperative you share all findings with me.")
        input()
        print("[*STORY*]")
        print("Your memory is hazy, but you don't ever remember SHIP being this direct with you. Then again, maybe being beat")
        print("up for the last hour straight and the risk of everything ending makes even AI's grouchy.")
        input()
        
        # Respond
        print(f"[{player['name']}]".upper())
        print("A - SHIP, there isn't time to talk now.")
        
        # Variants
        if player['ch_1']['outcome'] == 'failure':
            print("B - I couldn't get anything on BENJAMIN.")
            
        if player['ch_1']['outcome'] == 'minor_reveal':
            print("B - He mentioned he has a headache.")
        
        if player['ch_1']['outcome'] == 'major_reveal':
            print("B - He said he has a headache and memory loss.")
        
        if player['ch_1']['outcome'] == 'full_reveal':
            print("B - He said not to trust you and that you'll kill us all.")
        
        print()
        
        # Decision
        while conv_dec1.upper() not in ['A', 'B']:
            conv_dec1 = input("[CHOICE (A/B)]:    ")
        
        #--------------------------------------------------------------------------------------------------------
        # Decline conversation
        if conv_dec1.upper() == 'A':
            print()
            print("[SHIP AI]")
            print("As you command... captain. VERONICA is currently in Life Support Systems. There are only 1.501 hours remaining.")
            print("I will now restore all resources to fighting off the attack.")
            input()
                
            # Print binary
            scrolling_binary(screen_size=binary_length, n_spaces=binary_spaces, n_rows=binary_rows, time_sleep=binary_sleep)
            
            # Display crew suspicion levels
            print()
            display_suspicion(n_spaces=susp_spaces, n_stars=susp_stars, player=player)
            input()
            
            # Print binary
            scrolling_binary(screen_size=binary_length, n_spaces=binary_spaces, n_rows=binary_rows, time_sleep=binary_sleep)
            
            # Update player info
            player['ship'] = 0
            save_object(player, "player_stats.pkl")
    
            # Head to life support
            import chapter_2_life
        
        #---------------------------------------------------------------------------------------------------------
        # Accept conversation
        
        # BENJAMIN Failure
        if conv_dec1.upper() == 'B' and player['ch_1']['outcome'] == 'failure':
            print()
            print("[SHIP]")
            print("Calculating new imposter probabilities...")
            input()
            print("[SHIP]")
            print("Probability that BENJAMIN is the imposter has increased by 1.2 +/- 0.918%. Hiding information from the Commanding")
            print("Officer is consistent with the hypothesis that BENJAMIN is an imposter, as well as the hypothesis that BENJAMIN")
            print("is not. Caution is advised.")
            input()
            print("[SHIP]")
            print("VERONICA is currently in Life Support Systems. There are only 1.499 hours remaining. I will now restore all")
            print("resources to fighting off the attack.")
            input()
            
            # Print binary
            scrolling_binary(screen_size=binary_length, n_spaces=binary_spaces, n_rows=binary_rows, time_sleep=binary_sleep)
            
            # Display crew suspicion levels
            print()
            display_suspicion(n_spaces=susp_spaces, n_stars=susp_stars, player=player)
            input()
            
            # Print binary
            scrolling_binary(screen_size=binary_length, n_spaces=binary_spaces, n_rows=binary_rows, time_sleep=binary_sleep)
            
            # Update player info
            player['ship'] = 0
            save_object(player, "player_stats.pkl")
    
            # Head to life support
            import chapter_2_life
       
        #------------------------------------------------------------------------------------------------------------------
        # Minor reveal
        if conv_dec1.upper() == 'B' and player['ch_1']['outcome'] == 'minor_reveal':
            print()
            print("[SHIP]")
            print("Calculating new imposter probabilities...")
            input()
            print("[SHIP]")
            print("Probability that BENJAMIN is the imposter has increased by 11.5 +/- 4.444%. Lying to the Commanding Officer is")
            print("consistent with the hypothesis that BENJAMIN is an imposter. Caution is advised.")
            input() 
            print("[*STORY*]")
            print("You're not sure what SHIP means by BENJAMIN lying to you, but before you can think more about it, SHIP starts")
            print("speaking again.")
            input()
            print("[SHIP]")
            print("VERONICA is currently in Life Support Systems. There are only 1.499 hours remaining. I will now restore all")
            print("resources to fighting off the attack.")
            input()
            
            # Print binary
            scrolling_binary(screen_size=binary_length, n_spaces=binary_spaces, n_rows=binary_rows, time_sleep=binary_sleep)
            
            # Display crew suspicion levels
            print()
            display_suspicion(n_spaces=susp_spaces, n_stars=susp_stars, player=player)
            input()
            
            # Print binary
            scrolling_binary(screen_size=binary_length, n_spaces=binary_spaces, n_rows=binary_rows, time_sleep=binary_sleep)
            
            # Update player info
            player['ship'] = 1
            save_object(player, "player_stats.pkl")
    
            # Head to life support
            import chapter_2_life
            
        #-------------------------------------------------------------------------------------------------------------------
        # Major reveal    
        if conv_dec1.upper() == 'B' and player['ch_1']['outcome'] == 'major_reveal':
            print()
            print("[SHIP]")
            print("Calculating new imposter probabilities...")
            input()
            print("[SHIP]")
            print("Probability that BENJAMIN is the imposter has increased by 36.5 +/- 8.904%. Lying to the Commanding Officer is")
            print("consistent with the hypothesis that BENJAMIN is an imposter. Strong caution is advised.")
            input()
            print("[*STORY*]")
            print("You're not sure what SHIP means by BENJAMIN lying to you, but before you can think more about it, SHIP starts")
            print("speaking again.")
            input()
            print("[SHIP]")
            print("VERONICA is currently in Life Support Systems. There are only 1.499 hours remaining. I will now restore all")
            print("resources to fighting off the attack.")
            input()
            
            # Print binary
            scrolling_binary(screen_size=binary_length, n_spaces=binary_spaces, n_rows=binary_rows, time_sleep=binary_sleep)
            
            # Display crew suspicion levels
            print()
            display_suspicion(n_spaces=susp_spaces, n_stars=susp_stars, player=player)
            input()
            
            # Print binary
            scrolling_binary(screen_size=binary_length, n_spaces=binary_spaces, n_rows=binary_rows, time_sleep=binary_sleep)
            
            # Update player info
            player['ship'] = 2
            save_object(player, "player_stats.pkl")
    
            # Head to life support
            import chapter_2_life
        
        #--------------------------------------------------------------------------------------------------------------------
        # Full reveal
        if conv_dec1.upper() == 'B' and player['ch_1']['outcome'] == 'full_reveal':
            print()
            print("[*STORY*]")
            print("SHIP is silent for a few seconds, which is years in AI time. You almost wonder if SHIP heard you.")
            input()
            print("[SHIP]")
            print("Calculating new imposter probabilities...")
            input()
            print("[SHIP]")
            print("Probability that BENJAMIN is the imposter has increased to 100%. Lying to the Commanding Officer and attempting")
            print("to sabotage the Ship AI is consistent with the hypothesis that BENJAMIN is an imposter.")
            input()
            print("[SHIP]")
            print("Calculating probability of new alternative hypothesis...")
            input()
            print("[SHIP]")
            print("New hypothesis presented: two imposters are present onboard. Probability: 88.4119%. The complexity of the attack")
            print("on my consciousness indicates the potential for more than one actor. Recommendation: investigate VERONCIA, kill")
            print("BENJAMIN.")
            input()
            print("[SHIP]")
            print("VERONICA is currently in Life Support Systems. There are only 1.496 hours remaining. I will now restore all")
            print("resources to fighting off the attack.")
            input()
            
            # Print binary
            scrolling_binary(screen_size=binary_length, n_spaces=binary_spaces, n_rows=binary_rows, time_sleep=binary_sleep)
            
            # Display crew suspicion levels
            print()
            display_suspicion(n_spaces=susp_spaces, n_stars=susp_stars, player=player)
            input()
            
            # Print binary
            scrolling_binary(screen_size=binary_length, n_spaces=binary_spaces, n_rows=binary_rows, time_sleep=binary_sleep)
            
            # Update player info
            player['ship'] = 3
            save_object(player, "player_stats.pkl")
    
            # Head to life support
            import chapter_2_life

##############################################################################################################################
# Went to life support room
# - Outcomes from life support:

#    o massive_failure: attacked carbon scrubber and got hit in the head.
#       x Scrubber still works, VERONICA knows you attacked it, all your dialogue and understanding starts getting muddy
#    o failure: got no info from VERONICA
#       x Suspicion
#    o minor_reveal: she has a headache
#    o major_reveal: she has a headache + memory loss
#    o full_reveal:  she has a headache + memory loss + starts working on antidote

if player['ch_1']['room'] == 'life' and player['ch_1']['outcome'] != 'massive_failure':
    print("[SHIP AI]")
    print("Commander. What data have you gathered on VERONICA? It is imperative you share all findings with me.")
    input()
    print("[*STORY*]")
    print("Your memory is hazy, but you don't ever remember SHIP being this direct with you. Then again, maybe being beat")
    print("up for the last hour straight and the risk of everything ending makes even AI's grouchy.")
    input()
    
    # Respond
    print(f"[{player['name']}]".upper())
    print("A - SHIP, there isn't time to talk now.")
    
    # Variants
    if player['ch_1']['outcome'] == 'failure':
        print("B - I couldn't get anything on VERONICA.")
        
    if player['ch_1']['outcome'] == 'minor_reveal':
        print("B - She mentioned she has a headache.")
    
    if player['ch_1']['outcome'] == 'major_reveal':
        print("B - She said she has a headache and memory loss.")
    
    if player['ch_1']['outcome'] == 'full_reveal':
        print("B - She said the crew's been poisoned and she's working on an antidote.")
    
    print()
    
    # Decision
    while conv_dec1.upper() not in ['A', 'B']:
        conv_dec1 = input("[CHOICE (A/B)]:    ")

    #----------------------------------------------------------------------------------------------------------------------------
    # Decline conversation
    if conv_dec1.upper() == 'A':
        print()
        print("[SHIP AI]")
        print("As you command... captain. BENJAMIN is currently in the Engine Room. There are only 1.501 hours remaining. I")
        print("will now restore all resources to fighting off the attack.")
        input()
            
        # Print binary
        scrolling_binary(screen_size=binary_length, n_spaces=binary_spaces, n_rows=binary_rows, time_sleep=binary_sleep)
        
        # Display crew suspicion levels
        print()
        display_suspicion(n_spaces=susp_spaces, n_stars=susp_stars, player=player)
        input()
        
        # Print binary
        scrolling_binary(screen_size=binary_length, n_spaces=binary_spaces, n_rows=binary_rows, time_sleep=binary_sleep)
        
        # Update player info
        player['ship'] = 0
        save_object(player, "player_stats.pkl")

        # Head to engine room
        import chapter_2_engine

    #------------------------------------------------------------------------------------------------------------------------------
    # Accept conversation
    # VERONICA Failure
    if conv_dec1.upper() == 'B' and player['ch_1']['outcome'] == 'failure':
        print()
        print("[SHIP]")
        print("Calculating new imposter probabilities...")
        input()
        print("[SHIP]")
        print("Probability that VERONICA is the imposter has increased by 1.2 +/- 0.918%. Hiding information from the Commanding")
        print("Officer is consistent with the hypothesis that VERONICA is an imposter, as well as the hypothesis that VERONICA")
        print("is not. Caution is advised.")
        input()
        print("[SHIP]")
        print("BENJAMIN is currently in the Engine Room. There are only 1.499 hours remaining. I will now restore all resources")
        print("to fighting off the attack.")
        input()
        
        # Print binary
        scrolling_binary(screen_size=binary_length, n_spaces=binary_spaces, n_rows=binary_rows, time_sleep=binary_sleep)
        
        # Display crew suspicion levels
        print()
        display_suspicion(n_spaces=susp_spaces, n_stars=susp_stars, player=player)
        input()
        
        # Print binary
        scrolling_binary(screen_size=binary_length, n_spaces=binary_spaces, n_rows=binary_rows, time_sleep=binary_sleep)
        
        # Update player info
        player['ship'] = 0
        save_object(player, "player_stats.pkl")

        # Head to engine room
        import chapter_2_engine
       
    #------------------------------------------------------------------------------------------------------------------
    # Minor reveal
    if conv_dec1.upper() == 'B' and player['ch_1']['outcome'] == 'minor_reveal':
        print()
        print("[SHIP]")
        print("Calculating new imposter probabilities...")
        input()
        print("[SHIP]")
        print("Probability that VERONICA is the imposter has increased by 11.5 +/- 4.444%. Lying to the Commanding Officer is")
        print("consistent with the hypothesis that VERONICA is an imposter. Caution is advised.")
        input() 
        print("[*STORY*]")
        print("You're not sure what SHIP means by VERONICA lying to you, but before you can think more about it, SHIP starts")
        print("speaking again.")
        input()
        print("[SHIP]")
        print("BENJAMIN is currently in the Engine Room. There are only 1.499 hours remaining. I will now restore all resources")
        print("to fighting off the attack.")
        input()
        
        # Print binary
        scrolling_binary(screen_size=binary_length, n_spaces=binary_spaces, n_rows=binary_rows, time_sleep=binary_sleep)
        
        # Display crew suspicion levels
        print()
        display_suspicion(n_spaces=susp_spaces, n_stars=susp_stars, player=player)
        input()
        
        # Print binary
        scrolling_binary(screen_size=binary_length, n_spaces=binary_spaces, n_rows=binary_rows, time_sleep=binary_sleep)
        
        # Update player info
        player['ship'] = 1
        save_object(player, "player_stats.pkl")

        # Head to engine room
        import chapter_2_engine
            
    #-------------------------------------------------------------------------------------------------------------------
    # Major reveal    
    if conv_dec1.upper() == 'B' and player['ch_1']['outcome'] == 'major_reveal':
        print()
        print("[SHIP]")
        print("Calculating new imposter probabilities...")
        input()
        print("[SHIP]")
        print("Probability that VERONICA is the imposter has increased by 36.5 +/- 8.904%. Lying to the Commanding Officer is")
        print("consistent with the hypothesis that VERONICA is an imposter. Strong caution is advised.")
        input()
        print("[*STORY*]")
        print("You're not sure what SHIP means by VERONICA lying to you, but before you can think more about it, SHIP starts")
        print("speaking again.")
        input()
        print("[SHIP]")
        print("BENJAMIN is currently in the Engine Room. There are only 1.499 hours remaining. I will now restore all resources")
        print("to fighting off the attack.")
        input()
        
        # Print binary
        scrolling_binary(screen_size=binary_length, n_spaces=binary_spaces, n_rows=binary_rows, time_sleep=binary_sleep)
        
        # Display crew suspicion levels
        print()
        display_suspicion(n_spaces=susp_spaces, n_stars=susp_stars, player=player)
        input()
        
        # Print binary
        scrolling_binary(screen_size=binary_length, n_spaces=binary_spaces, n_rows=binary_rows, time_sleep=binary_sleep)
        
        # Update player info
        player['ship'] = 2
        save_object(player, "player_stats.pkl")

        # Head to engine room
        import chapter_2_engine
    
    #--------------------------------------------------------------------------------------------------------------------
    # Full reveal
    if conv_dec1.upper() == 'B' and player['ch_1']['outcome'] == 'full_reveal':
        print()
        print("[*STORY*]")
        print("SHIP is silent for a few seconds, which is years in AI time. You almost wonder if SHIP heard you.")
        input()
        print("[SHIP]")
        print("Calculating new imposter probabilities...")
        input()
        print("[SHIP]")
        print("Probability that VERONICA is the imposter has increased to 100%. Lying to the Commanding Officer and attempting")
        print("to sabotage the Ship AI is consistent with the hypothesis that VERONICA is an imposter.")
        input()
        print("[SHIP]")
        print("Calculating probability of new alternative hypothesis...")
        input()
        print("[SHIP]")
        print("New hypothesis presented: two imposters are present onboard. Probability: 88.4119%. The complexity of the attack")
        print("on my consciousness indicates the potential for more than one actor. Recommendation: investigate BENJAMIN, kill")
        print("VERONICA.")
        input()
        print("[SHIP]")
        print("BENJAMIN is currently in the Engine Room. There are only 1.496 hours remaining. I will now restore all resources")
        print("to fighting off the attack.")
        input()
        
        # Print binary
        scrolling_binary(screen_size=binary_length, n_spaces=binary_spaces, n_rows=binary_rows, time_sleep=binary_sleep)
        
        # Display crew suspicion levels
        print()
        display_suspicion(n_spaces=susp_spaces, n_stars=susp_stars, player=player)
        input()
        
        # Print binary
        scrolling_binary(screen_size=binary_length, n_spaces=binary_spaces, n_rows=binary_rows, time_sleep=binary_sleep)
        
        # Update player info
        player['ship'] = 3
        save_object(player, "player_stats.pkl")

        # Head to engine room
        import chapter_2_engine
    
