# start with some designs that need to be printed
unprinted_designs=['phone case', 'robot pendant', 'dodecahedron']
completed_models=[]
#simulate printing each design until none are left
#move each design to completed model after printing
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design=unprinted_designs.pop()
        print(f"printing model: {current_design}")
        completed_models.append(current_design)
def show_completed_models(completed_models):
    print("the following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)