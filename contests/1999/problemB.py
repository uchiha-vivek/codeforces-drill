from itertools import permutations

def winning_probability(a1,a2,b1,b2):
    sunnet_cards = [a1,a2]
    slavic_cards = [b1,b2]
    win_count = 0
    for s_order in permutations(sunnet_cards):
        for sl_order in permutations(slavic_cards):
            s_rounds = 0
            sl_rounds = 0
            for i in range(2):
                if s_order[i]>sl_order[i]:
                    s_rounds+=1
                elif s_order[i]<sl_order[i]:
                    sl_rounds+=1
            if s_rounds>sl_rounds:
                win_count+=1
    return win_count

 
t:int = int(input())

for _ in range(t):
    a1,a2,b1,b2 = map(int,input().split())
    ans=winning_probability(a1,a2,b1,b2)
    print(ans)