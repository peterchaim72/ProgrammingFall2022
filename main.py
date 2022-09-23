# introductory example of a function from replit.com
# 8/30/2022 Peter Weinstein. added comments.

# return n! ("n factorial")
def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)

# main function    
print(factorial(6))

