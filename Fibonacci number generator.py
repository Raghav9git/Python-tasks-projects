print("Generate Fibonacci numbers")
Fn = int(input("How many fibonacci numbers do you want = "))
i=0
j=1
counting=0

if Fn <= 0:
    print("Please enter a positive number")
elif Fn == 1:
    print("Your Fibonacci sequence = ",j)
else:
    print("Your Fibonacci sequence = ")
    while counting < Fn:      # prints till the counting is just less than Fn
        print(i)
        i,j = j,i+j           # touple assignment - i becomes currnt value of  j 
        counting += 1                           # - j becomes current value of i+j
