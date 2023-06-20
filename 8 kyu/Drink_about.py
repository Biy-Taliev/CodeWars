'''
Kids drink toddy.
Teens drink coke.
Young adults drink beer.
Adults drink whisky.
Make a function that receive age, and return what they drink.

Rules:

Children under 14 old.
Teens under 18 old.
Young under 21 old.
Adults have 21 or more.
Examples: (Input --> Output)

13 --> "drink toddy"
17 --> "drink coke"
18 --> "drink beer"
20 --> "drink beer"
30 --> "drink whisky"

'''

def people_with_age_drink(age):
    return ["drink toddy", "drink coke", "drink beer", "drink whisky"][(age >= 21) + (age > 17) + (age > 13)]

a = 'abc'
for i in  a:
    b = i * (a.index(i)+1)
    b[0].upper()
    print