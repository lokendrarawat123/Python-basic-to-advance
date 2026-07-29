# write a program to find simple intrest using input function 
principle =float(input("enter the principal in rs =  "))
time=float(input("enter the time in year = "))
rate=float(input("enter the intrest rate in percent = "))
simple_intrest=(principle*time*rate)/100
print(f" total simple intrest = " , simple_intrest)