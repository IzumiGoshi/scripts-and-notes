order = ['A', 'B', 'C', 'D', 'E']
threes = []
BUFA = [['A'], ['B'], ['C'], ['D'], ['E']]
BUFB = []

while True:
    added_combination = False
    for BA in BUFA:
        BA_last = BA[-1][-1]
        BAi = order.index(BA_last)

        for i in range(BAi + 1, len(order)):
            BUFB.append(BA + [ order[i] ])
            added_combination = True

        if len(BA) == 3:
           threes.append(BA)
    
    BUFA = BUFB
    BUFB = []

    if not added_combination: break
'''
        Contents fo threes after is:

        0 :  ['A', 'B', 'C']
        1 :  ['A', 'B', 'D']
        2 :  ['A', 'B', 'E']
        3 :  ['A', 'C', 'D']
        4 :  ['A', 'C', 'E']
        5 :  ['A', 'D', 'E']
        6 :  ['B', 'C', 'D']
        7 :  ['B', 'C', 'E']
        8 :  ['B', 'D', 'E']
        9 :  ['C', 'D', 'E']
'''
