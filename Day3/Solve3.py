inputs = open('input.txt','r').readlines()
def split(word):
    return [char for char in word]
# gammar = []
# epsilonr=[]

# for i in range(12):
#     Zeros=0
#     Ones=0
#     for n in range(len(inputs)):
#         input = inputs[n]
#         input = split(input)

#         if int(input[i]) == 0:
#             Zeros += 1
#         else:
#             Ones += 1
#     if Zeros > Ones:
#             gammar.append(0)
#             epsilonr.append(1)
#     else:    
#             gammar.append(1)
#             epsilonr.append(0)        



# gamm = ''.join(str(x) for x in gammar)
# eps =''.join(str(x) for x in epsilonr)

# gamm = split(gamm)
# eps = split(eps)
# Dgamm =0
# Deps=0
# lenGamm = len(gamm)
# for i in range(lenGamm):
#     Dgamm += int(gamm[i])*(2**(lenGamm-i-1))    
#     Deps += int(eps[i])*(2**(lenGamm-i-1)) 
       
# print(Dgamm*Deps)        
#========================================= Part Two ==========================================

ogr = 0
z = 0
o = 0
csr = 0
ins=[]
for i in range(12):
    
    z = 0
    o = 0
    for n in range(len(inputs)):
        input = inputs[n]
        input = split(input)
        if int(input[i]) == 0:
            o+=1
        else:
            z+=1    
    if o > z :
        for b in range(len(inputs)):
            inputt = inputs[b]
            inputt = split(input)
            if int(inputt[i])==1:
                ins.append(inputs[b])
    elif o < z:
        for b in range(len(inputs)):
            inputt = inputs[b]
            inputt = split(input)
            if int(inputt[i])==0:
                ins.append(inputs[b])
print(ins)                 

            




