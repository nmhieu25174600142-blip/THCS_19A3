n=int(input("Nhap n: "))
if n > 1:
    sieve=[True]*n
    sieve[0]=sieve[1]=False
    for i in range(2,int(n**0.5)+1):
        if sieve[i]:
            for j in range(i*i,n,i):
                sieve[j]=False
    print([i for i,v in enumerate(sieve) if v])
else:
    print([])
