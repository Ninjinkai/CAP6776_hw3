# Homework 2 program to determine accuracy for clustering.

import numpy

# Paths for the input files.
data_label_path = './data_label.txt'
clustering_result_path = './clustering_result.txt'

# Lists to hold contents of input files.
data_label = []
clustering_result = []

# Matrix to hold T(Ck, Lm)).
t_matrix = numpy.zeros((10, 10), dtype=numpy.int)

# Read data label file.
try:
    with open(data_label_path, 'r') as data_label_input:
        for current_label in data_label_input:
            data_label.append(int(current_label.split(' ')[0]))
except:
    error_message = 'File + ' + data_label_path + ' not found.'
    exit(error_message)
data_label_input.close()

# Read clustering results file
try:
    with open(clustering_result_path, 'r') as clustering_result_input:
        for current_result in clustering_result_input:
            clustering_result.append(int(current_result.rstrip('\n')))
except:
    error_message = 'File + ' + clustering_result_path + ' not found.'
    exit(error_message)
clustering_result_input.close()

# Set variables for calculation:
# Accuracy = max (sum{Ck, Lm} T(Ck, Lm)) /n
# Where n = number of data points, Ck denotes kth cluster, Lm is the mth class,
# and T(Ck, Lm) is the number of data points that belong to class m and are
# assigned to cluster k.

n = len(data_label)
print(n)

for index in range(0, n):
    t_matrix[clustering_result[index] - 1][data_label[index] - 1] += 1

print(t_matrix)

maximum = 0
diag_sum = 0

for i in range(0, 10):
    for j in range(0, 10):
        diag_sum += t_matrix[j][(j + i) % 10]
    print(diag_sum)
    if diag_sum > maximum:
        maximum = diag_sum
    diag_sum = 0
print(maximum)
print(maximum/n)