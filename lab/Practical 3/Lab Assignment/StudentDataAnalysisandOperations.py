import numpy as np

a = np.loadtxt("Sample.csv", delimiter=',', skiprows=1)

print("All student Details:")
print("",a)

print("Total Students:", int(a.shape[0]))

print("All Student Roll Nos", a[:, 0])

print("Subject 1 Marks", a[:, 1])

print("Min marks in Subject 2", np.min(a[:, 2]))

print("Max marks in Subject 3", np.max(a[:, 3]))

print("All subject marks:", a[:, 1:4])

print("Total Marks", np.sum(a[:, 1:4], axis=1))

print(np.round(np.mean(a[:, 1:4], axis=1), 1))

print("Average Marks of each subject", np.round(np.mean(a[:, 1:4], axis=0), 1))

print("Average Marks of S1 and S2", np.round(np.mean(a[:, 1:3], axis=0), 1))

print("Average Marks of S1 and S3", np.round(np.mean(a[:, [1, 3]], axis=0), 1))

max_s3_index = np.argmax(a[:, 3])
print("Roll no who got maximum marks in Subject 3", a[max_s3_index, 0])

min_s2_index = np.argmin(a[:, 2])
print("Roll no who got minimum marks in Subject 2", a[min_s2_index, 0])

roll_24 = a[a[:, 2] == 24][:, [0]]
print("Roll no who got 24 marks in Subject 2", roll_24)

count_s1_less_40 = np.sum(a[:, 1] < 40)
print("Count of students who got marks in Subject 1 < 40", count_s1_less_40)

count_s2_more_90 = np.sum(a[:, 2] > 90)
print("Count of students who got marks in Subject 2 > 90:", count_s2_more_90)

count_each_sub_90 = np.sum(a[:, 1:4] >= 90, axis=0)
print("Count of students in each subject who got marks >= 90:", count_each_sub_90)

print("Roll no:", a[:, 0])

count_stud_sub_90 = np.sum(a[:, 1:4] >= 90, axis=1)
print("Count of subjects in which student got marks >= 90:", count_stud_sub_90)

print(np.sort(a[:, 1]))

students_50_90 = a[(a[:, 1] >= 50) & (a[:, 1] <= 90)]
print(students_50_90)

print(a)

indices_79 = np.where(a[:, 1] == 79)
print(indices_79)
