import os

# print(dir(os))

print(os.getcwd())

os.chdir("/Users/mac/Desktop/Sample")


print(os.getcwd())

print(os.listdir())

print("*"*20)

for path, dir, file in os.walk("/Users/mac/Desktop"):
    print(path)
    print(dir)
    print(file)