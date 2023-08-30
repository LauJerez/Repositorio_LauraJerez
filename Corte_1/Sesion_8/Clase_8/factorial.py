def factorial(x):
    a=1
    for i in range(x):   
        a*=(i+1)  #a=a*(i+1)
    return a

if __name__=="__main__":
    factorial(4)