"""Write a program to generate the Fibbonacci series."""

length=int(input("Enter the length of Fibbonacci series: "))   #receiving length of series
num1=0
num2=1
i=0                                                            #initializing the iteration i
print(num1)
print(num2)
while(i<=length):                                               #using while loop till condition of length get successful
    num=num1+num2
    num1=num2
    num2=num
    print(num)
    i+=1                                                        #incrementing
