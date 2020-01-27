a={"a":1,"b":2,"c":4}
b={"d":4,"e":5 ,"f":6}
all_keys=list(a.keys())
all_keys+=list(b.keys())
all_values=list(a.values())
all_values+=list(b.values())
result={}

for keys,values in zip(all_keys,all_values):
    result.update({keys:values})
print(result)
