def read_file(file_name):
    try:
        f = open(file_name, "r")
    except:
        return ("__CONTENT_START__\n" + " __NO_SUCH_FILE__" + "\n__CONTENT_END__\n")
    else:
        return ("__CONTENT_START__\n" + f.read() + "\n__CONTENT_END__\n")
    finally:
        print("done")

print(read_file("works.txt"))
print(read_file("w"))
