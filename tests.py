from functions.get_file_content import get_file_content


def test():
    print("file_content_1:")
    print(get_file_content("calculator", "main.py"))
    print("file_content_2:\n")
    print(get_file_content("calculator", "pkg/calculator.py"))
    print("file_content_3:\n")
    print(get_file_content("calculator", "/bin/cat"))
    print("file_content_4:\n")
    print(get_file_content("calculator", "pkg/does_not_exist.py"))


if __name__ == "__main__":
    test()
