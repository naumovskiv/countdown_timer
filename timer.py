import time
import sys

def timer(): #define timer function
    while True: #input validation loop
        try:
            input_time=int(input("Enter timer duration in seconds (integer): "))
        except ValueError: #give error for invalid input
            print("Invalid Value, try again!")
            continue
        else:
            break #on valid input
    for i in range(input_time,0,-1): #countdown
        sec= i%60
        min= (i//60)%60
        hr= i//3600
        sys.stdout.write('\r' + f'Time remaining:{hr:02d}:{min:02d}:{sec:02d}')#print time remaining over same output
        sys.stdout.flush()
        time.sleep(1) #wait 1 second per loop

    sys.stdout.write('\r' +"Time is up!".center(23,'*')) #complete message written over current line

timer()