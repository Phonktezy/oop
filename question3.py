#1
# class Point3D:
#
#     def init(self,x,y,z):
#         self.x = x
#         self.y = y
#         self.z = z
#     def info(self):
#         print(f'x = {self.x},y = {self.y},z = {self.z}')
#
#     def distance(self):
#         dxy = self.y - self.x
#         dzy = self.z - self.y
#         print(f'Расстояние между xy: {dxy},Расстояние между zy: {dzy}')
#
#     def double(self):
#         return 2*self.x,2*self.y,2*self.z
#
# a = Point3D(50,22,-10)
# b = Point3D(8,435,7)
# c = Point3D(-123,-4444,123)
# a.info()
# b.info()
# c.info()
# a.distance()
# a.z = 12343241231234324324
# a.info()
# print(a.double())
#
# a = int(input())
# if a % 2 == 0:
#     print('Четное')
# else:
#     print('Нечентное')
#
# a = [1, 2, 3, 4, 5]
# b = sum(a)
# print(b)

#2
# class CPerson:
#     def init(self, name,surname,otch,data,pol):
#         self.name = name
#         self.surname = surname
#         self.otch = otch
#         self.data = data
#         self.pol = pol
#
#     def rd(self):
#         print(f"Имя: {self.name} \n"
#               f"Фамилия: {self.surname} \n"
#               f"Отчество: {self.otch} \n"
#               f"Дата рождения: {self.data} \n"
#               f"Пол: {self.pol} \n")
#
#     def ch(self,name,surname,otch,data,pol):
#         print(f"Имя: {self.name} \n"
#               f"Фамилия: {self.surname} \n"
#               f"Отчество: {self.otch} \n"
#               f"Дата рождения: {self.data} \n"
#               f"Пол: {self.pol} \n")
#
#
#     def __del__(self):
#         print('Всё стёрто')
# tom = CPerson('alex', 'fef', 'ser',17012007,'m')
# tom.rd()
# tom.ch()

#3
# class Reader:
#     def __init__(self, full_name, ticket_number, faculty, birth_date, phone):
#         self.full_name = full_name
#         self.ticket_number = ticket_number
#         self.faculty = faculty
#         self.birth_date = birth_date
#         self.phone = phone
#
#     def takeBook(self, num_books):
#         print(f"{self.full_name} взял {num_books} книги")
#
#     def returnBook(self, num_books):
#         print(f"{self.full_name} вернул {num_books} книги")
#
# # Пример использования:
# reader = Reader("Петров В. В.", 12345, "Исторический", "01.01.2000", "123-456-7890")
# reader.takeBook(3)
# reader.returnBook(3)