from display import *
from draw import *
from parser import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

# add_edge(edges,1,2,3,4,5,6)
# add_edge(edges,2,4,6,1,3,5)

# ident(transform)
# matrix_mult(make_translate(1,2,3),transform)
# print_matrix(transform)
# matrix_mult(transform,edges)
# print_matrix(edges)

# ident(transform)
# matrix_mult(make_scale(3,4,5),transform)
# print_matrix(transform)
# matrix_mult(transform,edges)
# print_matrix(edges)

# ident(transform)
# matrix_mult(make_rotX(math.pi/2),transform)
# print_matrix(transform)
# matrix_mult(transform,edges)
# print_matrix(edges)

# ident(transform)
# matrix_mult(make_rotY(math.pi/2),transform)
# print_matrix(transform)
# matrix_mult(transform,edges)
# print_matrix(edges)

# ident(transform)
# matrix_mult(make_rotZ(math.pi/2),transform)
# print_matrix(transform)
# matrix_mult(transform,edges)
# print_matrix(edges)

parse_file( 'script', edges, transform, screen, color )
