

def QuickNote(x):
    counter = 0
    while counter < x:
        print("Just checking to make sure latest kali-linux vm is configured correctly.")
        print( str( (x-counter) ) )
        print()
        print()
        counter += 1


if __name__=="__main__":
    QuickNote(5)



