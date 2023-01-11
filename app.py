from art import *

random = randart()
hello = tprint("hello")

prompt = input('What would you like to say?')
message = tprint(prompt)

subject = input("what would you like to see as ascii art?")
artSubject = art(subject)

print(artSubject)

