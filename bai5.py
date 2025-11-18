def S1(n): return n*(n+1)//2
def S2(n):
    if n<=1: return 1
    r=1
    for i in range(1,n): r*=i
    return r
def S3(n):
    s=0
    for i in range(1,n+1):
        s+=((-1)**(i+1))/i
    return s
def S4(n):
    s=0
    for k in range(n+1):
        s+=k/(k+2)
    return s

n=int(input("Nhap n: "))
print("S1 =",S1(n))
print("S2 =",S2(n))
print("S3 =",S3(n))
print("S4 =",S4(n))
