
weight=int(input("enter weight in kg:"))
height=int(input("enter height in cm:"))
age=int(input("enter age:"))
gender=input ("enter gender:").lower()

print(weight, height, age, gender)

if gender=="male":
    BMR=10*weight + 6.25*height - 5*age + 5

elif gender=="female":
    BMR=10*weight + 6.25*height - 5*age - 161

else:
    print("please enter valid gender")

print(f"BMR={BMR}")

activity_level=int(input("""
           select activity level
           press 1 for sedentay
           press 2 for lightly active
           press 3 for moderatively active
           press 4 for very active
           press 5 for extra active
   """))

if activity_level==1:
    calorie=BMR*1.2

elif activity_level==2:
    calorie=BMR*1.375

elif activity_level==3:
    calorie=BMR*1.55

elif activity_level==4:
    calorie=BMR*1.725

elif activity_level==5:
    calorie=BMR*1.9

else:
    print("please enter valid actvity level")


print(f"total number of calories yo need to maintain your current weight={calorie}")

target_weight=int(input("enter the weight to reduce in kg:")) 

duration=int(input("enter duration in weeks:"))

#1kg=>7700

calorie_deficit=target_weight*7700

days=duration*7

daily_calorie_deficit=calorie_deficit/ days

print(f"daily calorie deficit is {daily_calorie_deficit}")

 
