curso = "pYthon"

print(curso.upper())
print(curso.lower())
print(curso.title())

curso1 = "     Python "

print(curso1.strip() + ".")
print(curso1.lstrip() + ".")
print(curso1.rstrip() + ".")


print(curso.center(10, "#"))
print("." .join(curso))