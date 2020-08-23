def valid_credit_card(n):
    n1=[ int( i ) for i in str( n) ][::-1]
    for i in range ( 1, len( n1 ), 2 ): n1[i ]= n1[i ] * 2
    n1=[ n1[i ] % 10 + n1[i ] // 10 if i % 2 else n1[i ] for i in range( len( n1 ) ) ]
    return sum(n1[1:]) * 9 % 10 == n%10

    ######
def valid_credit_card(number):
    new_number_list  =[2*int(val) if idx%2!=0 else int(val) for idx,val in enumerate(str(number)[::-1]) ]
    new_number = "".join(map(str,new_number_list))
    check_list = sum([int(i) for i in new_number])
    return check_list%10==0
    #########
def valid_credit_card(CrdNum):
    CrdNum=str(CrdNum)
    ChDgt=int(CrdNum[-1])
    CrdNum2=list(CrdNum[:-1])
    for i in range(1,len(CrdNum)-1,2):
        if int(CrdNum2[i])>=5:
            CrdNum2.insert(i, str((int(CrdNum2[i])*2)-9))
            CrdNum2.pop(i+1)
        else:
            CrdNum2.insert(i, str(int(CrdNum2[i])*2))
            CrdNum2.pop(i+1)
    print(CrdNum2)
    To=0
    for a in CrdNum2:
        To+=int(a)
    print (To)
    To2=str(To*9)
    print(To2)
    if int(To2[-1])==ChDgt:
        return "Visa Card" 
    else:
        return "Not a valid credit card number"
print(valid_credit_card(37562198673))

#########
number = 7777777777777777
A= list(str(number//10))[::-1]
number1= list(map(lambda x : 2*int(x), A[::2]))
number2= list(map(lambda x : x-9 if int(x)>9 else int(x), number1))
K=list(map(lambda x : int(x), A[1::2]))
print(((sum(K)+sum(number2))*9)%10==number%10)



#####################

def valid_credit_card(number):
    sayi = list(str(number)[::-1])
    for i in range(1, len(sayi),2):
        sayi[i] = int(sayi[i])*2
        if sayi[i] > 9: sayi[i] -= 9
    total = 0
    for i in sayi[1:]: total += int(i)
    return (total * 9)%10 == int(sayi[0])


    ############

    