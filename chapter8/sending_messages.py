messages=['hello', 'where are you?', 'how are you doing?']
def show_messages(l):
    sent_messages=[]
    while l:
        a=l.pop()
        print(a)
        sent_messages.append(a)
    print("this is initial list:")
    print(l)
    print("this is the other list:")
    print(sent_messages)
show_messages(messages)
