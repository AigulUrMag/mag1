from peewee import *

conn =SqliteDatabase('db1.sqlite')

class Students (Model):
	id =IntegerField(column_name='id')
	name =CharField(column_name='name')
	surname =CharField(column_name='surname')
	age =IntegerField(column_name='age')
	city =CharField(column_name='city')

	class Meta:
		database = conn

class Courses (Model):
	id =IntegerField(column_name='id')
	name =CharField(column_name='name')
	time_start =CharField(column_name='time_start')
	time_end =CharField(column_name='time_end')

	class Meta:
		database = conn


class Student_courses (Model):
	student_id =IntegerField(column_name='student_id')
	course_id =IntegerField(column_name='course_id')

	class Meta:
		database = conn

Students.create_table()
Courses.create_table()
Student_courses.create_table()

s1=Students(id=1, name='Max', surname='Brooks',age= 24,city= 'Spb')
s1.save
s1=Students(id=2, name='John', surname='Stones',age= 15,city= 'Spb')
s1.save
s1=Students(id=3, name='Andy', surname='Wings',age= 45,city= 'Manhester')
s1.save
s1=Students(id=4, name='Kate', surname='Brooks',age= 34,city= 'Spb')
s1.save


c1=Courses(id=1,name='python',time_start='21.07.21',date_end='21.08.21')
c1.save
c1=Courses(id=1,name='python',time_start='21.07.21',date_end='21.08.21')
c1.save

sc1=Student_courses(student_id=1,course_id=1)
sc1.save
sc1=Student_courses(student_id=2,course_id=1)
sc1.save
sc1=Student_courses(student_id=3,course_id=1)
sc1.save
sc1=Student_courses(student_id=4,course_id=2)
sc1.save

#query=Students.select().where(Students.age>30)
for s1 in Students.select().where(Students.age>30):
	print(s1.name)

query1 = Students.select().join(Student_courses).join(Courses).where(Courses.id == 1)
for s1 in query1:
    print(s1.name)


query2 = Students.select().join(Student_courses).join(Courses).where((Students.city == 'Spb') and (Courses.id == 1))
for s1 in query2:
    print(s1.name)


conn.commit()
conn.close