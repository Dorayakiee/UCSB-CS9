from Apartment import Apartment
from lab06 import mergesort
from lab06 import ensureSortedAscending
from lab06 import getBestApartment
from lab06 import getWorstApartment
from lab06 import getAffordableApartments

def test_getApartmentDetails():
    a0 = Apartment(114514, 100, "bad")
    assert a0.getApartmentDetails() == "(Apartment) Rent: $114514, Distance From UCSB: 100m, Condition: bad"

def test_lt():
    a1=Apartment(114,200,"excellent")
    a2=Apartment(514,250,"bad")
    a3=Apartment(191,50,"average")
    a4=Apartment(191,50,"average")
    a5=Apartment(191,50,"excellent")
    assert (a1<a2) == True
    assert (a2<a3) == False
    assert (a5<a4) == True

def test_gt():
    a1=Apartment(111,200,"excellent")
    a2=Apartment(199,250,"bad")
    a3=Apartment(123,50,"average")
    a4=Apartment(123,50,"average")
    a5=Apartment(123,50,"excellent")
    assert (a1>a2) == False
    assert (a3>a4) == False
    assert (a2>a5) == True

def test_eq():
    a1=Apartment(100,200,"excellent")
    a2=Apartment(150,250,"bad")
    a3=Apartment(120,50,"average")
    a4=Apartment(120,50,"average")
    a5=Apartment(120,50,"excellent")
    assert (a1==a2) == False
    assert (a3==a4) == True

# lab06
def test_ensureSortedAscending_sample():
    a0 = Apartment(1222, 222, "average")
    a1 = Apartment(1222, 222, "excellent")
    a2 = Apartment(1111, 111, "average")
    a3 = Apartment(1111, 233, "excellent")
    a4 = Apartment(777, 333, "bad")
    a5 = Apartment(888, 250, "excellent")
    apartmentList = [a0, a1, a2, a3, a4, a5]

    assert ensureSortedAscending(apartmentList) == False
    mergesort(apartmentList)
    assert ensureSortedAscending(apartmentList) == True

def test_ensureSortedAscending():
    a0 = Apartment(55555, 700, "bad")
    a1 = Apartment(7777, 430, "excellent")
    a2 = Apartment(8888, 10, "excellent")
    a3 = Apartment(55, 1, "average")
    apartmentList1 = [a0, a1, a2, a3]

    assert ensureSortedAscending(apartmentList1) == False
    mergesort(apartmentList1)
    assert ensureSortedAscending(apartmentList1) == True

def test_getBestapartment_sample():
    a0 = Apartment(1299, 200, "average")
    a1 = Apartment(1299, 200, "excellent")
    a2 = Apartment(1111, 100, "average")
    a3 = Apartment(1111, 215, "excellent")
    a4 = Apartment(777, 315, "bad")
    a5 = Apartment(888, 250, "excellent")
    apartmentList = [a0, a1, a2, a3, a4, a5]

    assert getBestApartment(apartmentList) == "(Apartment) Rent: $777, Distance From UCSB: 315m, Condition: bad"

def test_getBestApartment():
    a0 = Apartment(55555, 700, "bad")
    a1 = Apartment(7777, 430, "excellent")
    a2 = Apartment(8888, 10, "excellent")
    a3 = Apartment(55, 1, "average")
    apartmentList1 = [a0, a1, a2, a3]

    assert getBestApartment(apartmentList1) == "(Apartment) Rent: $55, Distance From UCSB: 1m, Condition: average"

def test_getWorstApartment_sample():
    a0 = Apartment(1200, 200, "average")
    a1 = Apartment(1200, 200, "excellent")
    a2 = Apartment(1000, 100, "average")
    a3 = Apartment(1000, 215, "excellent")
    a4 = Apartment(700, 315, "bad")
    a5 = Apartment(800, 250, "excellent")
    apartmentList = [a0, a1, a2, a3, a4, a5]

    assert getWorstApartment(apartmentList) == "(Apartment) Rent: $1200, Distance From UCSB: 200m, Condition: average"

def test_getWorstApartment():
    a0 = Apartment(55555, 700, "bad")
    a1 = Apartment(7777, 430, "excellent")
    a2 = Apartment(8888, 10, "excellent")
    a3 = Apartment(50, 1, "average")
    apartmentList1 = [a0, a1, a2, a3]

    assert getWorstApartment(apartmentList1) == "(Apartment) Rent: $55555, Distance From UCSB: 700m, Condition: bad"

def test_getAffordableApartments_sample():
    a0 = Apartment(1115, 215, "bad")
    a1 = Apartment(970, 215, "average")
    a2 = Apartment(950, 215, "average")
    a3 = Apartment(950, 190, "excellent")
    a4 = Apartment(900, 190, "excellent")
    a5 = Apartment(500, 250, "bad")
    apartmentList = [a0, a1, a2, a3, a4, a5]

    assert getAffordableApartments(apartmentList, 950) == '(Apartment) Rent: $500, Distance From UCSB: 250m, Condition: bad' +'\n'+ '(Apartment) Rent: $900, Distance From UCSB: 190m, Condition: excellent'+'\n'+'(Apartment) Rent: $950, Distance From UCSB: 190m, Condition: excellent'+'\n'+'(Apartment) Rent: $950, Distance From UCSB: 215m, Condition: average'

def test_getAffordableApartments():
    a0 = Apartment(55555, 700, "bad")
    a1 = Apartment(7777, 430, "excellent")
    a2 = Apartment(8888, 10, "excellent")
    a3 = Apartment(55, 1, "average")
    apartmentList1 = [a0, a1, a2, a3]

    assert getAffordableApartments(apartmentList1, 1) == ""
    assert getAffordableApartments(apartmentList1, 8000) == '(Apartment) Rent: $55, Distance From UCSB: 1m, Condition: average' + '\n' + '(Apartment) Rent: $7777, Distance From UCSB: 430m, Condition: excellent'
