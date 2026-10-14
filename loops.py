
for i in range(5):
    print("Hello")

for i in range(1, 6):
    print(i)

i = 1

while i <= 5:
    print(i)
    i = i + 1

for i in range(1, 6):
    if i == 3:
        break
    print(i)

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

for i in range(1, 4):
    for j in range(1, 3):
        print(i, j)
