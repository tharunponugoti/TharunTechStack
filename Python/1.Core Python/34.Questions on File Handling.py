with open("sample.txt", "r") as file:
    content = file.read()
    print("File Content:")
    print(content)
    print("Number of Characters:", len(content))



with open("sample.txt", "r") as file:
    lines = file.readlines()

print("Lines with more than 10 characters:")

for line in lines:
    if len(line.strip()) > 10:
        print(line.strip())






with open("demo.txt", "w") as file:
    file.write("Python\n")
    file.write("Java\n")
    file.write("C++\n")

with open("demo.txt", "a") as file:
    file.write("SQL\n")
    file.write("Django\n")

with open("demo.txt", "r") as file:
    print(file.read())






with open("sample.txt", "r") as file:
    data = file.read(10)
    print("First 10 Characters:", data)

    print("Cursor Position:", file.tell())

    file.seek(0)

    print("\nComplete File Content:")
    print(file.read())






class FileManager:

    def __enter__(self):
        self.file = open("custom.txt", "w")
        self.file.write("Hello from Custom Context Manager\n")
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()

        if exc_type:
            print("Exception Type:", exc_type)
            print("Exception Value:", exc_value)

        print("File Closed")


with FileManager() as file:
    file.write("Second Line\n")





from contextlib import contextmanager

@contextmanager
def open_file(filename, mode):
    file = open(filename, mode)
    try:
        yield file
    finally:
        file.close()
        print("File Closed Successfully")


with open_file("sample.txt", "r") as file:
    print(file.read())






with open("sample.txt", "r") as file:

    while True:
        data = file.read(5)

        if not data:
            break

        print("Read:", data)
        print("Cursor Position:", file.tell())

    file.seek(10)

    print("\nReading Again From Position 10:")
    print(file.read())










