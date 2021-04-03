def tallest_people(**people):
    max_height = max(people.values())
    names = [k for k, v in people.items() if v == max_height]
    names.sort()
    for name in names:
        print(f'{name} : {max_height}')
