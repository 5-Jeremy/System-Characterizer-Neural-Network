import numpy as np

def summarize_data(dataset):
    # Count the number of systems with overshoot, undershoot, and neither
    overshoot_cnt = undershoot_cnt = neither_cnt = 0
    num_entries = dataset.shape[0]
    for i in range(num_entries):
        if dataset['Overshoot'][i] > 1e-10:
            overshoot_cnt = overshoot_cnt + 1
        elif dataset['Undershoot'][i] > 1e-10:
            undershoot_cnt = undershoot_cnt + 1
        else:
            neither_cnt = neither_cnt + 1
    print("Models with overshoot: " + str(overshoot_cnt) + "/" + str((overshoot_cnt/num_entries)*100) + "%")
    print("Models with undershoot: " + str(undershoot_cnt) + "/" + str((undershoot_cnt/num_entries)*100) + "%")
    print("Models with neither: " + str(neither_cnt) + "/" + str((neither_cnt/num_entries)*100) + "%")

def get_encoded_labels_overshoot_undershoot_classification(dataset):
    labels = np.empty((dataset.shape[0],3))
    for i in range(dataset.shape[0]):
        if dataset['Overshoot'][i] > 1e-5:
            labels[i,:] = [0, 1, 0]
        elif dataset['Undershoot'][i] > 1e-5:
            labels[i,:] = [0, 0, 1]
        else:
            labels[i,:] = [1, 0, 0]
    return labels