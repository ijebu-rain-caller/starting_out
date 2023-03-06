#Testing a function
from quick_test_file import neat_name

print("Enter 'q' at any time to quit the program.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break 
    last = input("Please give me a last name: ")
    if last == 'q':
        break

    formatted_name = neat_name(first,last)
    print("\tNeatly formatted name: " + formatted_name + '.')

    
#Unit Tests and Test Cases

#A unit test verifies that one specific aspect of a function's behavior is correct

#A test case is a collection of unit tests that together proves that the function behaves correctly.


