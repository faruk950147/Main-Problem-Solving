list1 = [1, 2, 3, 4, 5]

def forEach(arr,callback):
    for i in range(len(arr)):
        callback(arr[i], i, arr)

forEach(list1, lambda value,index,array: print(f"Value: {value} Index: {index} Array: {array}"))


















