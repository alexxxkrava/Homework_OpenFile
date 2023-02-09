with open('recipes.txt', 'r+', encoding = 'UTF-8') as file:
    cook_book = {}
    for line in file:
        dishes = line.strip()
        count = int(file.readline())
        all_parts = []
        for i in range(count):
            parts = file.readline().strip()
            ingredient_name, quantity, measure = parts.split(' | ')
            all_parts.append({
                'ingredient_name':ingredient_name,
                'quantity':quantity,
                'measure':measure
            })
        cook_book[dishes] = all_parts
        file.readline()
    print(cook_book)

def get_shop_list_by_dishes(dishes, person_count):




