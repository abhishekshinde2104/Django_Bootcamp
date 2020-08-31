###########################
## PART 10: Simple Game ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--  ##
###########################

# It's time to actually make a simple command line game so put together everything
# you've learned so far about Python. The game goes like this:

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

# There are a few things you will have to discover for yourself for this game!
# Here are some useful hints:

# Try to figure out what this code is doing and how it might be useful to you

#GETTING COMPUTER GUESS :
import random
digits = list(range(10))
random.shuffle(digits)
digits = digits[:3]
print(digits[:3])

comp_guess = 0
comp_guess = (digits[0]*100)+(digits[1]*10)+(digits[2])

print("Computer guess is : ",comp_guess)

# GETTING USER GUESS:
guess = input("What is your guess for 3 digit number ? ")
print(guess)
#print(type(guess)) -->string

#LOGICC:
check =0
while check!=1:
    if (digits[0]==guess[0] or digits[1]==guess[1] or digits[2]==guess[2]):
        print("Match")
        check =0

    elif(digits[0]==guess[0] and digits[1]==guess[1] and digits[2]==guess[2]):
        print("Perfect Match")
        check =1

    else:
        print("No Match")
        check=0





# Think about how you will compare the input to the random number, what format
# should they be in? Maybe some sort of sequence? Watch the Lecture video for more hints!
