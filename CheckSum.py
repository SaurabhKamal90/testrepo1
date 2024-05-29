#given an array of length n
#given a sum
#check if the pair of elements exist in array

def CheckPair(arr, arr_size, sum):
     for i in range(0, arr_size -1):
         for j in range(i+1, arr_size):
             if (arr[i] + arr[j]==sum):
                 return 1
     return 0


if __name__ == "__main__":
    arr = [0, -1, 2, -3, 1]
    sum = -2
    arr_size = len(arr)

    if (CheckPair(arr, arr_size, sum)):
        print("Yes")

    else:
        print("No")