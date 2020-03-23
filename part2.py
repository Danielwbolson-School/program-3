
import numpy as np
import random

def normalize(v):
	norm = np.linalg.norm(v)
	if norm == 0:
		return v
	return v / norm

# Open our file to write our new vertices
f = open("part2.obj", "a")

# Set our input variables
e = 75
nSamples = 25
lightVec = np.array([-0.70711, 0, 0.70711])
reflect = np.array([0.70711, 0, 0.70711])
normal = np.array([0, 0, 1])
toWorld = np.matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]])

# Calculate our tbn matrix to move from tangent space to world
n = normalize(reflect)
t = normalize(np.cross(n, lightVec))
b = normalize(np.cross(n, t))
tbn = np.array([t, b, n])
invTbn = np.transpose(tbn)

for i in range(0, nSamples):
	
	theta = np.arccos(np.power(random.random(), 1 / (e + 1)))
	phi = 2 * np.pi * random.random()
	
	# New view vector IN TANGENT SPACE w/reflect as normal
	x = np.sin(theta) * np.cos(phi)
	y = np.sin(theta) * np.sin(phi)
	z = np.cos(theta)
	viewVec = normalize(np.array([x, y ,z]))
	
	# Convert our view vector from tangent space
	viewVec = np.dot(invTbn, viewVec)
	
	# Calculate magnitude of vector
	spec = reflect @ viewVec
	spec = np.power(spec, e)

	newVec = spec * viewVec
	
	f.write("\nv " + str(newVec[0]) + " " + str(newVec[1]) + " " + str(newVec[2]))
	f.write("\nl 1 " + str(i + 9))
