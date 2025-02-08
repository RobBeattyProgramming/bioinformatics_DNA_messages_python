# create gui
# store previous info in a csv file
import csv

def recallInfo(option):
    with open('savedData.csv', mode ='r')as file:
        csvFile = csv.reader(file)
        rows = list(csvFile)
        nothing = ""
        
        #call at open of program
        if option == "previous":
            for lines in csvFile:
                if lines[0] == "previous":        
                    return lines[1]
                
        if option == "saveOne":
            savedRow = rows[1]
            if savedRow[1] == "null":
                return nothing
            else:
                return savedRow[1]
        elif option == "saveTwo":
            savedRow = rows[2]
            if savedRow[1] == "null":
                return nothing
            else:
                return savedRow[1]
        elif option == "saveThree":
            savedRow = rows[3]
            if savedRow[1] == "null":
                return nothing
            else:
                return savedRow[1]
            
        elif option == "addData":
            pass
            

print(recallInfo("saveOne"))
