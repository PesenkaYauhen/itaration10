import itertools

n = 0

m = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = list(itertools.permutations(m))
# print( x)
print('dlinna', len(x))
for i in range(0, len(x)):  # 3628800
    for j in range(0, len(m) - 1):
        # for r in range(len(m) -1- j):
        # print(j)
        q = 1
        while j + q < len(m):
            # print(x[i][j])
            if x[i][j] > x[i][j + q]:
                n += 1
                # print(n)
            q += 1

print("iteracii", n)
#n = 81648000