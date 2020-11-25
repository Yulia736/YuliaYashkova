1.
print("Введите число A= ")
A=int(input())
print("Введите число B= ")
B=int(input())
if A<B:
	for i in range (A,B+1):
		print(i)
if A>B:
	for i in range (A,B-1,-1):
		print(i)
2.
a=int(input())
b=int(input())
c1=a//1000
c2=a//100%10
while (((c1*10+c2)*10+c2)*10+c2)<=b:
    print(c1,c2,c2,c1,sep="")
    c2=c2+1
    if (c2>9):
        c1=c1+1
        c2=0 

