#!usr/bin/python

#############################
#          file: operations_module.py
#          Name: Victor
#          Date: 6/6/2021
#############################
from hashlib import new
import operations
from student import Student
from teachers import Teachers

operations.add_numbers(8,5)
operations.sub_numbers(89,14)
operations.multi_numbers(958,87)
operations.div_numbers(55,5)
print(operations.add_numbers(8,5))
print(operations.sub_numbers(89,14))
print(operations.multi_numbers(958,87))
print(operations.div_numbers(55,5))

new_student = Student("Marley ", "Freelancing", 2000)


Student.greet_student()

new_teacher = Teachers("Mr Mwai","18545", "Life skills", "70000")

Teachers.get_tsc_no()
