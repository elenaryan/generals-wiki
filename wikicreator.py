import subprocess
# Python 3 (i am pretty sure)
# Lenners_ry -- wikicreator script that takes user input and copies 
# valid and properly formatted wiki page to the clipboard
# Dec. 21 2020

# This exists in part to streamline my wiki page creation
# it also exists to standardize my pages' formatting



# Clipboard Function

def write_to_clipboard(output):
	process = subprocess.Popen(
		'pbcopy', env={'LANG':'en_US.UTF-8'}, stdin=subprocess.PIPE)
	process.communicate(output.encode('utf-8'))





# Title/Author  and Basic Info

title = input("Enter title here: ")

author = input("Enter the author here: ")

publication_date = input("Enter the publication date: ")

publication_location = input("Enter city of publication: ")

press = input("Enter press: ")
#print(title+" "+author+" "+publication_date)


# Get the author's first and last names
author = author.split(" ")
author_first = author[0]
author_last  = author[1]

print(author_first)
print(author_last)



# Start building the page
# (Wonder if it makes more sense to just write this out into a text file??)

head = "===="+author_last+", "+title+"====\n"

body = "=== Animating Questions/Argument: === \n\n\\\\"

cont = "\n=== Contribution to the Field: === \n\n\\\\"

source_method = "\n=== Sources and Methodology: === \n\n\\\\"

critique = "\n=== Critiques: === \n\n\\\\"

rel_pages = "\n=== Related Authors and Books: === \n\n\\\\"

bib_entry = "\n"+author_last+", "+author_first +". //"+title+"//. "+publication_location+": "+press+", "+publication_date+"."

full_content = head+body+cont+source_method+critique+rel_pages+bib_entry

write_to_clipboard(full_content)
