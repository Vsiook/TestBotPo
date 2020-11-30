dict_game=[
    [None, 'карти1', 'info', 'more info'],
    [None, 'карти2', 'info', 'more info'],
    [None, 'карти', 'info', 'more info'],
    [None, 'карти', 'info', 'more info'],
    [None, 'карти', 'info', 'more info'],
    [None, 'карти', 'info', 'more info'],
    [None, 'карти', 'info', 'more info'],
    [None, 'карти', 'info', 'more info'],
]



def chek_place( ):
    chek_len=0
    for i in range(len(dict_game)):
        if dict_game[i][0]!=None:
            chek_len+=1
    print(chek_len)
    if chek_len ==8:
        return chek_len
    else:return chek_len

chek_place()

def chek_user(id):
    chek_id = 1
    for i in range(len(dict_game)):
        if dict_game[i][0] == id:
            chek_id =0
    return chek_id


# def chek_money():


# def chek_users():