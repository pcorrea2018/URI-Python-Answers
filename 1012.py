a, b, c = input().split()

a = float(a)
b = float(b)
c = float(c)

pi = 3.14159

tri=(a*c)/2
cir=pi*c**2
trap=(c*(a+b))/2
quad=b**2
ret=a*b

print("TRIANGULO: %0.3f\n" %tri +
      "CIRCULO: %0.3f\n" %cir +
      "TRAPEZIO: %0.3f\n" %trap +
      "QUADRADO: %0.3f\n" %quad +
      "RETANGULO: %0.3f" %ret)
