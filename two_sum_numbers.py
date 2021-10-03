#O(n^2) time | O(1) Space
def two_sum_numbers(array, target_sum):
    print("Longitud del array es " + str(len(array)))
    print("El numero a buscar es " + str(target_sum))
    movements = 0;
    for i in range(len(array)-1):
        first_num = array[i]
        for j in range(i+1, len(array)):
            second_num = array[j]
            movements+=1
            if first_num + second_num == target_sum:
                print("La cantidad de movimientos fue : " + str(movements))
                return [first_num, second_num]
    print("La cantidad de movimientos fue : " + str(movements))
    return []

#O(n) time | O(n) Space
def two_sum_numbers_hash(array, target_sum):
    print("Longitud del array es " + str(len(array)))
    print("El numero a buscar es " + str(target_sum))
    movements = 0;
    nums = {}
    for value in array:
        potential_match = target_sum - value 
        movements+=1
        if potential_match in nums:
            print("La cantidad de movimientos fue : " + str(movements))
            return [potential_match, value]
        else:
            nums[value] = True
    print("La cantidad de movimientos fue : " + str(movements))
    return []

#O(nLog(n)) time | O(1) Space
def two_sum_numbers_pointers(array, target_sum):
    print("Longitud del array es " + str(len(array)))
    print("El numero a buscar es " + str(target_sum))
    array.sort()
    movements = 0;
    left = 0
    right = len(array) - 1
    while left < right:
        current_sum = array[left] + array[right] 
        movements+=1
        if current_sum == target_sum:
            print("La cantidad de movimientos fue : " + str(movements))
            return [array[left],array[right]]
        elif current_sum < target_sum:
            left+=1
        elif current_sum > target_sum:
            right-=1
    print("La cantidad de movimientos fue : " + str(movements))
    return []

target = 13
array = [-1, 5 , -8 ,0, 14, 4 , 9];
print("----------------------- Funcion two_sum_numbers ----------------------------")
print(array)
print(two_sum_numbers(array, target))

print("----------------------- Funcion two_sum_numbers_hash -----------------------" )
print(array)
print(two_sum_numbers_hash(array, target))


print("----------------------- Funcion two_sum_numbers_pointers -----------------------" )
print(array)
print(two_sum_numbers_pointers(array, target))