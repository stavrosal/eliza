import re, regexp

print("*  Hello I'm Eliza! (to quit type 'exit')")

while True:
   
    user = input('>  ').lower() #case-insensitive RegEx
    if user == 'exit':
        print("*  Goodbye!")
        break

    
    for regex in regexp.responses:
        matched = re.match(regex, user)
        if matched:
            print('* ', regexp.responses[regex].format(matched.group(1)))
            break

    if not matched: #reply in a generic way
            print('* Interesting...Tell me more')
            
