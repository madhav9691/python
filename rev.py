def reverse(n):
    s1=0
    while n>0 :
        rem=n%10
        s1=s1*10+rem
        n=n//10
    return(s1)
#reverse(10)
    


