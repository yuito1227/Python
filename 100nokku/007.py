import sys


def main(lines):
    a = int(lines[0])
    s = "zero" if a == 0 else "not zero"
    print(s)


if __name__ == "__main__":
    lines = []
    for li in sys.stdin:
        lines.append(li.rstrip("\r\n"))
    main(lines)
