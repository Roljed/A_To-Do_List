# finish the function
def find_the_parent(child):
    parent_classes = [Drinks, Pastry, Sweets]
    for parent_class in parent_classes:
        if issubclass(child, parent_class):
            print(parent_class.__name__)
