import sys

print("24")

try:
  x = int(input("x :"))
  y = int(input("Y : "))
except ValueError:
   print("Invalid input!")
   sys.exit(1)
try :
    ans = x / y
except ZeroDivisionError:
    print("Error cannot divide by 0.")
    sys.exit(1)



print(f"{x} / {y} = ans")