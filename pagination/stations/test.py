import csv
st_list = []
with open('data-398-2018-08-30.csv', encoding = "UTF-8") as f:
    reader = csv.DictReader(f)
    st_list.append(list(reader))
    print(st_list)

    