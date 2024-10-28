def total_calc(bill_amount,tip perc):
    total = bill_amount*(1 + 0.01*tip_perc)
    total = round(total,2)
    print(f"pleasea pay ${total}")
total_calc(150,20)
def factorial(x):
    '''this is a recursive function to find the factorial of a integer'''
    if x==0 or x==1
        return 1
    else:
       return x*factorial(x-1)
print(factorial.__doc__)
print("the factorial of 0:",factorial(0))      
print("the factorial of 1:",factorial(1))
print("the factorial of 2:",factorial(2))
print("the factorial of 5:",factorial(5))
print("the factorial of 10:",factorial(10))