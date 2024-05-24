cargo = ['диван', 'чемодан', 'саквояж','картина', 'корзина', 'картонка', 'маленькая собачонка']
my_list = cargo
print(my_list)
print(my_list [0])
print(my_list[-1])
print(my_list [2:4]) # с третьего до пятого
print(cargo [2:5]) # с третьего до пятого включительно
my_list[-1] = 'взъерошенный пёс' # замена последнего (по смыслу))
print(my_list)
my_list[-1] = 'маленькая собачонка'
my_list[2] = 'сумка' # замена третьего по заданию
print(my_list)
cargo = {'диван': 'sofa', 'чемодан': 'suitcase', 'саквояж': 'travel bag', 'картина': 'picture', 'корзина': 'cart', 'картонка': 'cardboard', 'маленькая собачонка': 'a little dog'}
my_dict=cargo
print(my_dict)
print(my_dict['картонка'])
my_dict['пёс'] = 'dog' # добавить новый
print(my_dict)