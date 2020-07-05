# Way 1: Write data
# file_obj = open('sample.txt', mode='w')
# for i in range(10):
#     file_obj.write(f'Testleaf - Python {i}\n')
# print(file_obj.closed)
# file_obj.close()
# print(file_obj.closed)

# Way 2: Write data
with open('data.txt', mode='w') as file_obj:
    for i in range(10):
        file_obj.write(f'5 * {i} = {5 * i}\n')

with open('data.txt', mode='r') as file_obj:
    data = file_obj.read()
    print(data)