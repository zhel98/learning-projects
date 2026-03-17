def get_square (length: int, width: int) -> int:
    """Принимает длину и ширину, возвращает площадь"""
    return length  * width

square_2 = get_square (7,5)
square_coworking = get_square(15,9)

print(square_2)
print(square_coworking)

print(get_square.__doc__)
print(help(get_square))