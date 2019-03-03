from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
	 Every command is a single character that takes up a line
	 Any command that requires arguments must have those arguments in the second line.
	 The commands are as follows:
		 line: add a line to the edge matrix -
			   takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
		 ident: set the transform matrix to the identity matrix -
		 scale: create a scale matrix,
				then multiply the transform matrix by the scale matrix -
				takes 3 arguments (sx, sy, sz)
		 translate: create a translation matrix,
					then multiply the transform matrix by the translation matrix -
					takes 3 arguments (tx, ty, tz)
		 rotate: create a rotation matrix,
				 then multiply the transform matrix by the rotation matrix -
				 takes 2 arguments (axis, theta) axis should be x y or z
		 apply: apply the current transformation matrix to the edge matrix
		 display: clear the screen, then
				  draw the lines of the edge matrix to the screen
				  display the screen
		 save: clear the screen, then
			   draw the lines of the edge matrix to the screen
			   save the screen to a file -
			   takes 1 argument (file name)
		 quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
	with open(fname) as f:
		i = f.readline()[:-1]
		while i:
			if i == 'line':
				i = f.readline()[:-1]
				temp = [int(x) for x in i.split(' ')]
				add_edge(points,temp[0],temp[1],temp[2],temp[3],temp[4],temp[5])
			elif i == 'ident':
				ident(transform)
			elif i == 'scale':
				i = f.readline()[:-1]
				temp = [int(x) for x in i.split(' ')]
				matrix_mult(make_scale(temp[0],temp[1],temp[2]),transform)
			elif i == 'translate':
				i = f.readline()[:-1]
				temp = [int(x) for x in i.split(' ')]
				matrix_mult(make_translate(temp[0],temp[1],temp[2]),transform)
			elif i == 'rotate':
				i = f.readline()[:-1]
				temp = i.split(' ')
				if temp[0] == 'x':
					matrix_mult(make_rotX(int(temp[1])),transform)
				elif temp[0] == 'y':
					matrix_mult(make_rotY(int(temp[1])),transform)
				elif temp[0] == 'z':
					matrix_mult(make_rotZ(int(temp[1])),transform)
			elif i == 'apply':
				matrix_mult(transform,points)
			elif i == 'display':
				clear_screen(screen)
				draw_lines(points,screen,color)
				display(screen)
			elif i == 'save':
				clear_screen(screen)
				draw_lines(points,screen,color)
				i = f.readline()[:-1]
				save_extension(screen,i)
			elif i == 'quit':
				return
			i = f.readline()[:-1]
