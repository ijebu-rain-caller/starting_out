# A function can be seen as a block of code that performs a particular activity or set of activities
# def is used as the function definition 
# docstring helps for the documentation of the function, its in triple parenthtesis
def greet_user(username):
    """Display a simple greeting and say hello to the user."""
    print("Hello, " + username.title() + "!")


greet_user("mubarak")



#TRY IT YOURSELF 
def display_message():
    """Displays an informatory sentence."""
    print("This chapter has given an introduction to functions.")

display_message()


def favorite_book(fave):
    """An insight into the users favorite book."""
    print("One of my favorite books is " + fave.title() + "!" )

favorite_book("wuthering heights")

#An argument is a piece of info that is passed through a function call to a function.
#A parameter is needed by the function to do its job
