# Key: 
# SV = Speed Value1
# DV = Distance Value
# TV = Time Value

userchoice = input("What do you want to calculate?")


if userchoice == "speed":
    dv = int(input("What is the distance?"))
    tv = int(input("What is the time?"))
    print(dv/tv)

elif userchoice == "distance":
    sv = int(input("What is the speed?"))
    tv = int(input("What is the time?"))
    print(sv*tv)

elif userchoice == "time":
    dv = int(input("What is the distance?"))
    sv = int(input("What is the speed?"))
    print(dv/sv)
