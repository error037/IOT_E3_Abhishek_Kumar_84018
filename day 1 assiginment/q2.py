num = int (input("enter the number : "))

print(" The face value : {} ".format(num))
d= num//1000
rd=d
d=d*1000
num=num%1000

c= num//1000
rc=c
c=c*100
num=num%100

b=num//10
rb=b
b=b*10
num=num%10
a=num
ra=num
print(f"place value of number :{d,c,b,a}")
print(f"reverse from number : {ra,rb,rc,rd}")


