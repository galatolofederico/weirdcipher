import argparse
from weirdcipher import WeirdCipher

def main():
    r"""
    You can use ``weirdcipher`` with the CLI interface

    To encrypt a string

    >>> weirdcipher --key "your-key" your message

    To decrypt a ciphertext

    >>> weirdcipher --key "your-key" --decrypt kWSMDWGvoiMy32f5
    """

    parser = argparse.ArgumentParser()

    parser.add_argument("--key", required=True)
    parser.add_argument("--decrypt", action="store_true")
    parser.add_argument("--encoding", default="utf-8")
    parser.add_argument("message", type=str, nargs="+")

    args = parser.parse_args()
    message = " ".join(args.message)

    cipher = WeirdCipher(args.key, encoding=args.encoding)
    if args.decrypt:
        message = cipher.decrypt(message)
    else:
        message = cipher.encrypt(message)

    print(message)


if __name__ == "__main__":
    main()