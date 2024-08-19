text = list(map(int, input().split()))
banana_price  = int(text[0])
initial_value = int(text[1])
num_of_banana = int(text[2])
output = 0
 
for i in range(num_of_banana):
   output += (i+1) * banana_price
 
output = output - initial_value
if output <= 0:
   print(0)
else:
   print(output)
