# 3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# Например:
# >>>  thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#     "И": ["Иван", "Илья"],
#     "М": ["Мария"], "П": ["Петр"]
# }
# Подумайте: полезен ли будет вам оператор распаковки?
# Как поступить, если потребуется сортировка по ключам? Можно ли использовать словарь в этом случае?

def thesaurus(*names):
    out_dict = {}
    for name in names:
        if not (out_dict.get(name[0])):
            out_dict[name[0]] = [name]
        else:
            out_dict[name[0]].append(name)
    return out_dict

print(thesaurus("Иван", "Мария", "Петр", "Илья"))
