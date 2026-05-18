def fibonanci_series(N,a=0,b=1):
    counter=0
    while counter<N:
        a,b=b,a+b
        print(a,end=" ")
        counter=counter+1
N=int(input("enter the range for fibonanci series: "))
fibonanci_series(N)