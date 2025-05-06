
# mathematics and mathemcatical induction

t:int = int(input())

for _ in range(t):
    n,m,l,r = map(int,input().split())
    # A bit mathematical induction
    # for nth day we get n+1 steps
    # general formula [l,r] ==> l<r thus r-l+1=n+1 
    # for day 0 we have segment [0,0] , here l=0 and r=0 so 0-0+1 = o+1 . Holds True 😊
    # on day m it is [lm,rm] so rm-lm+1 = m+1
    # for m+1 it is [l(m+1),r(m+1)] so r(m+1) - l(m+1) +1 = (m+1)+1

    # On simplifying the above equation
    # r(m+1) -l(m+1)+1  =(m+1)+1
    # rm +r -lm -l +1 = m+2
    # (r-l)(m) = m+1 ..........(1)
    # (r-l)(m+1)=(m+1) +1 .......(2)
    # from eq 1 and 2 if its true for m then its also true for (m+1)

    length:int = m+1
    L_prime = 1
    R_prime = l+length-1
    print(L_prime,R_prime) 