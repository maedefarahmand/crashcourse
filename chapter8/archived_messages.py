messages=['hello', 'where are you?', 'how are you doing?']
sent_messages=[]
def show_messages(l):
   
    while l:
        a=l.pop()
        print(a)
        sent_messages.append(a)
    
show_messages(messages[:])
print("this is initial list:")
print(messages)
print("this is the other list:")
print(sent_messages)