import os


def main():

    directory = input("please input directory: ")

    if os.path.isdir(directory):
        dir_analyse(directory)
    else:
        print("Directory {} does not exist".format(directory))


def dir_analyse(directory):

    total_size = 0

    # open file for writing
    file_obj = open("data.txt", "w")

    # run through the directory line by line
    for file_name in os.listdir(directory):

        # if file is doc or txt, write line
        if os.path.splitext(file_name)[1] == ".doc" or os.path.splitext(file_name)[1] == ".txt":
            file_obj.write("{}\n".format(file_name))

    # finally close file object
    file_obj.close()


main()
