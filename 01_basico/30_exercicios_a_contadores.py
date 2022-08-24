i = 0
j = 10

print()

while i <= 10:
    print(f'i: {i} || j: {j}')
    i += 1
    j -= 1

print()

for p, r in enumerate(range(10, 1, -1)):
    print(p, r)