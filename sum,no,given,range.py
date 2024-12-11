start = int(input("enter the start of the range: "))
end = int(input("enter the end of the range : "))
sum = 0
for i in range(start, end + 1):
  sum += i
  print("the sum is:", sum)
