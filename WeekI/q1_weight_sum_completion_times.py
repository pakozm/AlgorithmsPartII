import sys
f = open(sys.argv[1])
N = int(f.readline().rstrip())
data = [ map(int, x.rstrip().split()) for x in f.readlines() ]
# [0] is weight, [1] is length
data = [ ( x[0], x[1], x[0] - x[1] ) for x in data ]
def compare(a,b):
    if a[2] < b[2]: return 1
    elif a[2] > b[2]: return -1
    else:
        if a[0] < b[0]: return 1
        elif a[0] > b[0]: return -1
        else: return 0

data.sort(cmp=compare)

time = 0
result = 0
for w,l,d in data:
    time += l
    result += w * time

print result
