def func():
    print("module Inside one.py")

print("one.py at indentation level 0")

func()

if __name__ =="__main__":
    print("One.py running directly")
else:
    print("one.py running under import")
