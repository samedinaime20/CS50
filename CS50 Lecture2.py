#print("meow")
#print("meow")
#print("meow")


# i=0
# while i<20:
#     print("meow")
#     i=i+1

# for i in range(20):
#     print("meow")

# print("meow\n"*3, end="")

# while True:
#     n=int(input("Enter a number: "))
#     if n>0:
#         break
# for _ in range(n):
#     print("meow")

# def main():
#     number=get_number()
#     meow(number)
#
# def meow(n):
#     for _ in range(n):
#         print("meow")
#
# def get_number():
#     while True:
#         n=int(input("Enter a number: "))
#         if n>0:
#             break
#     return n

# students=["Hermione","Harry","Ron"]
# for i in range(len(students)):
#     print(i+1,students[i])

# students={"Hermione":"Gryffindor","Harry":"Gryffindor","Ronald":"Gryffindor","Draco":"Slytherin",}
# for student in students:
#     print(student, students[student], sep="-> ")

# students=[
#     {"name":"Hermione","House":"Gryffindor","patronus":"Otter"},
#     {"name":"Harry","House":"Gryffindor","patronus":"Stag"},
#     {"name":"Ronald","House":"Gryffindor","patronus":"Jack Russell terrier"},
#     {"name":"Draco","House":"Slytherine","patronus": None}
# ]
# for student in students:
#     print(student["name"],student["House"],student["patronus"],sep="| ")

# for _ in range(3):
#     print("#")

# def main():
#     print_column(3)
#
# def print_column(height):
#     for _ in range(height):
#         print("#")
# main()

# def main():
#     print_row(4)
#
# def print_row(width):
#     print("?"*width)
# main()

def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print_row(size)

def print_row(width):
    print('#' * width)
main()