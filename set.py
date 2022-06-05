s1=set([1,2,3,4,5,6])
s2=set([4,8,9,5,4,6])

'''
now union of sets
It will add all the elements and will remove the dupicatess
'''
union_set=s1.union(s2)

#------------------------------------
'''
Intersection of sets: 
Means the common elements present in sets.
'''
intr_set=s1.intersection(s2)

#-------------------------------------
'''
Disjoint of sets:

Means there are no common elemnts are present between two sets
'''
print(s1.isdisjoint(s2))

#-------------------------------------

'''
symmetric_difference:
    return all the elements by excluding the common elemnts
'''
#print(s1.symmetric_difference(s2))
#--------------------------------------
'''
difference:
    it return the elements present in s1 but not in s2

diffrence_update:
    I will 

'''
print(s1.differenc(s2))



'''
Apart from these, we can try this functions


add():	Adds an element to the set
clear():	Removes all the elements from the set
copy():	Returns a copy of the set
difference():	Returns a set containing the difference between two or more sets
difference_update():	Removes the items in this set that are also included in another, specified set
discard():	Remove the specified item
intersection():	Returns a set, that is the intersection of two other sets
intersection_update():	Removes the items in this set that are not present in other, specified set(s)
isdisjoint():	Returns whether two sets have a intersection or not
issubset():	Returns whether another set contains this set or not
issuperset():	Returns whether this set contains another set or not
pop():	Removes an element from the set
remove():	Removes the specified element
symmetric_difference():	Returns a set with the symmetric differences of two sets
symmetric_difference_update():	inserts the symmetric differences from this set and another
union():	Return a set containing the union of sets
update():	Update the set with the union of this set and others

'''
