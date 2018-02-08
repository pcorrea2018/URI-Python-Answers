d = int(input())

a = d//365
m = (d%365)//30
di = (d%365)%30

print("%d ano(s)\n" %a + "%d mes(es)\n" %m + "%d dia(s)" %di)
