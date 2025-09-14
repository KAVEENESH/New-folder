height=float(input("height is"))
weight=float(input("weight is"))
BMI=weight/(height/100)**2
print("your BMI is",BMI)
if BMI<=18.4:
    print("you are underweight")
elif BMI<= 24.9:
  print("you are healthy")
elif BMI<= 29.9:
  print("you are fat")
elif BMI<= 34.9:
  print("you are obese")
elif BMI<= 39.9:
  print("you are very obese")
else :
 print("you are very very fat")