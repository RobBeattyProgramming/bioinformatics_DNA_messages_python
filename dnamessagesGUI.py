# create gui
# store previous info in a csv file
import csv

def recallInfo(option):
    with open('savedData.csv', mode ='r')as file:
        csvFile = csv.reader(file)
        
        #call at open of program
        if option == "previous":
            for lines in csvFile:
                if "previous" == lines[0]:        
                    return lines[1]
                
        elif option == "savedData":
            pass

print(recallInfo("previous"))