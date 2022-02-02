from posixpath import split


forward = 1
down = 1
up = -1 
px = 0
aim = 0
depth = 0
inputs = open('input.txt','r').readlines()

for i in range(len(inputs)):
    gpos = inputs[i].split(' ')
    dir = str(gpos[0])
    pos = int(gpos[1])

    if dir == 'forward':
        depth += pos*aim
        px += pos
    if dir == 'down':
        # depth += pos
        aim += pos
    if dir == 'up':
        aim -= pos
        # depth -= pos    
        
    
print(depth*px)