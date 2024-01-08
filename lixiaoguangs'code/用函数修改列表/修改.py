#每个函数只完成一种具体的工作
#比用一个函数完成两项工作要好
def print_models(unprinted_designs,completed_models):
    """模拟每个打印设计，直到没有"""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        #打印设计函数很简单
        print("Printing model:" + current_design)
        completed_models.append(current_design)
        #将设计以个个从unprinted_designs移到completed_models
#再次写一个显示列表的函数
def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case','robot pendant','dodecahedron']
completed_models = []

print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)
#將列表以副本传播,用[:]
print_models(unprinted_designs[:],completed_models)
print(unprinted_designs)

