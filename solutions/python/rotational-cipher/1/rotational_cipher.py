def rotate(text, key):
    word_list=list(text)
    key_value=key
    alpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    new_list=[]
    for i in word_list:
        if i!=" ":
            value=i.lower()
            try:
                cur_pos=alpha.index(value)
            except ValueError as e:
                new_list.append(i)
                continue
            if (25-cur_pos)>key_value:
                pos=cur_pos+key_value
                cur_test=alpha[pos]
            else:
                pos=abs(key_value-(25-cur_pos))
                cur_test=alpha[pos-1]
            if value==i:
                new_list.append(cur_test)
            else:
                new_list.append(cur_test.upper())
        else:
           new_list.append(" ")
    return ''.join(new_list)
        
