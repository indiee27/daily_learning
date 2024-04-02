# DICTIONARY OF TERMS
# snake case is variables written with an underscore ie snake_case

# function example without passing a parameter
def giveMeTen():
    return 10

print(giveMeTen())


# function example
def age_label(age):
    label = "User age: " + str(age) 
    return label 

# - def is the keyword to create a function
# - age_label is the function name
# - age is the parameter
# - label is a variable
# - return is the keyword for outputting a value
#   - alternative to return you can use 'print' to display a variable in the console
#   - or use both
# - str is to change the integer to a string to be able to concatenate the label variable

# function has to be called
# in this case, because there isn't a print statement in the function it has to be called as:
print(age_label(22))

# good practise for function naming is to use a verb for a return value function and start with 'is' for a boolean return

def apply_discount(price):
    discount = 20
    return price - discount
# here discount is a local variable (has local scope) meaning it cant be accessed outside of the function code block

# setting a counter loop inside a function
def onboard_passengers(bookings):
    counter = 1
    while counter <= bookings:
        print(f"Passenger {counter} on board")
        counter += 1
# alternatively
    for i in range(bookings):
        print(f"Passenger {i} on board")

# alternatively if you're looping through a list:
def halves_prices(cart):
    for price in cart:
        print(f"New price: {price/2}")

## LISTS
specials = ['pizza', 'pasta', 'risotto']
specials.sort() 
specials.insert(0, 'spaghetti')
specials.append('linguine')
specials.pop() 
print(specials)


