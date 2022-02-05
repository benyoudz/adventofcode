import copy
def split(bin):
    return [num for num in bin]
Binaries=open('input.txt','r').readlines()
o0=copy.deepcopy(Binaries)
o1=[]
o2=[]
o3=[]
o4=[]
o5=[]
o6=[]
o7=[]
o8=[]
o9=[]
o10=[]
o11=[]
o12=[]
aa=[o0,o1,o2,o3,o4,o5,o6,o7,o8,o9,o10,o11,o12]
# =====================First==============================
z=0
o=0
for i in range(len(Binaries)):
    if int(split(Binaries[i])[0]) == 0:
        z+=1
    else:
        o+=1
if z>o:
    for n in range(len(Binaries)):
        if int(split(Binaries[n])[0]) == 1:
            if Binaries[n] in o0:
                o0.remove(Binaries[n])
else:
    for n in range(len(Binaries)):
        if int(split(Binaries[n])[0]) == 0:
            if Binaries[n] in o0:
                o0.remove(Binaries[n])                         
# =======================rest============================
for bit in range(len(split(o0[0]))-1):
    z= 0
    o= 0
    if bit > 0:
        if len(OnP) != 1:
            On = copy.deepcopy(aa[bit-1])
        else:
            On = OnP
        aa[bit]=On

        OnP = aa[bit-1]
    else:
        On = o0
        OnP = Binaries           
    for bin in range(len(OnP)):
        if int(split(OnP[bin])[bit])+1 >0:
            if int(split(OnP[bin])[bit]) == 0:
                z+=1
            else:
                o+=1     
        else:
            z=z
            o=o        
    if z>o:
        for bin in range(len(OnP)):
            if int(split(OnP[bin])[bit])+1 >0:
                if int(split(OnP[bin])[bit]) == 1:
                    if OnP[bin] in On:
                        On.remove(OnP[bin])   
    else:
        for bin in range(len(OnP)):
            if int(split(OnP[bin])[bit])+1 >0:
                if int(split(OnP[bin])[bit]) == 0:
                    if OnP[bin] in On:
                        On.remove(OnP[bin])                  
#========================CO2 scrubber rating===============================
co0=copy.deepcopy(Binaries)
co1=[]
co2=[]
co3=[]
co4=[]
co5=[]
co6=[]
co7=[]
co8=[]
co9=[]
co10=[]
co11=[]
co12=[]
a=[co0,co1,co2,co3,co4,co5,co6,co7,co8,co9,co10,co11,co12]
# =====================First==============================
zz=0
oo=0
for i in range(len(Binaries)):
    if int(split(Binaries[i])[0]) == 0:
        zz+=1
    else:
        oo+=1
if zz>oo:
    for n in range(len(Binaries)):
        if int(split(Binaries[n])[0]) == 0:
            if Binaries[n] in co0:
                co0.remove(Binaries[n])
else:
    for n in range(len(Binaries)):
        if int(split(Binaries[n])[0]) == 1:
            if Binaries[n] in co0:
                co0.remove(Binaries[n])                         
# =======================rest============================
for bit in range(len(split(co0[0]))):
    zz= 0
    oo= 0
    if bit > 0:
        if len(CnP) != 1:
            Cn = copy.deepcopy(a[bit-1])
        else:
            Cn = CnP
            Cn =Cn
        a[bit]=Cn

        CnP = a[bit-1]
    else:
        Cn = co0
        CnP = Binaries           
    for bin in range(len(CnP)):
        if int(split(CnP[bin])[bit]) == 0:
            zz+=1
        else:
            oo+=1     
    if zz>oo:
        for bin in range(len(CnP)):
            if int(split(CnP[bin])[bit]) == 0:
                if CnP[bin] in Cn:
                    Cn.remove(CnP[bin])   
    else:
        for bin in range(len(CnP)):
            if int(split(CnP[bin])[bit]) == 1:
                if CnP[bin] in Cn:
                    Cn.remove(CnP[bin])
        # ============================================
BCn=[]
BOn=[]
for i in range(len(split(Cn[0]))-1):
    BCn.append(split(Cn[0])[i])
    BOn.append(split(On[0])[i])
Cn= BCn
On = BOn
Dcn =0
Don=0
length = len(On)
# Script For Convert Binary To Decimal 'D' Reference Decimals & 'B' Reference Binarys
for i in range(length):
    Dcn += int(Cn[i])*(2**(length-i-1))    
    Don += int(On[i])*(2**(length-i-1))  
print('O2 Rate => ',Don,'  Co2 Rate=>',Dcn)    
print('the life support rating of the submarine Is =',Dcn*Don)
