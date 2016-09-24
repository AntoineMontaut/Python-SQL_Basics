'''
Read and write files in python
'''

import collections

population2010_dict = collections.defaultdict(int)
population2100_dict = collections.defaultdict(int)
population_growth_2010_2100 = collections.defaultdict(int)

with open('lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_continent-90m.csv', 'rU') as inputFile:
    header = next(inputFile).rstrip().split(',')
    print header
    for line in inputFile:
        line = line.rstrip().split(',')
        if line[1] == 'Total National Population':
            population2010_dict[line[0]] += int(line[5])
            population2100_dict[line[0]] += int(line[6])

#for continent in population2010_dict:
 #   print('Population in {0} is: {1}'.format(continent, population2010_dict[continent]))
 
for key in population2010_dict.keys():
    population_growth_2010_2100[key] = 100*(population2100_dict[key]-\
    population2010_dict[key])/population2010_dict[key]
 
with open("population_per_continent.csv", 'w') as outputFile:
    outputFile.write("continent,population_2010,population_2100,growth_2010_2100\n")
    for k,v in population2010_dict.iteritems():
        outputFile.write(k + ',' + str(v) + ',' + \
        str(population2100_dict[k]) + ',' +\
        str(population_growth_2010_2100[k])+'%' + '\n')