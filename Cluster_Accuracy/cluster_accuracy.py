# Homework 2 program to determine accuracy for clustering.

import numpy
import sys
from munkres import Munkres

# Paths for the input files.
data_label_path = './data_label.txt'
clustering_result_path = './clustering_result.txt'
output_file_path = './clustering_accuracy.txt'

# Lists to hold contents of input files.
data_label = []
clustering_result = []

# Sets to verify count of labels and count of clusters match.
data_label_set = set()
clustering_result_set = set()

# Read data label file.
try:
    with open(data_label_path, 'r') as data_label_input:
        for current_label in data_label_input:
            data_label.append(int(current_label.split(' ')[0]))
            data_label_set.add(int(current_label.split(' ')[0]))
except:
    error_message = 'File + ' + data_label_path + ' not found.'
    exit(error_message)
data_label_input.close()

# Read clustering results file
try:
    with open(clustering_result_path, 'r') as clustering_result_input:
        for current_result in clustering_result_input:
            clustering_result.append(int(current_result.rstrip('\n')))
            clustering_result_set.add(int(current_result.rstrip('\n')))
except:
    error_message = 'File + ' + clustering_result_path + ' not found.'
    exit(error_message)
clustering_result_input.close()

explanation = """
Nick Petty
CAP6776 Homework 3

Accuracy = max (sum{Ck, Lm} T(Ck, Lm)) /n
Where n = number of data points, Ck denotes kth cluster, Lm is the mth class, and T(Ck, Lm) is the number of data points that belong to class m and are assigned to cluster k.  Because k and m refer to the number of classes in the data set, they must be equal.

Finding the maximum sum of T(Ck, Lm), when given T in matrix form, is a variation on the Assignment Problem.  Solving this problem via brute force will give a run time of m!, which is excessive.  Instead, the Munkres algorithm (or the Hungarian Algorithm) is used.  This gives a run time of m^3, which is much better.

To use the Munkres algorithm, the Python munkres package has been imported.
Package documentation: https://pypi.python.org/pypi/munkres/
The matrix from T(Ck, Lm) does not immediately work with this algorithm, as it is designed to find the minimum sum.  A second matrix, composed of a very large number minus each cell value in the T matrix must also be created.  This larger-valued matrix, when given to the algorithm, will then find the maximum sum.\n"""

# Set variables for calculation:

# Verify that count of labels matches count of clusters.  Find the number of classes m and clusters k.
if len(data_label_set) == len(clustering_result_set):
    m = len(data_label_set)
else:
# Write the output file and end the program.
    with open(output_file_path, 'w') as output_file:
        output_file.write(explanation)
        output_file.write("The number of data labels is not the same as the number of clusters.  Clustering accuracy cannot be calculated.")
    output_file.close()
    quit()

# Sum of T(Ck, Lm) values to maximize
max_sum = 0

# Number of data points.
n = len(data_label)

# Matrix to hold T(Ck, Lm)).
t_matrix = numpy.zeros((m, m), dtype=numpy.int)

# Matrix to hold large-valued t_matrix.
t_matrix_large = numpy.zeros((m, m), dtype=numpy.int)

# Generate T(Ck, Lm) and the large version as a copy.
for index in range(0, n):
    t_matrix[clustering_result[index] - 1][data_label[index] - 1] += 1
    t_matrix_large[clustering_result[index] - 1][data_label[index] - 1] += 1

# Fill the large version of T(Ck, Lm) with large values.
for i in range(0, m):
    for j in range(0, m):
        t_matrix_large[i][j] = sys.maxsize - t_matrix_large[i][j]

# Create a munkres object.
munkres_object = Munkres()

# Use the Munkres algorithm to find the location of cells that make the maximum sum.
max_sum_indices = munkres_object.compute(t_matrix_large)

# Save the values of the maximum sum cells.
max_sum_indices_values = []

# Determine maximum sum.
for row, column in max_sum_indices:
    max_sum += t_matrix[row][column]
    max_sum_indices_values.append(t_matrix[row][column])

# Write the output file.
with open(output_file_path, 'w') as output_file:
    output_file.write(explanation)
    output_file.write("\nThe number of data points, n: " + str(n) + "\n")
    output_file.write("\nT(Ck, Lm) as a k by m matrix, where each row is a cluster, and each column is a class label:\n")
    output_file.write(str(t_matrix) + "\n")
    output_file.write("\nT(Ck, Lm) cells and values that make up the maximum sum:\n")
    for i in range(0, m):
        output_file.write(str(max_sum_indices[i]) + " = " + str(max_sum_indices_values[i]) + "\n")

    output_file.write("-------------\n\t" + str(max_sum) + "\n")
    output_file.write("\nAccuracy for clustering then equals this maximum sum divided by n." + "\n")
    output_file.write(str(max_sum) + "/" + str(n) + " = " + str(max_sum / n))

output_file.close()