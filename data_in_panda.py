'''
managing data with Pandas
lecz-urban-rural-population-land-area-estimates_codebook.csv
'lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_codebook.csv'
'''

def csv_reader():
    '''test csv reader'''
    
    import csv
    
    with open('lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_codebook.csv', 'rU') as input_file:
        input_reader = csv.reader(input_file)
        for line in input_reader:
            print line 
            
# csv_reader()

def panda():
    '''test pandas'''
    
    import pandas as pd
    
    input_dataframe = pd.read_csv('lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_codebook.csv')
    print input_dataframe["Variable"]
    # print input_dataframe[0:10]
    

panda()