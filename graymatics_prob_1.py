class Knapsack:
    def __init__(self, name, weight,value):
        self.name=name
        self.weight=weight
        self.value=value

def items(list_of_items, max_weight, no_items):

    if no_items == 0 or max_weight == 0:
        return 0
    if (list_of_items[no_items-1].weight > max_weight):
        return items(list_of_items, max_weight, (no_items-1))
    else:
        return max(
            list_of_items[no_items-1].value + items(list_of_items, (max_weight-list_of_items[no_items-1].weight), (no_items-1)),
            items(list_of_items, max_weight, (no_items-1))
        )

  
 
if __name__=="__main__":
    item_1=Knapsack("map", 9, 150)
    item_2=Knapsack("compass", 13, 35)
    item_3=Knapsack("water", 153,200)
    item_4=Knapsack("sandwich",50,160)
    item_5=Knapsack("glucose", 15,60)
    item_6=Knapsack("tin", 68,45)
    item_7=Knapsack("banana", 27,60)
    item_8=Knapsack("apple", 39,40)

    list_of_items=[item_1,item_2,item_3,item_4,item_5,item_6,item_7,item_8]

    total_value=items(list_of_items, 100, len(list_of_items))
    print(total_value)