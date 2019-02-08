from mybox import MyBox as mybox
from myclass import Person as person
from child import Student as student
#from myboxiterator import MyIterator as myboxiterator

print("Objects:")
john = person('John', 'Malcolm')
print(john)

josh_student = student('Josh', 'Pare', 123)
print(josh_student)

print("|Task 3|")

myBox = mybox()

myBox.add(john)
myBox.add(josh_student)
myBox.add(john)

print('Add 3 items: ' + str(myBox))
print('Length = ' + str(len(myBox)))
myBox.remove(josh_student)
print('Remove Josh: ' + str(myBox))
print('Length = ' + str(len(myBox)))
print('Contains Josh? ' + str(myBox.contains(josh_student)))

print('Iterator:')
myIterator = myBox.iterator()
print(myIterator)
