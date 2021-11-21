# 2. * (вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно),
# не используя ключевое слово yield.

max_num = 15
odd_nums_generator = (i for i in range(1, max_num + 1, 2))
print(next(odd_nums_generator))
print(next(odd_nums_generator))
print(next(odd_nums_generator))
print(next(odd_nums_generator))
print(next(odd_nums_generator))
print(next(odd_nums_generator))
print(next(odd_nums_generator))
print(next(odd_nums_generator))
print(next(odd_nums_generator))