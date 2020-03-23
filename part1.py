
import numpy as np
import math

import random
random.seed(1)


def row1_pdf(x):
	return (6 - x) / 16

def row1_inv_cdf(x):
	return 6 - 2 * math.sqrt(9 - 8 * x)


def row2_pdf(x):
	return 1/4

def row2_inv_cdf(x):
	return 4 * x


def row3_pdf(x):
	return (x + 2) / 16
	
def row3_inv_cdf(x):
	return -2 + 2 * math.sqrt(1 + 8 * x)


def row4_pdf(x):
	return x / 8
	
def row4_inv_cdf(x):
	return 4 * math.sqrt(x)


# Row 1
variance = 0
error = 1000
numSamples = 0
while error > 0.008:
	# Variance
	randVal = random.random()
	mc = row1_inv_cdf(randVal)
	variance += np.power(mc / row1_pdf(mc) - 8.0, 2.0)
	
	numSamples += 1
	
	avgVar = (1.0 / numSamples) * variance
	error = math.sqrt(avgVar / numSamples)

print("\nRow 1:\nVariance: " + str(avgVar) + "\nNumSamples: " + str(numSamples) + "\n\n")


# Row 2
variance = 0
error = 1000
numSamples = 0
while error > 0.008:
	# Variance
	randVal = random.random()
	mc = row2_inv_cdf(randVal)
	variance += np.power(mc / row2_pdf(mc) - 8.0, 2.0)
	
	numSamples += 1
	
	avgVar = (1.0 / numSamples) * variance
	error = math.sqrt(avgVar / numSamples)

print("\nRow 2:\nVariance: " + str(avgVar) + "\nNumSamples: " + str(numSamples) + "\n\n")


# Row 3
variance = 0
error = 1000
numSamples = 0
while error > 0.008:
	# Variance
	randVal = random.random()
	mc = row3_inv_cdf(randVal)
	variance += np.power(mc / row3_pdf(mc) - 8.0, 2.0)
	
	numSamples += 1
	
	avgVar = (1.0 / numSamples) * variance
	error = math.sqrt(avgVar / numSamples)
	
print("\nRow 3:\nVariance: " + str(avgVar) + "\nNumSamples: " + str(numSamples) + "\n\n")


# Row 4
variance = 0
error = 1000
numSamples = 0
while error > 0.008:
	# Variance
	randVal = random.random()
	mc = row4_inv_cdf(randVal)
	variance += np.power(mc / row4_pdf(mc) - 8.0, 2.0)
	
	numSamples += 1
	
	avgVar = (1.0 / numSamples) * variance
	error = math.sqrt(avgVar / numSamples)
	
print("\nRow 4:\nVariance: " + str(avgVar) + "\nNumSamples: " + str(numSamples) + "\n\n")