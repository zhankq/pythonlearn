def count_str_char(my_str):
    englistwords = "abcdefghijklmnopqrstuvwxyz"
    englistwordsuper = englistwords.upper()
    mathword = "0987654321"
    englistwords_num = other_num = mathword_word=0
    for i in my_str:
        if i in englistwords or i in englistwordsuper:
            englistwords_num += 1
        elif i in mathword:
            mathword_word+=1
        else:
            other_num+=1
    return (englistwords_num,other_num,mathword_word)

englistwords_num , other_num , mathword_word = count_str_char("ad3234~!@$~")

print(englistwords_num , other_num , mathword_word)