#vahemiku kehtestamine
low_limit= float(input("min: "))
high_limit= float(input("max: "))

#inputi saamine 
input_temp1= float(input("input1:"))
input_temp2= float(input("input2:"))

#input validity control (1-valid; 0-not valid)
valid_range=((low_limit-3), (high_limit+3))

if valid_range[0]<= input_temp1 <= valid_range[1]:
    input1_validity= 1
else:
    input1_validity= 0

if valid_range[0]<= input_temp2 <= valid_range[1]:
    input2_validity= 1
else:
    input2_validity= 0

#vale/vigase info kustutamine
if input1_validity== 0:
    input_temp1= input_temp2
    #print("andur 1 vigane")
else:
    input_temp1= input_temp1

if input2_validity== 0:
    input_temp2= input_temp1
    #print(andur 2 vigane)
else:
    input_temp2= input_temp2

#input average leidmine
input_temp= ((input_temp1+input_temp2)/2)


#kontroll kas input on antud vahemikus ja output(0-turn/stay off; 1-turn/stay on)
if low_limit <= input_temp <= high_limit:
    output=0
else:
    output=1


#kontroll print commandid
#print("1 validity: ", input1_validity)
#print("2 validity: ", input2_validity)
#print(input_temp1)
#print(input_temp2)
#print(input_temp)
#print(output)