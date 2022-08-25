def factorial(n):
  if n == 0:
    return 1
  else:
    x = n+1
    print("debugging am here " + str(x))
    return n * factorial(n - 1)
print(factorial(6))
print("can i stop at a breakpoint please?")
y = 27
y = y*2
print(y)
