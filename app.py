from art import *

coffee = art("coffee")
random = randart()
hello = tprint("hello")

# prints user prompt into ascii
prompt = input('What would you like to say?')
message = tprint(prompt)

#prints ascii art from user selected subject
subject = input("what would you like to see as ascii art?")
artSubject = art(subject)

print(artSubject)