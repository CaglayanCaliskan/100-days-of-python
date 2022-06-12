# import turtle
# # import another_module
# # print(another_module.another_variable)

# timmy = turtle.Turtle()
# print(timmy)
# timmy.shape('turtle')
# timmy.color('coral')
# timmy.forward(105)

# my_screen = turtle.Screen()
# print(my_screen.canvheight)

# my_screen.etableitonclick()
# importing random module


from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ["Pokemon Name", "Type"]
table.add_row(["Pikachu", "Electric"])
table.add_row(["Squirtle", "Water"])
table.add_row(["Charmander", "Fire"])
table.align = 'l'
print(table.align)

print(table)
