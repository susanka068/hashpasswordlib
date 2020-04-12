import re

import sys,random,string,math

def random_id(length):
    no = '0123456789'
    alpha = 'qwertyuioplkjhgfdsazxcvbnm'
    symbs = string.punctuation
    id=''
    while(True):
        if(len(id)==length):
            break
        id+= random.choice(no)
        if(len(id)==length):
            break
        id+= random.choice(alpha)
        if(len(id)==length):
            break
        id+= random.choice(symbs)

    return (id)


def my_hash_tool(my_word):

    for char in string.punctuation:
        my_word = my_word.replace(char,"")


    my_word = my_word.replace(" ","")
    hash_table_1= dict(a='qwe',A='trt',b='yqe',B='jqw',c='iey',C='pqj',d='pai',D='mbu', e='unb',E='nai',f='yta',F='opq',g='nuy',G='uy7',h='hi2',H='nug', i ='nt2', I='kgs', j ='jiq', J='ibz', k ='yug', K='iy5', l ='byg', L='vl2', m ='vz8', M='gy2', n ='jq7', N='mz5', o ='12t', O='jaq', p ='bv1', P='69v', Q ='jf4', q='hg1', r ='98g', R='8bw', s ='di5', S='nc2', t ='izk', T='ub2', u ='nvo', U='hl2', V ='ef3', v='uy3', w ='hzn', W='jd2',x ='uo1', X='nxx', y ='ihl', Y='t3u',z ='13b', Z='10d')
    Key_list = list(hash_table_1.keys())

    Value_list = list(hash_table_1.values())
    a= my_word
    length_word =  len(a)
    pwd=""
    total_length = pow(2 , length_word) + pow(-1,length_word)
    for  word in a:
        new = word
        if(new in Key_list):
            occ = Key_list.index(new)
            val_occ = Value_list[occ]
            pwd = pwd + val_occ

    length_hashed = len(pwd)
    subtracted_len =  total_length - length_hashed
    random_chars = random_id(subtracted_len)
    ultimate_pwd = pwd + random_chars
    return (ultimate_pwd)


def get_main_pwd(hashed_pwd):
    lngth = len(hashed_pwd)
    powerval = math.log(lngth , 2)
    actual_powerval = (math.ceil(powerval)) -1
    temp=[]
    q = (actual_powerval*3)
    for item in range(0,q):
        temp.append(hashed_pwd[item])
    newstr="".join(temp)

    return newstr


//how to call the functions and check them

a_2 = my_hash_tool("weqtt())?>:+*&%##$^#$")
a_1 = get_main_pwd(a_2)

