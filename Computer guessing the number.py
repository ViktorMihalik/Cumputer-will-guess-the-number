# We can set up the range
low = 1
high = 1000

print("please think about number between {} and {}".format(low,high))
input("Please enter to start")

# Algorithm
guesses = 1
while low != high:
    #print("\t guess a number between {} and {} ".format(low,high))
    guess = int(low+(high-low)//2)
    add = input("My Guess is {}.  Please hint me if this is your number [yes] or it's higher[h] or lower[l]".format(guess))
    
    if add == "h":
        low = guess + 1

    if add == "l":
        high = guess - 1

    if add == "yes":
        print("YEAH I've guessed it in {} guesses". format(guesses))
        break

    guesses += 1

    if add  != "h" or "l" or "yes":
      add = input("please elect if I guessed it [yes] or it's higher[h] or lower[l]".format(guess))
    if add == "" :
      add = input("please elect if I guessed it [yes] or it's higher[h] or lower[l]".format(guess))    

else:
    print("YOU NUMBER IS {}".format(low))
    print("I got it in {} guesses".format(guesses))

