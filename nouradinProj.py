def Trafic(drive, drink ):
    drive = input("take action: ")
    drink = input("take second action: ")
    if (drive == True) and (drink == True):
        print("Dont Drive")

    elif not(drive == True) or (drink == True):
        print("you can drive")
    elif (drive == False) and (drink == True):
        print("please take a taxi and continue your drinking")
        
    else:
        print("you are free from those acts go ahead")

Trafic()
