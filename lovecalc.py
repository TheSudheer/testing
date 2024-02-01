print("welcome to the love calculator.")
name_1=input("what is U R name?  \n")
name_2=input("what is their name?  \n")
combined_string=name_1 + name_2

lower_case_string=combined_string.lower()

print(lower_case_string)

t=lower_case_string.count("t")
r=lower_case_string.count("r")
u=lower_case_string.count("u")
e=lower_case_string.count("e")

true= t + r + u + e

l=lower_case_string.count("l")
o=lower_case_string.count("o")
v=lower_case_string.count("v")
e=lower_case_string.count("e")

love= l + o + v + e 

love_score=int(str(true)+ str(love))

if (love_score>10) or (love_score<90):
    print(f"Your love score is {love_score}, you go together like Coke and Mentos.")
elif (love_score>40) and (love_score<50):
    print(f"Your love score is{love_score}, you go together like chilaka gorinka.")
else:
    print(f"Your love score is{love_score}")










