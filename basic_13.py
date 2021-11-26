# 1. Print 1-255
# Print1To255()
# Print all the integers from 1 to 255. 

def print_int(low_num, high_num):
    while low_num <= high_num:
        print(low_num)
        low_num += 1
    

print_int(1, 255)



# 2. Print Odds 1-255
# PrintOdds1To255()
# Print all odd integers from 1 to 255. 


def print_odd_int(low_num, high_num):
    while low_num <= high_num:
        if low_num % 2 != 0:
            print(low_num)
            low_num += 1
        else:
            low_num += 1

print_odd_int(1, 255)

# 3. Print Ints and Sum 0-255
# PrintIntsAndSum0To255()
# Print integers from 0 to 255, and with each integer print the sum so far. 


def print_int_sum(low_num, high_num):
    sum = 0
    while low_num <= high_num:
        sum += low_num
        print(low_num, sum)
        low_num += 1

print_int_sum(1, 255)

# 4. Iterate and Print Array
# Iterate through a given array, printing each value. 
# PrintArrayVals(arr)

def print_arr1(arr):
    for i in range(0, len(arr), 1) :
        print(arr[i])
        

print_arr1([1, 2, 3, 4])




def print_arr(arr):
    i = 0
    while i < len(arr):
        print(arr[i])
        i += 1

arr = [1, 2, 3, 4]
print_arr(arr)

# 5. Find and Print Max
# PrintMaxOfArray(arr)
# Given an array, find and print its largest element. 

def print_max_arr1(list):
    max = list[0]
    for i in range(0, len(list), 1):
        if list[i] > max:
            max = list[i]
    print(max)    

print_max_arr1([1,2,3,23,4,5,6])
        








def print_max_arr(arr):
    i = 1
    max = arr[0]
    while i < len(arr):
        if(arr[i] > max):
            max = arr[i]
            i += 1
        else:
            i += 1
    print(max)
arr = [1, 2, 5, 3, 4]
print_max_arr(arr)

# 6. Get and Print Average
# PrintAverageOfArray(arr)
# Analyze an array’s values and print the average. 

def print_avg_arr(arr):
    i = 1
    sum = arr[0]
    while i < len(arr):
        sum += arr[i]
        i += 1
    avg = sum/len(arr)
    print(avg)

arr = [1, 2, 3, 4, 5]
print_avg_arr(arr)

# 7. Array with Odds
# ReturnOddsArray1To255()
# Create an array with all the odd integers between 1 and 255 (inclusive).  

def return_odd_arr(low_num, high_num):
    arr_odd = []
    while low_num <= high_num:
        if(low_num % 2 != 0):
            arr_odd.append(low_num)
            low_num += 1
        else:
            low_num += 1
    return arr_odd

print(return_odd_arr(1, 255))


# 8. Square the Values
# SquareArrayVals(arr)
# Square each value in a given array, returning that same array with changed values. 


def square_arr_vals(arr):
    i = 0
    while i < len(arr):
        arr[i] *= arr[i]
        i += 1
    return arr

arr = [ 2, 4, 6, 8]
print(square_arr_vals(arr))

# 9. Greater than Y
# ReturnArrayCountGreaterThanY(arr, y)
# Given an array and a value Y, count and print the number of array values greater than Y. 

def greater_than_y(arr, y):
    i = 0
    count = 0
    while i < len(arr):
        if(arr[i] > y):
            count += 1
            i += 1
        else:
            i += 1
    return count

arr = [ 2, 4, 6, 8]
print(greater_than_y(arr, 2))

# 10. Zero Out Negative Numbers
# ZeroOutArrayNegativeVals(arr)
# Return the given array, after setting any negative values to zero. 








