from functions.run_python import run_python_file


def test():
    print("Result 1:\n")
    print(run_python_file("calculator", "main.py"), "\n")
    print("Result 2:\n")
    print(run_python_file("calculator", "main.py", ["3 + 5"]), "\n")
    print("Result 3:\n")
    print(run_python_file("calculator", "tests.py"), "\n")
    print("Result 4:\n")
    print(run_python_file("calculator", "../main.py"), "\n")
    print("Result 5:\n")
    print(run_python_file("calculator", "nonexistent.py"), "\n")


if __name__ == "__main__":
    test()
