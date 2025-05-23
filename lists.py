# Replace the "ANSWER HERE" with your answer

def remove_elements(list_to_remove_elements):
    result = list_to_remove_elements [:]
    for i in [5, 4, 0]:
        if i < len(result):
            del result[i]
    return result # Remove this line and implement

sample1 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
output = remove_elements(sample1)
print(sample1)

def add_elements(list_to_add_elements):
    list_to_add_elements.insert(0,"Pink")
    list_to_add_elements.append("Yellow")
    return list_to_add_elements 
sample2= ['Red', 'Green', 'White', 'Black']
output = add_elements(sample2)
print(output)

def is_empty(list_to_check):
    if len(list_to_check) == 0:
        return "Vacia"
    else: "Tiene contenido"

sample3= []
output = is_empty(sample3)
print(output)

def check_lists(list_to_compare1, list_to_compare2):
    if len(list_to_compare1) >= 3 and len(list_to_compare2)>= 3:
        return list_to_compare1[2] == list_to_compare2[2]
    else:
        False
Lista1 = ['Gato', 'Perro', 'Cabra', 'Jirafa']
Lista2 = ['Perro', 'Gato', 'Cabra', 'Vaca', 'Koala',]
output = check_lists(Lista1,Lista2)
print(output)

def list_of_lists(list_of_lists_to_modify):
  if len(list_of_lists_to_modify) == 3:
    list_of_lists_to_modify[0] = list_of_lists_to_modify[0][:2]
    list_of_lists_to_modify[1] = list_of_lists_to_modify[1][1:4]
    list_of_lists_to_modify[2] = list_of_lists_to_modify[2][-2:]
  return list_of_lists_to_modify

List= [[1, 2, 3], [4, 5, 6, 7, 8], [9, 10, 11, 12]]
output = list_of_lists(List)
print(output)
