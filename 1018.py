n = int(input())

c=n//100
ci=(n%100)//50
v=((n%100)%50)//20
d=(((n%100)%50)%20)//10
cin=(((n%100)%50)%10)//5
do=((((n%100)%50)%10)%5)//2
u=((((n%100)%50)%10)%5)%2

print("%d\n" %n + "%d nota(s) de R$ 100,00\n" %c + "%d nota(s) de R$ 50,00\n" %ci + "%d nota(s) de R$ 20,00\n" %v + "%d nota(s) de R$ 10,00\n" %d + "%d nota(s) de R$ 5,00\n" %cin + "%d nota(s) de R$ 2,00\n" %do + "%d nota(s) de R$ 1,00" %u)
