def gcd(a,b):
    a,b=abs(a),abs(b)
    while b:
        a,b=b,a%b
    return a

a=int(input("Nhap a: "))
b=int(input("Nhap b: "))
print("UCLN =",gcd(a,b))
