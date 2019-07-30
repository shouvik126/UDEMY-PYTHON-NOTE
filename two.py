from one import func

print("two.py under indentation level 0")

if __name__ == '__main__':
    print("two.py running directly")
    func()
else:
    print("two.py running under import")
