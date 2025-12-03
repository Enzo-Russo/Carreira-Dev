a = 'Enzo'
b = 'Russo'
c = 'Santos'
d = 1.1

a2 = 'Enzo'
b2 = 'Russo'
c2 = 'Santos'
d2 = 1.1

string = 'a={nome1} b={nome2} c={nome3} d={nome4:.2f}'
string2 = 'a={0} b={1} c={2} d={3:.2f}'
# string.format(nome1=a, nome2=b, nome3=c, nome4=d) - transforma em parâmetro.
# a função que estiver dentro do objeto se torna um método (method), format está dentro da variavel string
formato = string.format(nome1=a, nome2=b, nome3=c, nome4=d)
formato2 = string2.format(a2, b2, c2, d2)
print(formato)
print(formato2)