import os, struct, sys, getopt, argparse, numpy as np

class particle:
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z


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


    voxels = create_voxels(nx,ny,nz)
    calc_density(filename, count_particles)
    print_pbrt_file()

def calc_voxel_size(nx,ny,nz):
    #Radio mayor o poloidal
    R = 0.2381

    #Radio menor o toroidal
    r = 0.09444165

    #Voxel size X
    x1 = particle(R+r, R+r, r)
    x2 = particle(R+r, -(R+r), r)
    dist_x = dist_eucl(x1,x2)
    vox_x = dist_x / nx

    #Voxel size Y
    y1 = particle(R + r, R + r, r)
    y2 = particle(R + r, -(R + r), r)
    dist_y = dist_eucl(y1, y2)
    vox_y = dist_y / ny

    #Voxel size z
    z1 = particle(R + r, R + r, r)
    z2 = particle(R + r, -(R + r), r)
    dist_z = dist_eucl(z1, z2)
    vox_z = dist_z/nz

    #incialización de voxels
    voxels = np.zeros((nx,ny,nz))


    #identificar con esos puntos la distancia euclidiana
    return voxels

def dist_eucl(particle1, particle2):
    a = np.array((particle1.x, particle1.y, particle1.z))
    b = np.array((particle2.x, particle2.y, particle2.z))
    return np.linalg.norm(a-b)


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
    # Radio mayor o poloidal
    R = 0.2381

    # Radio menor o toroidal
    r = 0.09444165

    # Calculo de puntos de extensión
    ext_point1 = particle(R + r, R + r, r)
    ext_point2 = particle(-(R + r), -(R + r), -r)

    pbrt_file = open("pbrt_files/density_model.pbrt", "a")
    # pbrt_file.write(header)
    try:
    except NameError as e:
        print(e)
        # pbrt_file.close()
    # pbrt_file.write(line)

if __name__ == '__main__':
    main()
