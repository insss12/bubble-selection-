def bubble_sort(lists): #tao ham bbubblesort
    n=len(lists) #variable n = len(list)
    for i in range(n): #chay vong lap dau tien tu n -> n-1
        for j in range(n-i-1): #chay vong lap thu 2 so sanh vs vong dau( cap phan tu )
            if lists[j] > lists[j+1]: #neu j > phan tu tiep theo
                lists[j], lists[j+1] = lists[j+1], lists[j] #thay doi

    return lists

def selection_sort(lists):
    n = len(lists) #variable n = len(list)
    for i in range(n): #chay vong lap
        min_num = i #gia su i la nho nhat
        for j in range(i+1, n): #duyet nhx phan tu trc no
            if lists[j] > lists[min_num]: #neu j > nho nhat
                min_num = j #min = j
    return lists


my_list=[14,6,72,1,7,9,32]
print(bubble_sort(my_list))
print(selection_sort(my_list))