masses = {
    'H':1.0079,
    'C':12.011,
    'N':14.007,
    'O':15.999,
    'S':32.06,
    'Cl':35.45,
    'Fe':55.845,
    'Og':294    
}
formula = []

for i in range(6):
    list1 = input().split()
    formula.append(list1)
    if not input():
        break

for i in range(len(formula)):
    if int(formula[i][1]) == 1:
        print(formula[i][0],end = '')
    else:
        print(formula[i][0],formula[i][1],end = '')