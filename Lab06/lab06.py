from Apartment import Apartment


def mergesort(apartmentList):
    if len(apartmentList) > 1:
        mid = len(apartmentList) // 2
        left = apartmentList[:mid]
        right = apartmentList[mid:]
        mergesort(left)
        mergesort(right)
        m=0
        n=0
        k=0
        while m < len(left) and n < len(right):
            if left[m] > right[n]:
                apartmentList[k] = right[n]
                n += 1

            else:
                apartmentList[k] = left[m]
                m += 1
            
            k += 1

        while m < len(left):
            apartmentList[k] = left[m]
            k += 1
            m += 1

        while n < len(right):
            apartmentList[k] = right[n]
            k += 1
            n += 1


def ensureSortedAscending(apartmentList):
    for i in range(len(apartmentList)-1):
        if not apartmentList[i] < apartmentList[i+1]:
            return False
        
    return True


def getWorstApartment(apartmentList):
    mergesort(apartmentList)
    return apartmentList[len(apartmentList) - 1].getApartmentDetails()

def getBestApartment(apartmentList):
    mergesort(apartmentList)
    return apartmentList[0].getApartmentDetails()



def getAffordableApartments(apartmentList, budget):
    ans = []
    ret = ""
    mergesort(apartmentList)
    for apartment in apartmentList:
        if apartment.getRent() <= budget:
            ans.append(apartment.getApartmentDetails())
            ret = "\n".join(ans)
    return ret


