""" Use while loop - to prove Collatz's hypothesis

    1. take any non-negative and non-zero integer number and name it c0;
    2. if it's even, evaluate a new c0 as c0 ÷ 2;
    3. otherwise, if it's odd, evaluate a new c0 as 3 × c0 + 1;
    4. if c0 ≠ 1, skip to point 2.
        The hypothesis says that regardless of the initial value of c0, it will always go to 1
"""
c0 = int(input("Enter a non-negative and non-zero interger : "))
steps = 0

while c0!= 1:
    if not c0%2:
        c0 = c0/2
    else:
        c0 = 3*c0 +1
    steps +=1
    print(int(c0))
print("steps = ", steps)    
    