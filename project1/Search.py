import csv
def Search():
    inp = "Cold Fire"
        # print(inp)
    with open('books.csv', newline= "") as file:
        readData = [row for row in csv.DictReader(file)]
        for i in range(len(readData)):
            if readData[i]['title'] == inp:
                return readData[i]['isbn']
                   
        return "not found"

print(Search()) 