import sys


def main(lines):
    a = int(lines[0])
    print(f"answer = {a*3}")


if __name__ == "__main__":
    lines = []
    for li in sys.stdin:
        lines.append(li.rstrip("\r\n"))
    main(lines)
