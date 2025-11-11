lst = list(map(int, input().split()))
even_positions = lst[::2]
even_positions.sort()
print(even_positions)
