class TryExceptFinally:


    def main():
        a = "a"/0
    if __name__ == '__main__':
        try:
            main()
        except ZeroDivisionError:
            pass
        except:
            print("something's wrong")
        finally:
                print("finished")


try:
    x = 1

finally:
    print("fin")

# from docx import Document

try:
    create_file = open("C:\\temp\\words.doc", 'x')
except:
    create_file = open("C:\\temp\\words.doc", 'r+')
    print("the file exists already")
finally:
    contents = create_file.write("Yury")

my_file = open("C:\\temp\\words.doc")
contents = my_file.read()
print(contents)

heb_f = open("C:\\temp\\heb-words.txt", 'w', encoding='utf-8')
contents = heb_f.write("דגכעיחל")
# read_contents = heb_f.read()
# print(read_contents)


# h_contents = hebrew_file.read()
# print(h_contents)
# print(hebrew_file)