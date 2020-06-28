import os, struct, sys, getopt

def main(argv):
    if len(argv) == 0:
        print('BinaryToText.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print('BinaryToText.py -i <inputfile> -o <outputfile>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('BinaryToText.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    if inputfile == '':
        print('BinaryToText.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    if outputfile == '':
        outputfile = inputfile

    convert_file(inputfile, outputfile)


def convert_file(input_file, output_file):
    with open("bin_files/"+input_file+".bin", "rb") as bin_file:
        text_file = open("text_files/"+output_file+".csv", "a")
        bin_file_content = bin_file.read()
        header = parse_header(str(struct.unpack('cccccc', bin_file_content[:6])))
        text_file.write(header)
        line = ' '
        index = 6
        struct_size = 32
        file_size = os.path.getsize("bin_files/"+input_file+".bin")
        while index < file_size:
            try:
                line = parse_line(str(struct.unpack_from('dddc', bin_file_content, index)))
            except NameError as e:
                print(e)
                text_file.close()
            text_file.write(line)
            index += struct_size
        text_file.close()
    bin_file.close()


if __name__ == '__main__':
    main(sys.argv[1:])
