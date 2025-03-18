import codecademylib3_seaborn
import pandas as pd
from students import students

print(students.columns)
students = pd.melt(frame=students, id_vars=['full_name','gender_age','grade'], value_vars=['fractions', 'probability'], value_name='score', var_name='exam')

print(students.head())
print(students.columns)
print(students.exam.value_counts())

########################################

duplicates = students.duplicated()
print(duplicates.head())
print(duplicates.value_counts())
students = students.drop_duplicates()
duplicates = students.duplicated()
print(duplicates.head())
print(duplicates.value_counts())


##############Split Index##########################

students["gender"] = students.gender_age.str[0:1]
students["age"] = students.gender_age.str[1:3]
print(students.head())

students = students[['full_name','exam','grade','score','gender','age']]

###################Split char ##################################

name_split = students["full_name"].str.split(' ')

students["first_name"] = name_split.str.get(0)
students["last_name"] = name_split.str.get(1)

print(students.head())

###################String Parsing ##################################

students["score"] = students["score"].replace('[\%,]','', regex=True)
students["score"] = pd.to_numeric(students["score"])


students.grade = students.grade.str.split('(\d+)', expand=True)[1]

print(students.dtypes)

students.grade = pd.to_numeric(students.grade)
avg_grade = students.grade.mean()

print(avg_grade)
