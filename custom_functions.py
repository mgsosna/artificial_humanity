########################################################################################################
# ARTIFICIAL HUMANITY
# Custom functions
#
# Matt Grobis
########################################################################################################

# Save player stats
import pickle
def save_object(obj, filename):
    with open(filename, 'wb') as output:  # Overwrites any existing file.
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)

#------------------------------------------------------------------------------
# Scrolling 1s and 0s
import numpy as np
import time

def scrolling_binary(screen_size, n_rows, n_spaces, time_sleep):
    binary = np.random.choice([x for x in range(2)], n_rows*screen_size)
    binary.resize(n_rows, screen_size)

    for row in range(binary.shape[0]):
        str_row = str(binary[row, :])
        print('\r' + ' '*n_spaces + str_row[1:(len(str_row)-1)], end = '')   
        print()
        time.sleep(time_sleep)                

#-----------------------------------------------------------------------------
# Display crew suspicion

def display_suspicion(n_spaces, n_stars, player):
    print(" " * n_spaces, "*" * n_stars, "CREW SUSPICION LEVELS", "*" * n_stars)
    print(" " * n_spaces, "BENJAMIN:", player['crew_suspicion']['BENJAMIN'])
    print(" " * n_spaces, "VERONICA:", player['crew_suspicion']['VERONICA'])