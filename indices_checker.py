mdmids = []
originids = []
uniqueids = []

with open('originids') as f:
    for line in f:
        originids.append(int(line))

with open('mdmids') as f:
    for line in f:
        mdmids.append(int(line))

print('Origin IDs:')
print(len(originids))

for i in range (0, len(originids)):
    if not originids[i] in mdmids:
        uniqueids.append(originids[i])

print('Unique IDs:')
print(len(uniqueids))
