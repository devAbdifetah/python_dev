def trafic(drive, drink):
    out = input("enter your choice"+trafic(drive, drink))
    if (drive == True) and (drink == True):
        print("Dont Drive")

    elif not(drive == True) and (drink == True):
        print("you can drive")
    elif (drive == False) and (drink == True):
        print("please take a taxi and continue your drinking")   
    else:
        print("take your taxi and contine your drinking")

trafic(drive, drink)
