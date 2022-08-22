import csv

li = [chr(i) for i in range(32, 127)]
li_int = [i for i in range(32, 127)]

with open('unicode_dec_list.csv', 'w') as f:
    writer = csv.writer(f)
    for li_i, li_c in zip(li_int, li):
        writer.writerow([li_i, li_c])