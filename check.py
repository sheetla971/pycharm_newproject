def check(a,b):
    if a>b:
        return a
    else:
        return b
a=input("first number:")
b=input("second number:")
a,b=int(a),int(b)
print(check(a,b))
