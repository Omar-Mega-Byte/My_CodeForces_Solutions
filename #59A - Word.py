text = input().strip()
lower_count = 0
upper_count = 0
for word in text:
   if word.islower():
       lower_count += 1
   else:
       upper_count += 1
if upper_count > lower_count:
   print(text.upper())
else:
   print(text.lower())
