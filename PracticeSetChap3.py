userName = input("Enter your name: \n")
print(userName + ", Good Afternoon.")
print(f"{userName} , Good Afternoon.")  #f string--> f" (no gap inbetween)

Date  = '17.02.2026'
letter = f'''\nDear <|{userName}|>,
        You are selected for the position of Software Engineer at our company. We are excited to have you on board and look forward to working with you.
        <|{Date}|>'''
print(letter)

template = '''\nDear <|Name|>,
        You are selected for the position of Software Engineer at our company. We are excited to have you on board and look forward to working with you.
        <|Date|>'''

print(template.replace("<|Name|>", userName).replace("<|Date|>", Date)) #replace <|Name|> with userName then replace <|Date|> with Date.This is method chaining.



sentence = "This are some  extra   spaces."
print(sentence.find("  "))

sentence1 = sentence.replace("  "," ")
print(sentence1)       #only changes the first occurrence of double spaces to single space. The second occurrence of double spaces remains unchanged.