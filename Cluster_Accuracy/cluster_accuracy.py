# Homework 2 program to determine accuracy for clustering.

import numpy

# Paths for the input files.
data_label_path = './data_label.txt'
clustering_result_path = './clustering_result.txt'

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

# Verify that count of labels matches count of clusters.
if len(data_label_set) == len(clustering_result_set):
    label_count = len(data_label_set)
else:
    print("The number of data labels is not the same as the number of clusters.")
    quit()

# Set variables for calculation:
# Accuracy = max (sum{Ck, Lm} T(Ck, Lm)) /n
# Where n = number of data points, Ck denotes kth cluster, Lm is the mth class,
# and T(Ck, Lm) is the number of data points that belong to class m and are
# assigned to cluster k.

# Number of data points.
n = len(data_label)
print(n)

# Matrix to hold T(Ck, Lm)).
t_matrix = numpy.zeros((label_count, label_count), dtype=numpy.int)

# Generate T(Ck, Lm).
for index in range(0, n):
    t_matrix[clustering_result[index] - 1][data_label[index] - 1] += 1

print(t_matrix)