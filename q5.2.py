import crypt
import timeit


def password_encrypt(password):
    encrypted_pass=crypt.crypt(password)
    return encrypted_pass


def main():
    password = input("please enter password: ")
    print("The encrypted password is {}".format(password_encrypt(password)))

    code='''def password_encrypt(password):
    encrypted_pass=crypt.crypt(password)
    return encrypted_pass'''
    time = timeit.timeit(code, "import crypt")
    print(time)

main()