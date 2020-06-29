# f=open("filesample.py","wb+")
"""f=open("filesample.py","w")
f.write("print('hai')")
f.close()"""
with open("filesample.py", "r") as f:
    x = f.read()
print(x)
