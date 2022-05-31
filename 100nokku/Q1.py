# import sys
import os

for i in range(1, 100):
    old_name = f"{i+1:0=3}.py"
    new_name = f"{i:0=3}.py"
    os.rename(old_name, new_name)

# def main(lines):
#     f = open("test.txt", "r")
#     code = f.read()
#     f.close()
#     for i in range(100):
#         file_name = f"{i+1:0=3}.py"
#         f = open(file_name, "w")
#         f.write(code)
#         f.close()


# if __name__ == "__main__":
#     lines = []
#     # for li in sys.stdin:
#     #     lines.append(li.rstrip("\r\n"))
#     main(lines)
