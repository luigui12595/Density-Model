import os, struct, sys, getopt, argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--particles", type=str,
                        help="particles filename", required=True)
    parser.add_argument("-nx", type=int,
                        help="divide the x axis by given number", required=True)
    parser.add_argument("-ny", type=int,
                        help="divide the y axis by given number", required=True)
    parser.add_argument("-nz", type=int,
                        help="divide the z axis by given number", required=True)
    parser.add_argument("-t", "--total_particles", type=int,
                        help="number of total particles", required=True)

    args = vars(parser.parse_args())
    nx = args['nx']
    ny = args['ny']
    nz = args['nz']
    filename = args['particles']
    count_particles = args['total_particles']
    create_voxels(nx,ny,nz)
    calc_density(filename, count_particles)
    print_pbrt_file()

def create_voxels(nx,ny,nz):
    R = 0.015
    r = 0.00006
    #identificar puntos vértices
    #identificar con esos puntos la distancia euclidiana

def calc_density(input_file, count_particles):
    with open("bin_files/"+input_file+".bin", "rb") as bin_file:
        bin_file_content = bin_file.read()
        line = ' '
        index = 0
        struct_size = 24
        file_size = os.path.getsize("bin_files/"+input_file+".bin")
        while index < file_size:
            try:
                line = str(struct.unpack_from('ddd', bin_file_content, index))
                #identificar el voxel de acuerdo a las coordenadas en los ejes
                #
            except NameError as e:
                print(e)
            index += struct_size
    bin_file.close()


def print_pbrt_file():
    # pbrt_file = open("pbrt_files/density_model.pbrt", "a")
    # pbrt_file.write(header)
    try:
    except NameError as e:
        print(e)
        # pbrt_file.close()
    # pbrt_file.write(line)

if __name__ == '__main__':
    main()
