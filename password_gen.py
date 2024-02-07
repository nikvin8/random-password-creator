from string import digits, ascii_letters
import secrets


def pass_gen():
    return '-'.join([''.join([secrets.choice(digits + ascii_letters) for _ in range(8)]) for i in range(4)])


if __name__ == "__main__":
    pass_gen()
