import math
text = list(map(int, input().split()))
n = text[0]
m = text[1]
a = text[2]
 
num_length = math.ceil(n / a)
num_width = math.ceil(m / a)
 
num_flagstones = num_length * num_width
 
print(num_flagstones)
