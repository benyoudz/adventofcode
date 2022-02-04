
inputs = open('input.txt','r').readlines()
def split(word):
    return [char for char in word]
Bgamm = []
epsilonr=[]

for i in range(12):
   Zeros=0
   Ones=0
   for n in range(len(inputs)):
       input = inputs[n]
       input = split(input)

       if int(input[i]) == 0:
           Zeros += 1
       else:
           Ones += 1
   if Zeros > Ones:
           Bgamm.append(0)
           epsilonr.append(1)
   else:    
           Bgamm.append(1)
           epsilonr.append(0)        
# gamm = ''.join(str(x) for x in Bgamm)
# eps =''.join(str(x) for x in epsilonr)
Dgamm =0
Deps=0
lenGamm = len(Bgamm)
# Script For Convert Binary To Decimal 'D' Reference Decimals & 'B' Reference Binarys
for i in range(lenGamm):
   Dgamm += int(Bgamm[i])*(2**(lenGamm-i-1))    
   Deps += int(epsilonr[i])*(2**(lenGamm-i-1))   
print(Dgamm*Deps)        
#========================================= Part Two ==========================================

