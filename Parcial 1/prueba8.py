num1 = 3
num2 = 7
num3 = 4

if num2 % 2 != 0:             # ← PRIMER CASILLA: !=
    x = 3 * num2
else:
    x = num2 * 2

if x % 2 == 0:
    t = x + num3
else:
    t = x - num3

if t > 10:                    # ← SEGUNDA CASILLA: >
    resultado_final = t * num1
else:
    resultado_final = t + num1

print(f"Resultado final: {resultado_final}")
