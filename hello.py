x = int(input("x: "))
y = int(input("y: "))

try:
    result = x / y
except ZeroDivisionError:
    print(" you can't devide by Zero")
    sys.exit(1)

print(f"{x} / {y} = {result}")