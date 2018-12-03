import os


def main():

    directory = input("please input directory: ")

    if os.path.isdir(directory):
        dir_size(directory)
    else:
        print("Directory {} does not exist".format(directory))


def dir_size(directory):

    total_size = 0

    for file_name in os.listdir(directory):
        print("{}".format(file_name))
        size = os.path.getsize(os.path.join(directory, file_name))
        total_size = total_size + size
        print("The Contents of {} directory is: {}".format(directory, total_size))

main()
