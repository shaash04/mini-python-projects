 #first proj of 60 projects
s=input("Enter the word you want the acronym for")
acronym=""
acronym=acronym+s[0].upper()
if s==" ":
    print("enter a valid string")
else:
    for i in range(len(s)):
        if s[i]==" " and i+1 <len(s):
            acronym+=s[i+1].upper()
    print("Herse's your acronym : {}".format(acronym))
        
        