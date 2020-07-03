str1 = " an apple a day a day keeps the doctor away ! #$ efd , ;,, sd,  "
# print(str1)

str2 = str1

# str1 = str1.replace(" ! ", "     s fd   d f   d")
# print(str1)
# str1 = str1.split()

# print(str1)
print("###")
print (str2)

import re
split_list = [" ", "apple"]
str2 = re.split(";|,|\*|\n| ", str2)
print(str2)