    1
   12
  123
 1234
12345

a=5
i=1
while(i<=a): # this loop is for printing number of rows
    j=1
    while(j<=a-i): # this will help to print the spaces, 1st line 4 spaces, 2 nd - 3 spaces like that
        print(' ',end='')
        j=j+1
    k=1
    while(k<=i): # helps to pring numbers, 1st line 1 num, 2nd line 2 num
        print(k,end='')
        k=k+1
    print()

    i=i+1
