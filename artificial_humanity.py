######################################################################################################
# ARTIFICIAL HUMANITY - load screen
#
# Matt Grobis
######################################################################################################
import os
import pickle
from custom_functions import *

# Navigate to folder with story files
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

# Hacker mode
hacker_mode = False

# Load screen
print()
print("*" * 100)
print("\n" + " " * 40, "ARTIFICIAL HUMANITY" + "\n")
print("----- (N) NEW GAME" + "\n")
print("----- (L) LOAD GAME" + "\n")
print("----- (Q) QUIT" + "\n")
print()

#----------------------------------------------------------------------------------------------------
# Hacker mode (note: this only displays hacker mode option. Can enter hacker mode with 'h' key)
if 'n_completions.pkl' in os.listdir():

    # Load player data
    n_completions = pickle.load(open('n_completions.pkl', 'rb'))

    # Check if they beat the game twice
    if n_completions >= 2:
       print("----- (H) HACKER MODE" + "\n")
       hacker_mode = True

#----------------------------------------------------------------------------------------------------
# Get player action
if hacker_mode == False:
    print('[INSTRUCTIONS]')
    print("To play a new game, type 'N' and press enter. To load a game, enter 'L'. To quit, enter 'Q'.")
    print("Entries can be upper- or lower-case.")
    print()
    act = input("[CHOICE (N/L/Q)]:  ")

    # If action isn't one of the three options, make them input it again
    # - Note: you can enter hacker mode without seeing it as an option
    while act.upper() not in ['N', 'L', 'Q', 'H']:
        act = input("That input isn't one of the options. Please try again [N/L/Q]:    ")

if hacker_mode == True:
    print('[INSTRUCTIONS]')
    print("To play a new game, type 'N' and press enter. To load a game, enter 'L'. To quit, enter 'Q'.")
    print("To enter hacker mode, type 'H'. Entries can be upper- or lower-case.")
    print()
    act = input("[CHOICE (N/L/Q/H)]:  ")

    # If action isn't one of the three options, make them input it again
    while act.upper() not in ['N', 'L', 'Q', 'H']:
        act = input("That input isn't one of the options. Please try again [N/L/Q/H]:    ")

#-----------------------------------------------------------------------------------------------------
# Player quits
if act.upper() == 'Q':
    print("The Starfleet will have to wait another day for your service...")
    quit()

#-----------------------------------------------------------------------------------------------------
# Player loads file
if act.upper() == 'L':

    # Make sure the file actually exists
    if 'player_stats.pkl' in os.listdir():
        player = pickle.load(open('player_stats.pkl', 'rb'))

        if player['chapter'] == 1:
            import chapter_1
            import chapter_2
            import chapter_3

        if player['chapter'] == 2:
            import chapter_2
            import chapter_3

        if player['chapter'] == 3:
            import chapter_3

    # If file doesn't exist, print message and quit
    else:
        print("No 'player_stats.pkl' file found! Starting a new game.")
        input()
        import chapter_0
        import chapter_1
        import chapter_2
        import chapter_3

#-----------------------------------------------------------------------------------------------
# Player chooses new game
if act.upper() == 'N':

    # If there's an existing file, get player decision on whether to overwrite
    if 'player_stats.pkl' in os.listdir():
        overwrite = input("\n" + "WARNING: this will erase an existing file. Proceed? [Y/N]    ")

        while overwrite.lower() not in ["y", "n"]:
            overwrite = input("Please specify Y or N: should file be overwritten?   ")

        # If player ok with overwriting, begin game
        if overwrite.upper() == "Y":
            print("\n" * 2)
            import chapter_0
            import chapter_1
            import chapter_2
            import chapter_3

        # If player not ok, print message and quit
        if overwrite.upper() == "N":
            print("Will not overwrite; exiting now.")
            quit()

    # If no existing file, start new game
    else:
        print('\n' * 2)
        import chapter_0
        import chapter_1
        import chapter_2
        import chapter_3

