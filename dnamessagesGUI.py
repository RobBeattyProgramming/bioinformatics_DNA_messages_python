# create gui
# store previous info in a csv file


import csv
def recallInfo(option):
    with open('savedData.csv', mode ='r')as file:
        csvFile = csv.reader(file)
        #for lines in csvFile:
           #print(lines)
        
        #call at open of program
        if option == "previous":
            pass
        elif option == "savedData":
            pass