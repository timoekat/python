#for x in range(1,21):
  #  print("x = ", x, "x2 = ", x*x)


students = ["Александр", "Михаил", "Сергей", "Ольга", "Кирилл", "Олеся", "Виктор"]

for i in range (0,len(students)):
    print(students[i])


word = "Тест"

for s in word:
    print(s)

for student in students:
    print(student)



num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for n in num:
    if (n % 2 == 1):
        print(n)