#-------------------------------------------------------------------------------------------------------
# Player enters hacker mode
if act.upper() == 'H':
    print()
    print("[HACKER MODE ENGAGED. WARNING: MASSIVE STORYLINE SPOILERS AHEAD]")
    input()
    print("[INSTRUCTIONS]")
    print("In Hacker Mode, you have greater freedom to explore storyline options. You will be able to navigate to any chapter")
    print("and select the outcome of previous chapters. First, select the chapter you would like to begin from:")
    print()
    print("1 - [CHAPTER ONE]")
    print("2 - [CHAPTER TWO]")
    print("3 - [CHAPTER THREE]")
    print()

    chapter_choice = ''
    while chapter_choice not in [1, 2, 3]:
        chapter_choice = int(input("[CHOICE (1/2/3)]:    "))

    # No matter what they choose, create the player
    player = {}
    player['chapter'] = chapter_choice
    player['ch_1'] = dict()
    player['ch_2'] = dict()
    player['ch_3'] = dict()

    player['name'] = ""

    # Record player name
    while len(player['name']) == 0:
        print()
        player['name'] = input("[What is your name?].......").capitalize()

    #------------------------------------------------------------------------------------------------------------------
    # If chapter == 1:
    if chapter_choice == 1:

        # Inform user there are no previous decisions; starting game
        print()
        print()
        print("[INSTRUCTIONS]")
        print("There are no storyline decisions in the Introduction. Beginning Chapter 1 now.")
        input()

        save_object(player, "player_stats.pkl")
        import chapter_1
        import chapter_2
        import chapter_3

    #------------------------------------------------------------------------------------------------------------------
    # If chapter == 2 or chapter == 3:
    if (chapter_choice == 2) or (chapter_choice == 3):

        # Initialize crew suspicion
        player['crew_suspicion'] = dict()
        player['crew_suspicion']['BENJAMIN'] = 0
        player['crew_suspicion']['VERONICA'] = 0

        # Get location from chapter 1
        print()
        print()
        print("[INSTRUCTIONS]")
        print("Where did you go in Chapter 1?")
        print()
        print("[engine] - ENGINE ROOM")
        print()
        print("[life]   - LIFE SUPPORT SYSTEMS")
        print()

        # Record player room
        ch_1_room = ''
        while ch_1_room not in ['engine', 'life']:
            ch_1_room = input("[CHOICE (engine/life)]:    ").lower()

        #-------------------------------------------------------------
        # Record chapter outcome
        if ch_1_room == 'engine':
            print()
            print()
            print("[INSTRUCTIONS]")
            print("What happened in the Engine Room?")
            print()
            print("[full_reveal]  - BENJAMIN has a headache, amnesia, and distrusts SHIP")
            print()
            print("[major_reveal] - BENJAMIN has a headache and amnesia")
            print()
            print("[minor_reveal] - BENJAMIN has a headache")
            print()
            print("[failure]      - You didn't get any info from BENJAMIN")
            print()
            print("[kill_nothing] - Kill BENJAMIN and don't hide his body")
            print()
            print("[kill_hide]    - Kill BENJAMIN and hide his body")
            print()
            print("[kill_lock]    - Kill BENJAMIN and lock the door to the Engine Room")
            print()

            ch_1_outcome = ''
            while ch_1_outcome not in ['full_reveal', 'major_reveal', 'minor_reveal', 'failure',
                                       'kill_nothing', 'kill_hide', 'kill_lock']:
                ch_1_outcome = input("[CHOICE (full_reveal/major_reveal/...)]:    ").lower()

            # Get suspicion (all other outcomes are zero)
            if ch_1_outcome in ['failure', 'minor_reveal']:
                print()
                print()
                print("[INSTRUCTIONS]")
                print("How suspicious was BENJAMIN?")
                print()
                print("[0] - No suspicion")
                print()
                print("[1] - Suspicion")
                print()

                ch_1_suspicion = ''
                while ch_1_suspicion not in [0, 1]:
                    ch_1_suspicion = int(input("[CHOICE (0/1)]:    "))

                player['crew_suspicion']['BENJAMIN'] = ch_1_suspicion


            # Save player info
            player['ch_1'] = {'room': 'engine', 'outcome': ch_1_outcome}

            # If this is chapter_2, load it
            if chapter_choice == 2:
                print()
                print()
                print("[INSTRUCTIONS]")
                print("Chapter 1 decisions recorded. Beginning Chapter 2 now.")
                input()

                save_object(player, "player_stats.pkl")
                import chapter_2
                import chapter_3

        #-------------------------------------------------------------
        # Record chapter outcome
        if ch_1_room == 'life':
            print()
            print()
            print("[INSTRUCTIONS]")
            print("What happened in Life Support Systems?")
            print()
            print("[full_reveal]     - VERONICA has a headache, amnesia, and is working on a cure")
            print()
            print("[major_reveal]    - VERONCIA has a headache and amnesia")
            print()
            print("[minor_reveal]    - VERONICA has a headache")
            print()
            print("[failure]         - You didn't get any info from VERONCIA")
            print()
            print("[massive_failure] - You attempted to destroy the carbon scrubber")
            print()

            ch_1_outcome = ''
            while ch_1_outcome not in ['full_reveal', 'major_reveal', 'minor_reveal', 'failure',
                                       'massive_failure']:
                ch_1_outcome = input("[CHOICE (full_reveal/major_reveal/...)]:    ").lower()

            # Get suspicion
            if ch_1_outcome in ['failure', 'major_reveal']:
                print()
                print()
                print("[INSTRUCTIONS]")
                print("How suspicious was VERONICA?")
                print()
                print("[0] - No suspicion")
                print()
                print("[1] - Suspicion")
                print()

                ch_1_suspicion = ''
                while ch_1_suspicion not in [0, 1]:
                    ch_1_suspicion = int(input("[CHOICE (0/1)]:    "))

                player['crew_suspicion']['VERONICA'] = ch_1_suspicion

            # If massive failure, then suspicion +3
            if ch_1_outcome == 'massive_failure':
                player['crew_suspicion']['VERONICA'] = 3

            # Save player info
            player['ch_1'] = {'room': 'life', 'outcome': ch_1_outcome}

            # If this is chapter_2, load it
            if chapter_choice == 2:
                print()
                print()
                print("[INSTRUCTIONS]")
                print("Chapter 1 decisions recorded. Beginning Chapter 2 now.")
                input()

                save_object(player, "player_stats.pkl")
                import chapter_2
                import chapter_3

    ##############################################################################################################
    # Keep going if this is Chapter 3
    if chapter_choice == 3:

        # If user went to life support systems:
        if ch_1_room == 'life':

            #----------------------------------------------------------------------------------------------------------------
            # Massive failure can't make it to chapter 3, so start at chapter 2 instead
            if ch_1_outcome == 'massive_failure':
                print()
                print()
                print("[INSTRUCTIONS]")
                print("It is impossible to make it to Chapter 3 if you attempted to destroy the carbon scrubber. Beginning")
                print("Chapter 2 instead.")
                input()

                save_object(player, "player_stats.pkl")
                import chapter_2

            #-----------------------------------------------------------------------------------------------------------------
            else:
                print()
                print()
                print("[INSTRUCTIONS]")
                print("In Chapter 1 you went to Life Support Systems, so in Chapter 2 you went to the Engine Room. What")
                print("happened in the Engine Room?")
                print()
                print("[full_reveal]  - BENJAMIN has a headache, amnesia, and distrusts SHIP")
                print()
                print("[major_reveal] - BENJAMIN has a headache and amnesia")
                print()
                print("[minor_reveal] - BENJAMIN has a headache")
                print()
                print("[failure]      - You didn't get any info from BENJAMIN")
                print()
                print("[kill_nothing] - Kill BENJAMIN and don't hide his body")
                print()
                print("[kill_hide]    - Kill BENJAMIN and hide his body")
                print()
                print("[kill_lock]    - Kill BENJAMIN and lock the door to the Engine Room")
                print()

                ch_2_outcome = ''
                while ch_2_outcome not in ['full_reveal', 'major_reveal', 'minor_reveal', 'failure',
                                           'kill_nothing', 'kill_hide', 'kill_lock']:
                    ch_2_outcome = input("[CHOICE (full_reveal/major_reveal/...)]:    ").lower()

                # Get suspicion (all other outcomes are zero)
                if ch_2_outcome in ['failure', 'minor_reveal']:
                    print()
                    print()
                    print("[INSTRUCTIONS]")
                    print("How suspicious was BENJAMIN?")
                    print()
                    print("[0] - No suspicion")
                    print()
                    print("[1] - Suspicion")
                    print()

                    ch_2_suspicion = ''
                    while ch_2_suspicion not in [0, 1]:
                        ch_2_suspicion = int(input("[CHOICE (0/1)]:    "))

                    player['crew_suspicion']['BENJAMIN'] = ch_2_suspicion

                # Save player info
                player['ch_2'] = {'room': 'engine', 'outcome': ch_2_outcome}

                # Load chapter 3
                print()
                print()
                print("[INSTRUCTIONS]")
                print("Chapter 1 and 2 decisions recorded. Beginning Chapter 3 now.")
                input()

                save_object(player, "player_stats.pkl")
                import chapter_3

        #-------------------------------------------------------------------------------------------------------
        if ch_1_room == 'engine':

            #----------------------------------------------------------------------------------------------------------------
            # kill_nothing can't make it to chapter 3, so start at chapter 2 instead
            if ch_1_outcome == 'kill_nothing':
                print()
                print()
                print("[INSTRUCTIONS]")
                print("It is impossible to make it to Chapter 3 if you killed BENJAMIN and then didn't lock the door")
                print("or hide his body. Beginning Chapter 2 instead.")
                input()

                save_object(player, "player_stats.pkl")
                import chapter_2

            #-----------------------------------------------------------------------------------------------------------------
            else:
                print()
                print()
                print("[INSTRUCTIONS]")
                print("In Chapter 1 you went to the Engine Room, so in Chapter 2 you went to Life Support Systems.")
                print("What happened in Life Support Systems?")
                print()
                print("[full_reveal]   - VERONICA has a headache, amnesia, and is working on a cure")
                print()
                print("[major_reveal]  - VERONCIA has a headache and amnesia")
                print()
                print("[minor_reveal]  - VERONICA has a headache")
                print()
                print("[failure]       - You didn't get any info from VERONCIA")
                print()

                ch_2_outcome = ''
                while ch_2_outcome not in ['full_reveal', 'major_reveal', 'minor_reveal', 'failure',
                                           'massive_failure']:
                    ch_2_outcome = input("[CHOICE (full_reveal/major_reveal/...)]:    ").lower()

                # Get suspicion
                if ch_2_outcome == 'failure':
                    player['crew_suspicion']['VERONICA'] = 1

                # Save player info
                player['ch_2'] = {'room': 'life', 'outcome': ch_2_outcome}

                # Load chapter 3
                print()
                print()
                print("[INSTRUCTIONS]")
                print("Chapter 1 and 2 decisions recorded. Beginning Chapter 3 now.")
                input()

                save_object(player, "player_stats.pkl")
                import chapter_3
