# Completa el siguiente codigo para que el valor de r al finalizar la ejecucion sea "ruel"

f = "HolaMundoCruel"
r = f
l = len(f)

for i in range(0, l + 1, 5):
    r = f[i:l]

print(r)