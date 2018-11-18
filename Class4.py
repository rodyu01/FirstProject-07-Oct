TXT_file = open("C:\\Users\\CaField\\Documents\\Assignment_1.txt", 'a+', encoding='koi8-r')

Wtxt_file = open("C:\\Users\\CaField\\Documents\\New_assignment.txt", 'w')

# content = TXT_file.read()

# print(content)
# TXT_file.close()

# print(TXT_file.read()

content = TXT_file.write("\n\n\nasdfghj\nklqwertyuio\npzxcvbnm,")

TXT_file.close()
Wtxt_file.close()


try:
    f = open("C:\\Users\\CaField\\Documents\\New_assignment1.txt", 'r')
except:
     print('happens')
finally:
    print("dfghjk")


from selenium import webdriver