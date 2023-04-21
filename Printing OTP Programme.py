take_input=input()
length_num=len(take_input)
otp=""
for i in range(1,length_num,2):
    odd=int(take_input[i])
    odd=odd**2
    otp=otp+(str(odd))
print(otp[0:4])