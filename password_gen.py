from string import digits, ascii_letters
import secrets


# Let's create cryptographically strong random numbers. Using the module "secrets" allow us to avoid weakness of
# pseudorandom number generator.
def pass_gen(length=4):
    return (secrets.choice(digits + ascii_letters + "!@#$%^&*~+=") for _ in range(length))


# Generate a 16-character password separated by a dash every 4 characters.
if __name__ == "__main__":
    password = ''
    for i in range(4):
        password += ''.join(pass_gen())
        if i < 3:
            password += '-'
# Example output: "9xIU-O5g#-eGZ9-U348"
