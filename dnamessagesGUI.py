import csv
import tkinter as tk

m = tk.Tk()

m.mainloop()

vibrioCholeraeSegment = "atcaatgatcaacgtaagcttctaagcatgatcaaggtgctcacacagtttatccacaacctgagtggatgacatcaagataggtcgttgtatctccttcctctcgtactctcatgaccacggaaagatgatcaagagaggatgatttcttggccatatcgcaatgaatacttgtgacttgtgcttccaattgacatcttcagcgccatattgcgctggccaaggtgacggagcgggattacgaaagcatgatcatggctgttgttctgtttatcttgttttgactgagacttgttaggatagacggtttttcatcactgactagccaaagccttactctgcctgacatcgaccgtaaattgataatgaatttacatgcttccgcgacgatttacctcttgatcatcgatccgattgaagatcttcaattgttaattctcttgcctcgactcatagccatgatgagctcttgatcatgtttccttaaccctctattttttacggaagaatgatcaagctgctgctcttgatcatcgtttc"

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
        elif option == "saveOne":
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

def saveInfo(option, data):

        with open('savedData.csv', mode ='r') as file:
            csvFile = csv.reader(file)
            rows = list(csvFile)

            if option == 1:
                rows[1] = ['saveOne', data]
            if option == 2:
                rows[2] = ['saveTwo', data]
            if option == 3:
                rows[3] = ['saveThree', data]

        file = open('savedData.csv', 'w+')
 
        with file:    
            write = csv.writer(file)
            write.writerows(rows)
                    

saveInfo(1, vibrioCholeraeSegment)
        
        



    
    


        

    
         


