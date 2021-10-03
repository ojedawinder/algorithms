#O(n) | Space O(1)
def validateSubsequenceWhile(array, subsequence):
    arrIdx = 0
    seqIdx = 0
    while arrIdx < len(array) and seqIdx < len(subsequence):
        if array[arrIdx]==subsequence[seqIdx]:
            seqIdx+=1
        arrIdx+=1
    return seqIdx == len(subsequence)


#O(n) | Space O(1)
def validateSubsequenceFor(array, subsequence):
    seqIdx = 0
    for value in array:
        if seqIdx == len(subsequence):
            break 
        if value == subsequence[seqIdx]:
            seqIdx+=1
    return seqIdx == len(subsequence)

subsequence = [4, 13]
array = [-1, 5 , 4 ,0, 14, 12 , 9];
print("----------------------- Funcion validateSubsequenceWhile ----------------------------")
print(array)
print(subsequence)
print(validateSubsequenceWhile(array, subsequence))   

print("----------------------- Funcion validateSubsequenceFor ----------------------------")
print(array)
print(subsequence)
print(validateSubsequenceFor(array, subsequence))   