import sys
f = open(sys.argv[1])
N = int(f.readline().rstrip())
data = [ map(int, x.rstrip().split()) for x in f.readlines() ]
# [0] is weight, [1] is length
data = [ ( x[0], x[1], x[0]/float(x[1]) ) for x in data ]
data.sort(key=lambda x: -x[2])
time = 0
result = 0
for w,l,d in data:
    time += l
    result += w * time

print result
