


# # write a code to rotate the entered number by the user clockwise - right rotation. 
# # input: 45371
# #        2 ---> number of rotations
# # output:37145

# number = int(input("Enter a number: "))
# rotations = int(input("Enter number of rotations: "))
# splited = [int(digit) for digit in str(number)]

# print(splited)
# leftout = []
# result = []
# for i in range(0, rotations):
#     result.append(splited[i])
#     splited.remove(splited[i])

# # print(splited+result) 
# # # print(result)
# # # print(leftout)

# digits = []
# while number > 0:
#     digits.append(number % 10)
#     number = number // 10
# digits.reverse()
# print(digits)

# 71%10 ==> 1
# 371 % 10 ==> 71