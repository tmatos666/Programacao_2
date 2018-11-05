import re
#Ex1
"""string_a_comparar = ["Jan 1987", "May 1969", "Aug 2011"]
pattern = re.compile(r"(\w+\s(\d+))")
for i in string_a_comparar:
    s = re.findall(pattern, i)
    print(i,": ", s)
"""

#Ex2
"""string_a_comparar = ["1280x720", "1920x1600", "1024x768"]
pattern = re.compile(r"((\d+)x(\d+))")
for i in string_a_comparar:
    s = re.search(pattern, i)
    print(i,": ", s.group(2)," -- ", s.group(3))
"""
#Ex3
"""string_a_comparar = ["I love cats", "I love dogs","I love logs",
"I love cots"]
pattern = re.compile(r"I\slove\scats|I\slove\sdogs")
for i in string_a_comparar:
    s = re.findall(pattern, i)
    print(i,": \t", s)
"""

#Ex4
"""string_a_comparar = ["-255", "+128","-1910","720p"]
pattern = re.compile(r"^-?\d+$")
for i in string_a_comparar:
    s = re.search(pattern, i)
    print(i,": \t", s)
"""

#Ex5
"""string_a_comparar = ["415-555-1234", "650-555-2345","(416)555-3456"
,"202 555 4567","4035555678","1 416 555 9292"]
pattern = re.compile(r"(\d{3})")
for i in string_a_comparar:
    s = re.findall(pattern, i)
    print(i,": \t", s)
"""

#Ex6
"""string_a_comparar = ["tom@hogwarts.com", "tom.riddle@hogwarts.com",
"tom.riddle+regexone@hogwarts.com"
,"tom@hogwarts.eu.com","potter@hogwarts.com","harry@hogwarts.com",
"hermione+regexone@hogwarts.com"]
pattern = re.compile(r"^([\w\.]*)")
for i in string_a_comparar:
    s = re.findall(pattern, i)
    print(i,": \t", s)
"""

#Ex7
"""string_a_comparar = ["<a>This is a link</a>", 
"<a href='https://regexone.com'>Link</a>",
"<div class='test_style'>Test</div>",
"<Frame>Hello <span>world</span></div>"]
pattern = re.compile(r"^<(\w+)")
for i in string_a_comparar:
    s = re.findall(pattern, i)
    print(i,": \t", s)
"""

#Ex8
"""europa=[]
pattern = re.compile(r"pais\((\w*),.*")
with open("../europeCountries.txt") as mytxt:
    for line in mytxt:
        #print(line,end='')
        s = re.findall(pattern, line)
        europa.append(s[0])
mytxt.close()

f = open("../listaPaises.txt", "+w")
s = 1
for i in europa:
    text = "{} - {}\n".format(s, i)
    f.write(text)
    s += 1 
f.close()
"""

#Ex9  - email validator
"""emails = []
pattern = re.compile(r"^[\w.+-]+@\w+[.-]?\w+\.[a-zA-Z]{2,3}$")
with open("../emailValidator.txt") as mytxt:
    for line in mytxt:
        s = re.findall(pattern, line)
        #print(line,": \t", s)
        if len(s)>0:
            emails.append(s[0])
mytxt.close()

f = open("../validEmails.txt", "+w")
for i in emails:
    f.write(i+'\n') 
f.close()
"""

#Ex10
"""invPasswords = []
#mytxt = ["7 characters: o%THiS1", "16 characters: DidIanswerYour1Q"
#,"7: 9lB019$","16: 6l80UK! 122UkTfrl","5 characters: oHi66S1+"]
pattern = re.compile(r".*:\s(.*)")
with open("../passwordValidator.txt") as mytxt:
    for i in mytxt:
        s = re.findall(pattern, i)
        otherPattern = re.compile(r"^[\w%+-]{6,12}$")
        s1 = re.findall(otherPattern, s[0])
        if len(s1) == 0:
            #print(i,": \t", s1[0])
            invPasswords.append(s[0])
   
f = open("../invalidPasswords.txt", "+w")
for i in invPasswords:
    f.write(i+'\n') 
f.close()"""