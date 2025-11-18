def gcd(a,b):
    a,b=abs(a),abs(b)
    while b:
        a,b=b,a%b
    return a

num=int(input("Nhap tu: "))
den=int(input("Nhap mau: "))
g=gcd(num,den)
num//=g
den//=g
if den<0:
    num=-num
    den=-den
print(f"{num}/{den}")
