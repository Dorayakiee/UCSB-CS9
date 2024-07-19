def test_binarySearchNormal():
    assert binarySearch([1,2,3,4,5,6,7,8,9,10], 5) == True
    assert binarySearch([1,2,3,4,5,6,7,8,9,10], -1) == False
    assert binarySearch([1,2,3,4,5,6,7,8,9,10], 11) == False
    assert binarySearch([1,2,3,4,5,6,7,8,9,10], 1) == True
    assert binarySearch([1,2,3,4,5,6,7,8,9,10], 10) == True

def test_binarySearchDuplicates():
    assert binarySearch([-10, -5, 0, 1, 1, 4, 4, 7, 8], 0) == True
    assert binarySearch([-10, -5, 0, 1, 1, 4, 4, 7, 8], 2) == False
    assert binarySearch([-10, -5, 0, 1, 1, 4, 4, 7, 8], 4) == True

def test_binarySearchEmpty():
    assert binarySearch([], 0) == False

# def binarySearch(intList, item):
#     first = 0
#     last = len(intList) - 1
#     found = False

#     while first <= last and not found:
#         mid = (first + last) // 2
#         if intList[mid] == item:
#             found = True
#         else:
#             if item < intList[mid]:
#                 last = mid - 1
#             else:
#                 first = mid + 1
#     return found

# Recursive
def binarySearch(intList, item):
    # Base case
    if len(intList) == 0:
        return False

    mid = len(intList) // 2
    if intList[mid] == item:
        return True
    elif item < intList[mid]:
        return binarySearch(intList[0 : mid], item)
    else:
        return binarySearch(intList[mid + 1 : ], item)