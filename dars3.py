import os
os.system("cls")


######      20-masala
# def ask_nums():
#     a = int(input("How many numbers will u add: "))
#     result = [int(input(f"Insert {i + 1} - number: ")) for i in range(a)]
#     return result

# def find_little_num(a):
#     result = [a[i] for i in range(0, len(a) - 1) if a[i] < a[i + 1]]
#     return result

# nums = ask_nums()
# print(find_little_num(nums))











#######     21-masala
# def ask_nums():
#     num = int(input("How many nums will you insert? "))
#     result = [int(input(f"Insert {i + 1} - number: ")) for i in range(num)]
#     return result

# def checker(a):
#     return sorted(a) == a

# nums = ask_nums()
# print(checker(nums))











######      22-masala           1-usul
# def ask_nums():
#     num = int(input("How many nums will you insert? "))
#     result = [int(input(f"Insert {i + 1} - number: ")) for i in range(num)]
#     return result

# def printer(a):
#     if sorted(a, reverse=True) == a:
#         return "0"
#     else:
#         for i in range(len(a)):
#             if a[i] < a[i + 1]:
#                 return a[i + 1]

# nums = ask_nums()
# print(printer(nums))

####                              2-usul      
# def ask_nums():
#     num = int(input("How many nums will you insert? "))
#     result = [int(input(f"Insert {i + 1} - number: ")) for i in range(num)]
#     return result

# def printer(a):
#     return "0" if sorted(a, reverse=True) == a else next((a[i + 1] for i in range(len(a)) if a[i] < a[i + 1]))

# nums = ask_nums()
# print(printer(nums))












# #######        23-masala
# def ask_nums():
#     num = int(input("How many nums will you insert? "))
#     result = [int(input(f"Insert {i + 1} - number: ")) for i in range(num)]
#     return result

# def printer(a):
#     for i in range(1, len(a) - 1):
#         if not (a[i - 1] < a[i] > a[i + 1] or a[i - 1] > a[i] < a[i + 1]):
#             return a[i]
#     return "0"
        
# nums = ask_nums()
# print(printer(nums))










#######         24-masala
# def ask_nums():
#     a = int(input("How many numbers will you insert? "))
#     result = [int(input(f"Insert the {i + 1} - number: ")) for i in range(a)]
#     return result

# def finder(a):
#     a_copy = a.copy()
#     reversed_a = a_copy[::-1]
#     index1 = reversed_a.index(0)
#     index2 = reversed_a[index1 + 1:].index(0) + index1 + 1
#     return sum(reversed_a[index1 + 1:index2])

# nums = ask_nums()
# print(finder(nums))









####    [12, 0, 34, 345, 37, 0, 534, 56]

######      25-masala
# def ask_nums():
#     a = int(input("How many numbers will you insert? "))
#     result = [int(input(f"Insert the {i + 1} - number: ")) for i in range(a)]
#     return result

# def finder(a):
#     index1 = a.index(0) #1
#     index2 = a[index1 + 1:].index(0) + index1 + 1
#     return sum(a[index1:index2])

# nums = ask_nums()
# print(finder(nums))













#####       26-masala
# def ask_num():
#     a = int(input("How many numbers will you add? "))
#     result = [int(input(f"insert {i + 1} - number: ")) for i in range(a)]
#     return result
    
# def printer(a):
#     value_of_k = int(input("Insert the value of \"k\": "))
#     result = [i**value_of_k for i in a]
#     return result

# nums = ask_num()
# print(printer(nums))
    
    
    
    
    




#####       27 - masala
# def ask_nums():
#     a = int(input("How many numbers will you insert? "))
#     result = [int(input(f"Insert {i + 1} - number: ")) for i in range(a)]
#     return result

# def printer(a):
#     return [i**(a.index(i) + 1) for i in a]

# nums = ask_nums()
# print(printer(nums))








        
#######     28-masala
# def ask_num():
#     a = int(input("How many numbers will you insert? "))
#     num_list = [int(input(f"Insert {i + 1} - number: ")) for i in range(a)]
#     return num_list, a

# def printer(list_, len_list):
#     return [list_[i]**(i + 1) for i in range(len_list)]
    
# num_list, len_list = ask_num()
# print(printer(num_list, len_list))    
        
        
        
        
        
        
        
        
        


######      29-masala
# def ask_num():
#     a = int(input("How many numbers will you insert? "))
#     num_list = [int(input(f"Insert {i + 1} - number: ")) for i in range(a)]
#     return num_list

# def printer(list_):
#     return sum(list_)
    
# num_list = ask_num()
# print(printer(num_list))  

        