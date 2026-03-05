import random # to generate numbers 0-5

# Kingdoms For the start date 1066

#Countries I wish to play as, structured in a list
countries = [
"France","England", "Norway", "Denmark","Scotland"
] 

num = random.randint (0,5)
print(f'Random Number: {num}')  #f-string for not turning the int into a string. 
print(countries[num])            # In other words, not being apart of 'random number:'
 
quips = [
    "Ew, what are you, a Frenchie?",
    "God Save The Queen- Er- King.",
    "HINGADINGA DERGIN",
    "What does Denmark even do besides Lego?",
    "I'm the Scotman"
]

print(quips[num])

