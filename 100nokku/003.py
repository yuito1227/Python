import sys


def main(lines):
    print(lines[0])


if __name__ == "__main__":
    lines = []
    for li in sys.stdin:
        lines.append(li.rstrip("\r\n"))
    main(lines)
