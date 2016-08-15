print("Questão p.4 - 30")
print("")
num = 1
for num in range(1,51):
    print(num)
    num = num + 1
print("")

print("Questão p.4 - 31")
print("")
num = 2
while (num <= 100):
    print(num)
    num = num + 2
print("")

print("Questão p.4 - 32")
print("")
num = 10
while (num <= 1000):
    print(num)
    num = num + 10
print("")

print("Questão p.4 - 33")
print("")
num = 100
while (num != 1):
    print(num)
    num = num-1
print(num)
print("")

print("Questão p.4 - 34")
print("")
N = int(input("Informe um número: "))
num = 1
soma = 0
while (num <= N):
    soma = soma + num
    num = num + 1
    continue
print("A soma dos números é igual a: ", soma)
