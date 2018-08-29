import csv
import re

with open(r'c:/Users/Phanakhone/Desktop/lao_converter/final.txt', 'r', encoding='utf-8') as f:
    data = f.read().splitlines()


with open('c:/Users/Phanakhone/Desktop/lao_converter/final.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = re.sub('[\ufeff\ufeff]', '', data[0]).split('\t')
    print(fieldnames)

    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for d in data[1:]:
        s = d.replace('\ufeff', '')
        s = re.sub('[\ufeff\uffff]', '', d)
        print(d)

        s = dict(zip(fieldnames, d.split('\t')))

        print(s)
        writer.writerow(s)
