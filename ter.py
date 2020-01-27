def check(a,b):
    return a if a>b else b
a=input("first number:")
b=input("second number:")
a,b=int(a),int(b)
print(check(a,b))