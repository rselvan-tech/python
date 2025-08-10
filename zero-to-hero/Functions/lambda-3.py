def my_fun(x,fn):
    return fn(x)

result=my_fun("a:b:c",lambda a: a.split(":"))
print(result)