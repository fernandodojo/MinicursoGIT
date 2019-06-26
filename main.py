import soma as s
import subtracao as sub
def calculadora(a, b, operacao):
	if operacao == "+":
		print(s.soma(a,b))
	elif operacao == "-":
		print(sub.sub(a,b))


x = int(input("Digite o primeiro valor"))
y = int(input("Digite o segundo valor"))
op = input("Digite a operação(+, -)")
print("apenas um teste")

calculadora(x, y, op)
