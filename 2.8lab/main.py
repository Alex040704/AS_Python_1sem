with open('f.txt', 'r') as f:
    numbers = list(map(int, f.read().split()))

positives = [x for x in numbers if x > 0]
negatives = [x for x in numbers if x < 0]

result = []
for i in range(0, len(positives), 2):
    result.extend([positives[i], positives[i+1], negatives[i], negatives[i+1]])

with open('g.txt', 'w') as g:
    g.write(' '.join(map(str, result)))
