#set of variables to be used in the function
calculation_to_units = 20 * 60 * 60
name_of_unit = "seconds"

#function for calculating units
##declating inside of the function with () with parameter name inside
def days_to_units(num_of_days):
#putting parameter variable name instead of number value
    print(f'{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}')


#set the parameter value into the () for any calculation needed
days_to_units(20)
days_to_units(35)
days_to_units(50)
days_to_units(60)
days_to_units(100)

