import re
s1='''kavya is an optimist
    swathi is a short girl
    anusha is a good girl
    bhaskar is a cricket player
    satish is a regular student'''
obj=re.search("bhaskar",s1)
print(obj)
if obj:
    print("result=",obj.group())
