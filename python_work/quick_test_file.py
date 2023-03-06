def neat_name(first,last,middle=''):
    """Return a neatly formatted name"""
    if middle:
             full_name = first.title() + ' ' + middle.title() + ' ' + last.title()
    else: 
           full_name = first.title() + ' ' + last.title()

    return full_name


def country_info(city_name,country_name,population=''):
       """Returns a well formatted description of country"""
       if population:
                full_deetz = city_name.title() + ', ' + country_name.title() + ' - population: ' + str(population)
       else: 
            full_deetz = city_name.title() + ', ' + country_name.title()

       return full_deetz



























5


