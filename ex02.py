inventer = [
    ["Apple",50,0.75],
    ["Banana",100,0.50],
    ["orange",75,0.80]
    ]
def update_inventer(inventer,item_name,quantity_sold):
    for item in inventer:
        if item_name == item[0]:
            item[1] = item[1] - quantity_sold

print(inventer)
update_inventer(inventer,"Banana",20)
print(inventer)

def calculate_total_value(inventer):
    total = 0
    for inv in inventer :
        total = total + inv[1] * inv[2]
print()

        
