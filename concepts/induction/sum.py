# 1+2+3+...... = n*(n+1)//2
# put n=1 and compare LHS and RHS , 1==1 --> True
# assume its true for n=k
# 1+2+.....+k = k*(k+1)//2 ---->(1)

# proving  its true for n=k+1
# 1+2+3+ .......+k+k+1 = (k+1)(k+2)//2



def inductive_proof(k:int):
    # Taking the base case 
    # k=1
    # general formula : n*(n+1)//2
    left_base_case:int = sum(range(1,2))
    right_base_case:int = 1*(1+1)//2
    print(f'left sum is : {left_base_case} and right sum is : {right_base_case}')

    # assuming it holds true for n=k
    left_k_case:int = sum(range(1,k+1))
    right_k_case:int = k*(k+1)//2
    print(f'left sum is : {left_k_case} and right sum is : {right_k_case}')


    # proving it true for n=k+1
    lhs_new_k:int = left_k_case + (k+1)
    rhs_new_k:int = (k+1)*(k+2)//2
    print(f'left sum is : {lhs_new_k} and right sum is : {rhs_new_k}')

if __name__=="__main__":
    inductive_proof(3)