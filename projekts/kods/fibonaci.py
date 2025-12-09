fibonaci = [0, 1]

while len(fibonaci) < 100:
    fibonaci.append(fibonaci[-1] + fibonaci[-2])

for sk in reversed(fibonaci):
    print(sk, end=' ')
