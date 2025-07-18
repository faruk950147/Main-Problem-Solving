import itertools
import string

password = string.ascii_letters + string.digits + string.punctuation
for i in range(1, 5):
    for j in itertools.product(password, repeat=i):
        # join j tuple into string
        word = ''.join(j)
        # password warehouse
        with open("password.txt", "a") as f:
            try:
                f.write(word + "\n")
                print(f"Password Generated Successfully: {word}")
            except Exception as e:
                print("Exception", str(e))