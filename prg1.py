# * SATHIYA PRIYA S * II – BCA (24-27)
# EX 1 : FLOW CONTROLS FUNCTIONS AND MANIPULATIONS

def reverse_string(text):
     return text [: :-1]
def count_words(text):
    words=text.split()
    return len(words)
print("flow controls ,functions and manipulations")
print("~~~ ~~~~~~   ~~~~~~~ ~~  ~~~~~~~~~~")
input_text=input("enter a sentence :")

if input_text.startswith("hello"):
    print("greetings     : hello!")
elif input_text.startswith("good bye"):
    print("parting        : good bye!")
else :
        print("custom message :",input_text)
reverse_string= reverse_string(input_text)
print("reverse string    : ",reverse_string)
word_count = count_words(input_text)
print("word count      : ",word_count)

