input_string = input("enter a string ")
var=""
count=1
for i in range(len(input_string)-1):
  if (input_string[i]==input_string[i+1]):
     count+=1
     var+=input_string[i]
  elif (input_string[i]!=input_string[i+1]):
     var=var+input_string[i]+str(count)
     count=1
  if i+2==len(input_string):
    var=var+input_string[i+1]+str(count)
if len(input_string)==1:
    var=input_string[0]+str(1)
print(var)


