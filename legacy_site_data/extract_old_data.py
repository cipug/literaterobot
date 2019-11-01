import os
import csv

folder = './pages/'

fn_list = []
dn_list = []
d_revisions = []

# Obtain full list of directories from the old site
for (dirpath, dirnames, filenames) in os.walk(folder):
    for d in dirnames:
        dn = os.path.join(dirpath, d)
        dn_list.append(dn)
dn_list.sort()

# If 'revisions' is in a directory, get the last revision file with dir path
for d in dn_list:
    if "revisions" in d:
        temp_list = []
        for (dirpath, dirnames, filenames) in os.walk(d):
            for f in filenames:
                fn = os.path.join(dirpath, f)
                temp_list.append(fn)
        temp_list.sort()
        fn_list.append(temp_list[-1])
fn_list.sort()


# Create a table with all the relevant data from the last revision file
content_table = []
for fn in fn_list:
    (dirname, filename) = os.path.split(fn)
    open_file = open(fn, 'r')
    file_text = open_file.read()
    table_row = [dirname, file_text]
    content_table.append(table_row)

# Convert table to CSV

with open("output.csv", "w", newline="") as output:
    writer = csv.writer(output)
    writer.writerows(content_table)

# Note if needed: 
# os.path.dirname(os.path.dirname(fn))  # directory of directory of file
