# Homework 2 program to determine accuracy for clustering.

# Paths for the input files.
data_label_path = './data_label.txt'
clustering_result_path = './clustering_result.txt'

# Lists to hold contents of input files.
data_label = []
clustering_result = []

class_labels = set()
cluster_labels = set()

# Read data label file.
try:
    with open(data_label_path, 'r') as data_label_input:
        for current_label in data_label_input:
            data_label.append(int(current_label.split(' ')[0]))
            class_labels.add(int(current_label.split(' ')[0]))
except:
    error_message = 'File + ' + data_label_path + ' not found.'
    exit(error_message)
data_label_input.close()

# Read clustering results file
try:
    with open(clustering_result_path, 'r') as clustering_result_input:
        for current_result in clustering_result_input:
            clustering_result.append(int(current_result.rstrip('\n')))
            cluster_labels.add(int(current_result.rstrip('\n')))
except:
    error_message = 'File + ' + clustering_result_path + ' not found.'
    exit(error_message)
clustering_result_input.close()

print(data_label)
print(clustering_result)
print(sorted(class_labels))
print(sorted(cluster_labels))

# Set variables for calculation:
# Accuracy = max (sum{Ck, Lm} T(Ck, Lm)) /n
# Where n = number of data points, Ck denotes kth cluster, Lm is the mth class,
# and T(Ck, Lm) is the number of data points that belong to class m and are
# assigned to cluster k.

n = len(data_label)
print(n)