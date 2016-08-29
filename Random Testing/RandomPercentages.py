import random
my_list = 5*[1]+95*[6]
print(my_list)
for i in range(100):
    print(random.choice(my_list))