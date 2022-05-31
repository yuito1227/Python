import sys


def main(lines):
    a, b = map(int, lines[0].split())
    print(f"和: {a+b}")
    print(f"差: {a-b}")
    print(f"積: {a*b}")
    print(f"商: {a//b},余り: {a%b}")


if __name__ == "__main__":
    lines = []
    for li in sys.stdin:
        lines.append(li.rstrip("\r\n"))
    main(lines)
