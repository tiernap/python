import os


def main():

    # ask user for directory path
    directory = input("please input directory: ")

    # run dir_size function if directory exists
    if os.path.isdir(directory):
        dir_size(directory)
    else:
        print("Directory {} does not exist".format(directory))


def dir_size(directory):

    total_size = 0

    # for all files in directory, count size
    for file_name in os.listdir(directory):
        print("{}".format(file_name))
        size = os.path.getsize(os.path.join(directory, file_name))
        total_size = total_size + size
        print("The Contents of {} directory is: {}".format(directory, total_size))

        # if file_name is itself a directory, run nested function
        if os.path.isdir(os.path.normpath(directory+"/"+file_name)):
            dir_size(os.path.normpath(directory+"/"+file_name))


main()
