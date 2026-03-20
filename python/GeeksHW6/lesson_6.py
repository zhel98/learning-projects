# def get_square (length: int, width: int) -> int:
#     """Принимает длину и ширину, возвращает площадь"""
#     return length  * width

# square_2 = get_square (7,5)
# square_coworking = get_square(15,9)

# print(square_2)
# print(square_coworking)

# print(get_square.__doc__)
# print(help(get_square))

"функция которая принимает имя и фамилия"
"а в итоге возвращает данные в строке (формат: ФАМИЛИЯ Имя)"
"доп условие все буквы принимает"

name = input("enter ur name: ")
surname = input("enter ur surname: ")

def get_name_surname(name: str, surname: str) -> str:
    if name.isalpha() and surname.isalpha():
      return surname.upper()+ " " + name.title()  
    else:
        print("ты дурень")

print(get_name_surname(name,surname))


