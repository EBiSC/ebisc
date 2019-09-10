import csv


imbt = None
ebisc = None

with open("ibmt_inventory.csv", 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    ibmt = set(map(lambda row: row[0].strip(), reader))


with open("ebisc_cell_line_ids.csv", 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    ebisc = set(map(lambda row: row[0].strip(), reader))


not_in_ebisc = set()
not_in_ibmt = set()

for name in ibmt:
    if name not in ebisc:
        not_in_ebisc.add(name)

for name in ebisc:
    if name not in ibmt:
        not_in_ibmt.add(name)


with open("Output2.txt", "w") as text_file:
    text_file.write('lines missing in ebisc batch list:')
    text_file.write('\n')
    for name in not_in_ebisc:
        text_file.write(name)
        text_file.write('\n')
    text_file.write('------')
    text_file.write('\n')
    text_file.write(str(len(not_in_ebisc)))
    text_file.write('\n')

    text_file.write('\n\n')
    text_file.write('lines missing in ibmt inventory:')
    text_file.write('\n')
    for name in not_in_ibmt:
        text_file.write(name)
        text_file.write('\n')
    text_file.write('------')
    text_file.write('\n')
    text_file.write(str(len(not_in_ibmt)))
    text_file.write('\n')


    text_file.write('\n\n')
    text_file.write('\n\n')
    text_file.write(str(len(ibmt)))
    text_file.write('\n')
    text_file.write(str(len(ebisc)))
    text_file.write('\n')
