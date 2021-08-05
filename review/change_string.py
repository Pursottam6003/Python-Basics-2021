str1 = "wy"
str2 = "gf"
str3 = "u"
trg = "weeksyourweeks"
table = trg.maketrans(str1, str2, str3) 
print (trg.translate(table))