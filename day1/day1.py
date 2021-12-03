with open('inputs/input.txt') as input:
  inputList = input.read().split("\n")
  input.close()
  
increases = 0

for i, measurement in enumerate(inputList):
  if i == 0:
    continue
  if inputList[i] > inputList[i-1]:
    increases+=1

print(increases)
    
  