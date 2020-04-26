
f=open('rev_file.txt','r')
lines_count=0
words_count=0
chars_count=0
for line in f:
    lines_count+=1
    chars_count+=len(line)
    words_count+=len(line.split())
                 
print("number of lines=",lines_count)
print("number of words=",words_count)
print("number of characters=",chars_count)
    
