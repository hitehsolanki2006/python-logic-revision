def vowelsconsonants(line):
    vowels="aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    spece=" "
    vowelacount=0
    consonantscout=0
    spececount=0
    for i in line:
        if i in vowels:
            vowelacount+=1
        elif i in consonants :
            consonantscout+=1
        elif i in spece:
            spececount+=1
    count={"Vowels Count ":vowelacount,"Consonants Count":consonantscout,"Space Count":spececount}
    return count