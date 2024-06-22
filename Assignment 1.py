import math

m_perc = int(input("Enter the amount of males in the class: "))
f_perc = int(input("Enter the amount of females in the class: "))
nb_perc = int(input("Enter the amount of non-binary in the class: "))

totalStudents = m_perc + f_perc + nb_perc


print ("Total number of students: ",totalStudents)
print (f'The number of males, females, and n-b: \t {m_perc} \t\t {f_perc} \t\t40
        {nb_perc}')

m_perc = (m_perc/totalStudents)*100
f_perc = (f_perc/totalStudents)*100
nb_perc = (nb_perc/totalStudents)*100

print (f'The percentage of males, females and nb: {m_perc:.2f}% \t {f_perc:.2f}% \t {nb_perc:.2f}%')