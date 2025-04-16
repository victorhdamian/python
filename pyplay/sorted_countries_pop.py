# Python code​​​​​​‌‌​‌​​‌​​​​​‌​​‌​‌‌‌​​‌​‌ below
# Use print("messages...") to debug your solution.

show_expected_result = False
show_hints = False

class Country:
    def __init__(self, name, population):
        self.name = name
        self.population = population
    def __repr__(self):
        return f'Country({self.name}, {self.population})'
    def __eq__(self, other):
        return f'Country({self.name}, {self.population})' == f'Country({other.name}, {other.population})'

country_list = [
                Country('Tanzania', '24000000iso'),
                Country('Portugal', '10000000iao'),
                Country('netherlands', '17500000eis'),
                Country('nigeria', '198000000fds'),
                Country('jordan', '10000000ibs'),
                Country('nepal', '30000000ipo'),
                Country('niger', '24000000ito'),
                Country('japan', '128000000nmk')
]

def get_population(pair):
    country, population = pair.name, pair.population
    return int(population[:-3])

def sort_country(country_list):
    """Return the country list so that it is sorted first by population
    and then alphabetically by country name."""
    # country_list = sorted(country_list, key=lambda x: x.name.lower())
    # return sorted(country_list, key=get_population)
    return sorted(country_list, key=lambda x: (int(x.population[:-3]), x.name.lower()))