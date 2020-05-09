from inner_pro import *
from Proj_File import *

print(responses[0])
print('I am yr maths assistant.')
# print('if you want to see my maths operation then enter->111')


while True:
    print()  # for change the line
    text = input("Enter some text:\n")
    lt = FindNumFromText(text)
    for word in text.split(' '):
        if word.upper() in operation.keys():
            try:
                r = operation[word.upper()](lt)
                print('your answer=', r)
                
                ans = int(input('if you want to save this data,enter--> 1,else-->0:\n'))
                if ans == 1:
                    myfile(text)
                    myfile(f"your answer={r}")  # it must be a string
                    print('data has been saved.')
                else:
                    pass
            
            except:
                print('there is something wrong.\n')
            finally:
                break
        
        elif word.upper() in command.keys():
            command[word.upper()]()
            break
    else:
        sorry()
        break



