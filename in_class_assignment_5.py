#Problem 1. Sort With Quicksort.
# Please build a function called "quicksort" that uses recursion to define the quicksort algorithm for a list of any length. 
# Build a main script that reads in the list provided, "numbers.txt", and runs it through your quicksort algorithm. 
# The main script should return the finished sorted list as "sorted.txt"
# All 3 files "In_class_assignment_5.py", "numbers.txt", and "sorted.txt" should all be added to your github repository and submitted as a github link.


'''Info on Quicksort Algorithm: 
The Quicksort algorithm is an efficient sorting algorithm developed by British computer scientist Tony Hoare in 1959.

Quicksort is a divide-and-conquer algorithm. Suppose you have a list of objects to sort. You start by choosing an item in the list, called the *pivot item*. 
This can be any item in the list. You then partition the list into two sublists based on the pivot item and recursively sort the sublists.

The steps of the algorithm are as follows:

1. Choose the pivot item.
2. Partition the list into two sublists:
        Those items that are less than the pivot item
        Those items that are greater than the pivot item
3. Quicksort the sublists recursively.
4. Each partitioning produces smaller sublists, so the algorithm is reductive. 

The base cases occur when the sublists are either empty or have one element, as these are inherently sorted. 
 '''


def quicksort(numbers_in_a_list):
        
def partition(arr, low, high):
    i = (low - 1)      
    pivot = arr[high]     
 
    for j in range(low, high):
 
        if arr[j] <= pivot:
         
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
 
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)
 
def quickSort(arr, low, high):
    if low < high:
 
        pi = partition(arr, low, high)
 
        quickSort(arr, low, pi-1)
        quickSort(arr, pi + 1, high)
        
    return 
27 29 33 44 48 51 65 75 94 101 107 111 113 126 135 139 146 153 155 173 193 214 220 224 236 242 255 267 277 282 
307 315 321 325 332 356 362 382 425 441 443 448 449 454 460 465 476 479 484 489 505 507 508 520 522 532 536 543
549 566 573 580 589 604 606 640 655 667 688 702 709 711 723 724 725 729 731 754 782 814 816 820 828 834 835 840 
875 882 901 909 931 944 950 956 964 968 972 982 996 999 


def main():

 arr = [449, 48, 242, 44, 65, 520, 332, 173, 931, 667, 146, 640, 448, 522, 820, 
964, 688, 840, 113, 325, 950, 754, 999, 723, 909, 956, 255, 972, 111, 543, 
282, 443, 362, 968, 725, 549, 356, 828, 566, 193, 107, 982, 580, 606, 882, 
834, 236, 655, 604, 731, 321, 465, 814, 441, 460, 277, 29, 476, 126, 382, 
101, 27, 135, 944, 307, 220, 51, 153, 536, 711, 901, 507, 139, 94, 155, 
214, 724, 315, 33, 267, 782, 816, 75, 489, 835, 224, 532, 996, 573, 479, 
729, 484, 505, 508, 875, 709, 589, 425, 454, 702]
    n = len(arr)
     
    quickSort(arr, 0, n - 1)
     
    for i in range(n):
        print(arr[i], end = " ")

    return #WHAT DOES IT RETURN?


if __name__ == "__main__":
    main()
