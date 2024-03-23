n=int(input())

for i in range(1,n+1):
    for j in range(1,i+1):
        print("*", end=" ")
    print()




# python3 code to print pyramid pattern using while loop
n=5;i=0
while(i<=n):
  print(" " * (n - i) +"*" * i) 
  i+=1