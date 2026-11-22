def match_word(words):
    ctr = 0
    lst = []
    for word in words :
        if len(word) > 1 and word[0] == word[-1]:
            ctr+=1
            lst.append(word)
    print("List of word with same first and last letters\n " , lst)
    return ctr
count = match_word(['abc' , 'vsdfgv' , 'dgdfd' , '12345654321' , '1221' , 'zxz' , 'wrgfgsdf' , '3245' , 'fsfdgfdgf'])
print("NO. of word having first and last letter same are : " ,  count)
