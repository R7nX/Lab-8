from datetime import datetime

def checknumber(user_input):
    number=["0","1","2","3","4","5","6","7","8","9","."]
    low = user_input.lower() 
    num=0  
    for input_length in range(len(user_input)+1): 
        for cut_place in range(1,input_length+1): 
            digit_cut=slice(cut_place-1,cut_place)
            if low[digit_cut] not in number:
                num=1
    return num

def is_int(user_input):
    if float(user_input)%1==0:
        return print(int(user_input),"is an integer")
    else:
        return print(user_input, "is not an integer")
    
def is_prime(num):
    int(num)
    so_uoc=0
    for i in range (1,num+1): 
        if num%i==0:
            so_uoc+=1
    if num<2: 
        return print(f"{num} is not a prime")
    else: 
        if so_uoc==2: 
            return print(f"{num} is a prime")
        elif so_uoc>2: 
            return print(f"{num} is not a prime ")

def count(num): # hàm trả về snt
    so_uoc=0
    for y in range (1,num+1):
        if num% y==0:
            so_uoc+=1
    return so_uoc

def first_prime(n):
    snt=2
    num=0
    while num!=n:
        if count(snt)==2:
            print(snt, end =" ")
            num+=1
        snt+=1

def time_now():
    now = datetime.now()
    return print(f"\n \nToday is", now.strftime("%d:%m:%Y") + "\n" + "Time right now:", now.strftime("%H:%M:%S"))

def sum_fac(x):
    sum = 0
    def fac(x): 
        fact = 1    
        if x == 0 or x == 1:
            return fact
        else:
            for i in range(2, x+1):
                fact = fact * i
            return fact
    for i in range(0, x):
        sum = sum + fac(i)
    return print(f"Result: {sum}")



def main():
    user_input = input("Input: ")
    checknumber(user_input)

    while(checknumber(user_input) != 0):
        print("Invalid input. Please input again ")
        user_input=input("Input: ")
    
    is_int(user_input)
    print("\n")

    a = input("Input a number: ")
    while(checknumber(a) != 0):
        print("Invalid input. Please input again ")
        a=input("Input: ")
    is_prime(int(a))
    print("\n")

    n=int(input("Input number: "))
    while n<=0: 
        n=int(input("Input number: "))
    first_prime(n)

    time_now()
    print("\n")

    x = int(input("Input a number: "))	
    sum_fac(x)
    print("\n")

if __name__=="__main__":
    main()
