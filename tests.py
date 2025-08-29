from functions.write_content import write_file


def test():
    print("Result 1:\n")
    print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"), "\n")
    print("Result 2:\n")
    print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"), "\n")
    print("Result 3:\n")
    print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))

if __name__ == "__main__":
    test()
