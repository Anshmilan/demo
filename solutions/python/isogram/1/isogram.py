def is_isogram(string):
    new_str=string.replace(" ","")
    new_str1=new_str.replace("-","")
    set_sam=set(new_str1.lower())
    list_sam=list(new_str1.lower())
    string1=list( ''.join(set_sam))
    string2=list( ''.join(list_sam))
    if sorted(string1)==sorted(string2):
        return True
    else:
        return False

