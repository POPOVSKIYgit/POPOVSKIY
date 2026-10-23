n = int(input())

r1 = " ".join("+___" for _ in range(n))
r2 = " ".join(f"|{i} /" for i in range(1, n + 1))
r3 = " ".join("|__\\" for _ in range(n))
r4 = " ".join("|   " for _ in range(n))

print(r1)
print(r2)
print(r3)
print(r4)