years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
births = [723_165, 723_913, 729_674, 698_512, 695_233, 697_852, 696_271, 679_106, 657_076, 640_370]

'''
Return a list of tuples with each entry in this format
(year, birth, running_average)
Round the running_average to the nearest integer. 
'''
def annual_births_average(year=years, births=births):
    result = []
    sum = 0
    for index,  (year, birth) in enumerate(zip(years,births), start=1):
      sum += birth
      avg = round(sum/index)
      result.append((year,birth,avg))
    return result

print (annual_births_average(years, births))