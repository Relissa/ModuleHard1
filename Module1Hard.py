grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
average = sum(grades[0]) / len(grades[0]), sum(grades[1]) / len(grades[1]), sum(grades[2]) / len(grades[2]), sum(grades[3]) / len(grades[3]), sum(grades[4]) / len(grades[4])
list = (sorted(students))
estimates = list[0] + ': ' + str(average[0]), list[1] + ': ' + str(average[1]), list[2] + ': ' + str(average[2]), list[3] + ': ' + str(average[3]), list[4] + ': ' + str(average[4])
print(estimates)