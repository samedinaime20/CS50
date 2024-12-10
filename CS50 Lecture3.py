# print("hello, world")
#synatxerror

# --------------------------------------


# try:
#     x=int(input("Enter a number: "))
#     print(f"x is {x}")
# except ValueError:
#     print("x is not integer")
# #ValueError

# --------------------------------------


# try:
#     x=int(input("Enter a number: "))
#
# except ValueError:
#     print("x is not integer")
# else:
#     print(f"x is {x}")
#NameError

# --------------------------------------

# def main():
#     x=get_int()
#     print(f"x is {x}")
#
# def get_int():
#     while True:
#         try:
#             return int(input("Enter a number: "))
#
#         except ValueError:
#             pass
#
# main()


# --------------------------------------

# def main():
#     x=get_int("What's x? ")
#     print(f"x is {x}")
#
# def get_int(prompt):
#     while True:
#         try:
#             return int(input(prompt))
#
#         except ValueError:
#             pass
#
# main()