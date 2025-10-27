def response(hey_bob):
    hey=hey_bob.strip()
    if hey_bob.strip()=='':
        return "Fine. Be that way!"
    else:   
        if hey[-1]=='?'and hey.isupper()!=True:
            return "Sure."
        elif hey.isupper() and  hey[-1]!='?':
            return "Whoa, chill out!"
        elif hey.isupper() and hey[-1]=='?':
            return "Calm down, I know what I'm doing!"       
        else:
            return "Whatever."
        
