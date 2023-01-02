print("I have information for the following planets:\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")
 
 #planet number correlates to specific planet above, weight can changed based on user input
weight = 185
planet = 6

# Only one description will print based on planet number above

if planet == 1:
  print("On Venus you weigh ", end="") 
  print(weight * 0.91, end="")
  print(" pounds!")
elif planet == 2:
  print("On Mars you weigh ", end="") 
  print(weight * 0.38, end="")
  print(" pounds!")
elif planet == 3:
  print("On Jupiter you weigh ", end="") 
  print(weight * 2.34, end="")
  print(" pounds!")
elif planet == 4:
  print("On Saturn you weigh ", end="") 
  print(weight * 1.06, end="")
  print(" pounds!")
elif planet == 5:
  print("On Uranus you weigh ", end="") 
  print(weight * 0.92, end="")
  print(" pounds!")
else planet == 6:
  print("On Neptune you weigh ", end="") 
  print(weight * 1.19, end="")
  print(" pounds!")
