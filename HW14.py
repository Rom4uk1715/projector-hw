

'''
Practice
1) Modify the Country class to include a third instance attribute called capital as a string. Store your new class in a script and test it out by adding the following code at the bottom of the script:
japan = Country('Japan', 140_000_000, 'Tokyo')
print(f"{japan.name} population is {japan.population} and capital is {japan.capital}.") 
The output of your script should be:
Japan population is 140000000 and capital is Tokyo.
2)Add increase_population method to country class. This method should take an argument and increase population of the country on this number.
3)Create add method to add two countries together. This method should create another country object with the name of the two countries combined and population of the two countries added together.
bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)
bosnia_herzegovina = bosnia.add(herzegovina)
bosnia_herzegovina.population -> 15_000_000
bosnia_herzegovina.name -> 'Bosnia Herzegovina'
'''


# Practice task japan


class Country:
    # adding custom attributes
    def __init__(self, name: str, population: int, capital: str): # Додаємо попорядку кожний атрибут із класу
        self.name = name
        self.population = population
        self.capital = capital
    def growcountry(self, newpeople: int): # приріст населення країни 
        self.population += newpeople
    def two_on_one(self, country):  #створення обєкту який обєднює найменування та кількість наслення обох країн
        self.name += '_'
        self.name += country.name
        self.population = country.population


japan = Country('Japan', 140_000_000, 'Tokyo')
print(f"{japan.name} population is {japan.population} and capital is {japan.capital}.")
japan.growcountry(21334123)
print(f"{japan.name} population is growed to {japan.population}")


# Practice task Bosnia 

class Country1:
    # adding custom attributes
    def __init__(self, name: str, population: int):
        self.name = name
        self.population = population

    def growcountry(self, other):
        return Country1(self.name + ' ' + other.name, self.population + other.population)



bosnia = Country1('Bosnia', 10_000_000)
herzegovina = Country1('Herzegovina', 5_000_000)

bosnia_herzegovina = bosnia.growcountry(herzegovina)
print(f"{bosnia_herzegovina.name} population is {bosnia_herzegovina.population}")