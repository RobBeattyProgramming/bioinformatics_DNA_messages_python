vibrioCholeraeSegment = "atcaatgatcaacgtaagcttctaagcatgatcaaggtgctcacacagtttatccacaacctgagtggatgacatcaagataggtcgttgtatctccttcctctcgtactctcatgaccacggaaagatgatcaagagaggatgatttcttggccatatcgcaatgaatacttgtgacttgtgcttccaattgacatcttcagcgccatattgcgctggccaaggtgacggagcgggattacgaaagcatgatcatggctgttgttctgtttatcttgttttgactgagacttgttaggatagacggtttttcatcactgactagccaaagccttactctgcctgacatcgaccgtaaattgataatgaatttacatgcttccgcgacgatttacctcttgatcatcgatccgattgaagatcttcaattgttaattctcttgcctcgactcatagccatgatgagctcttgatcatgtttccttaaccctctattttttacggaagaatgatcaagctgctgctcttgatcatcgtttc"
    
def frequentKmer(dna, kmer):

    nucleotideList = list(dna)
    start = 0
    dnaLength = len(nucleotideList)
    segmentDict = {}

    #Collects segments of DNA in length of kmer and counts how frequently  
    while start < dnaLength - kmer - 1:
        segmentStart = start
        segmentEnd = start + kmer
        segmentString = ""

        while segmentStart != segmentEnd:
            segmentString = segmentString + nucleotideList[segmentStart]
            segmentStart += 1
        
        if segmentString in segmentDict:
            segmentDict[segmentString] += 1
        else:
            segmentDict[segmentString] = 0
        start += 1

    #finds most repeated kmer
    largestRepeatingKmer = max(segmentDict, key=segmentDict.get)
    return largestRepeatingKmer

x = frequentKmer(vibrioCholeraeSegment, 9)
print(x)