import sys


def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.

    for line in lines:
        X, Y, Z = map(int, line.split())


if __name__ == "__main__":
    lines = []
    for li in sys.stdin:
        lines.append(li.rstrip("\r\n"))
    main(lines)
