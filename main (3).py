# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

BMI = round(weight / height**2, 1)
BMI_I = int (BMI)

if BMI < 18.5 :
  print (f"your BMI is {BMI}, you are underweight")
elif BMI < 25 :
  print (f"your BMI is {BMI}, you have a normal weight")
elif BMI_I < 30 :
  print(f"your BMI is {BMI_I}, you are slightly overweight")
elif BMI_I < 35 :
  print (f"your BMI is {BMI_I}, you are obese")
else :
  print(f"your BMI is {BMI_I}, you are clinically obese")



    

