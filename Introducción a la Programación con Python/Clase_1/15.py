#Fibonacci alternativo

ault = 0 # anteultimo
ult = 1 # ultimo
n = 10
print(ault)
for i in range(n-1):
  print(ult)
  ult, ault = ault + ult, ult
