vibrioCholeraeSegment = "atcaatgatcaacgtaagcttctaagcatgatcaaggtgctcacacagtttatccacaacctgagtggatgacatcaagataggtcgttgtatctccttcctctcgtactctcatgaccacggaaagatgatcaagagaggatgatttcttggccatatcgcaatgaatacttgtgacttgtgcttccaattgacatcttcagcgccatattgcgctggccaaggtgacggagcgggattacgaaagcatgatcatggctgttgttctgtttatcttgttttgactgagacttgttaggatagacggtttttcatcactgactagccaaagccttactctgcctgacatcgaccgtaaattgataatgaatttacatgcttccgcgacgatttacctcttgatcatcgatccgattgaagatcttcaattgttaattctcttgcctcgactcatagccatgatgagctcttgatcatgtttccttaaccctctattttttacggaagaatgatcaagctgctgctcttgatcatcgtttc"

nucleotideList = list(vibrioCholeraeSegment)
start = 0
dnaLength = len(nucleotideList)
segmentDict = {}

while start < dnaLength - 8:
    segmentStart = start
    segmentEnd = start + 9
    segmentString = ""

    while segmentStart != segmentEnd:
        segmentString = segmentString + nucleotideList[segmentStart]
        segmentStart += 1
        print(segmentString)
    
    
    if segmentString in segmentDict:
        #print("hey!  : " + segmentString)
        #segmentDict[segmentString] = 0
        #print(segmentDict[segmentString])
        segmentDict[segmentString] += 1
    else:
        segmentDict[segmentString] = 0
    print(segmentDict[segmentString])
    #if segmentString in segmentDict:
    #    timeToAdd = segmentDict[segmentString]
    #    timeToAdd += 1
    #    segmentDict[segmentString] = timeToAdd
    #else:
    #    segmentDict[segmentString] = 0
    start += 1

x = segmentDict.keys()
#print(x)




