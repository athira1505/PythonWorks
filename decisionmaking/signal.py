# Syntax

# if condition1:
#     stmt1

# elif condition2:
#     stmt2

# elif condition3:
#     stmt3

# else:
#     default stmt

signal=input("enter the signal:").lower() #lower() will convert all letters to small letters

if signal=="red":
    print("STOP")

elif signal=="green":
    print("GO..")

elif signal=="yellow":
    print("wait")

else:
    print("invalid signal")