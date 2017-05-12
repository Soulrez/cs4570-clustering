import string
# Opens the ARFF files
lines = open('data/eb.arff').readlines()
# Enumerate the type variable
# Map of enumerations
type_map = {  'Bank':'0' , 'AutomobileIndustry':'1' , 'BpoIndustry':'2' , 'CementIndustry':'3' , 'Farmers1':'4' , 'Farmers2':'5' , 'HealthCareResources':'6' , 'TextileIndustry':'7' , 'PoultryIndustry':'8' , 'Residential(individual)':'9' , 'Residential(Apartments)':'10' , 'FoodIndustry':'11' , 'ChemicalIndustry':'12' , 'Handlooms':'13' , 'FertilizerIndustry':'14' ,'Hostel':'15' ,'Hospital':'16' , 'Supermarket':'17', 'Theatre':'18' , 'University':'19' }
newlines = []
for line in lines:
    for item in type_map:
        line = string.replace(line,item,type_map[item])
    newlines.append(line)
# Remove the ARFF-specific lines on the top
open('data/eb_stripped','w').writelines(newlines[12:-3])
