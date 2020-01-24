import os
from markdown2 import Markdown
import re
from datetime import datetime as dt
import pandas as pd

markdowner = Markdown()

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

# Create a Pandas dataframe
content_df = pd.DataFrame.from_records(content_table)
content_df.columns = ["file_path", "content"]

# Drop irrelevant rows and reset the index of the table
content_df = content_df.drop(content_df.index[[3,10,13,16]])
content_df = content_df.reset_index()

# Add in the columns for the new model
content_df.insert(loc=2, column = "date", value = "")
content_df.insert(loc=3, column = "place", value = "")
content_df.insert(loc=4, column = "agenda", value = "")
content_df.insert(loc=5, column = "notes", value = "")
content_df.insert(loc=6, column = "resources", value = "")
content_df.insert(loc=7, column = "attended", value = "")

# Create the function to return the table fields for the new site
def format_post(post):
    post_html = markdowner.convert(post)
    
    # Get rid of the stuff we don't want...
    pattern_list = ['<h2>(.*?)</h2>','[\n]', '[=]', '<p>']
    post_html_c = post_html
    for p in pattern_list:
        post_html_c = re.sub(p, "", post_html_c) 
    
    # Split out the info based on </p> and </ul> tags and make a list of strings
    post_html_l = re.split('</p>|</ul>', post_html_c)
    post_html_c = []
    for t in post_html_l:
        post_html_c.append(t.strip())
    
    #Index the bits that we need in the notes and resources...
    notes_i = post_html_c.index("Notes")
    try:
        resources_i = post_html_c.index("Resources")
    except:
        resources_i = ""
    if resources_i != "":
        resources_i_content = post_html_c[resources_i+1]
        notes_i_content = post_html_c[notes_i+1:resources_i]
    else:
        resources_i_content = "<ul>"
        notes_i_content = post_html_c[notes_i+1:]
        
    # Wrap up the notes in <p> tags again and concatenate back to a string...
    notes=""
    for n in notes_i_content:
        if n.startswith("<ul>"):
            notes = notes+"<p>"+n+"</ul></p>"
        elif n.startswith("</li>"):
            notes = notes+"<p><ul><li>"+n+"</ul></p>"
        else:
            notes = notes+"<p>"+n+"</p>"
    # Format the resources to create hyperlinks...
    resources_i_content = resources_i_content.replace('[[', '<a href="')
    resources_i_content = resources_i_content.replace('|', '">')
    resources_i_content = resources_i_content.replace(']]', '</a>')
    resources = resources_i_content+"</ul>"
    
    # Get the info from the indices...
    header = post_html_c[0]
    place = post_html_c[1]
    
    # Extract the date from the list...
    try:
        match = re.search(r'\d{4}-\d{2}-\d{2}', header)
        date = dt.strptime(match.group(), '%Y-%m-%d').date()
    except:
        match = re.search(r'\d{4}-\d{2}', header)
        date = dt.strptime(match.group(), '%Y-%m').date()
    date = date.strftime('%Y-%m-%d')

    # Find the no of attendees (thanks Dave)...
    try:
        attendees = re.search(r"(\d+)\sattendees",notes)
        attended = attendees[1]
        attended = int(attended)
    except:
        attended = 0

    # Return a dictionary of values
    return{"date":date, "place":place, 
           "agenda":"", "notes":notes, 
           "resources":resources, "attended":attended}

# For loop to populate table fields:
for il in range(9):
    ml_post = content_df.loc[il]['content']
    post = format_post(ml_post)
    for k, v in post.items():
        content_df.at[il, k] =  v

# Export pandas table to CSV
content_df.to_csv(r'old_site_data.csv')

# Export to JSON
content_df.to_json(r'old_site_data.json')
