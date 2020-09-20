def bubble(array):
    size = (len(array))
    for step in range(size):
        for i in range(0,size-step-1):
            if array[i+1]<array[i]:
                array[i],array[i+1] =array[i+1],array[i]  
        print(array)
bubble([2,6,7,8,3,1])
