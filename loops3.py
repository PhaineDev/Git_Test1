# Code with loops!

import sys

print("Let's start with what i've already learned so I don't forget")
print('Please enter your name:')

myName = input()

while True: #main loop and char count
    myNameLen = str(int(len(myName))) #count chars in myName
    count = (len(myName) - myName.count(' ')) #count spaces and subtract from myName. Save as var 'count'

    print('Your name is ' + myName)
    print('Your name has ' + myNameLen + ' characters')
    print('But this includes spaces...')

    while True: #ignore spaces loop

        print('Shall we ignore spaces? Y/N?')
        choice = input()

        if choice == 'n' or choice == 'N':                      #include spaces in myName character count
            print('Your name still has ' + myNameLen + ' letters, all is well and the universe is at peace.')

        elif choice == 'y' or choice == 'Y':                    #ignore spaces in myName character count
            print('When ignoring spaces your name has ' + str(count) + ' characters!')

        else:
            print('That is not a Y or N. Please try again')     #catches input error (not y or n)
            choice = input()
            continue

        print('Would you like to start again? Y or N?')
        tryAgain = input()

        while True:

            if tryAgain == 'y' or tryAgain == 'Y':
                print('Please enter your name:')
                myName = input()

            elif tryAgain == 'n' or tryAgain == 'N':
                print('OK, Goodbye!!')
                sys.exit()
                break

            else:
                print('That is not a Y or N. Please try again') #catches input error (not y or n)
                tryAgain = input()
                continue
            break
        break

            







#print('Would you like to try again?')
#tryAgain = input()

#if tryAgain == 'y' or tryAgain =='Y': #Try again - yes
#   print('yes test')

#elif tryAgain =='n' or tryAgain =='N': #Try again no - Goodbye 2
#    print('Goodbye!! 2')

# To do:
# Try again yes to loops back to myName entry
# y/n Error checking on Try again loops
# Reduce duplicated code - Try again loops are the same so can be consolidated?

#if input == simona print('hello')