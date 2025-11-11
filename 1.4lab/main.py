N = int(input())
A = int(input())
B = int(input())

result = [A, B]

for i in range(2, N):
    next_element = sum(result)
    result.append(next_element)

print(result)
