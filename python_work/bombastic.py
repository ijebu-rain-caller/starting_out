"""This module contains basic functions"""
def build_person(first,last,**other_info):
    """Allows you to build a persona from user information into a dictionary"""
    person = {}
    person['first_name'] = first
    person['last_name'] = last
    for key,value in other_info.items():
        person[key] = value
    return person 

def sand_wich(*ingredients):
    """Making the perfect sand-wich"""
    print("This is a summary of the ingredients in the sandwich: ")
    for tastes in ingredients:
        print("- " + tastes.title())




