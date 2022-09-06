import csv

pathCsvClients = "./resources/clientes.csv"


class DataMasking:
    def __init__(self):
        self.CSVDataClients = self.readFileCsv(pathCsvClients)

    def loadProgram(self):
        listNewData = self.processCSV(self.CSVDataClients)
        # print(listNewData)
        self.writeCSV(listNewData)

    def processCSV(self, CSVData):
        CSVDataNew = []
        # The CSVData[0] is the CSV title
        CSVDataNew.append(CSVData[0])

        positionColumnID = CSVData[0].index("ID")
        positionColumnName = CSVData[0].index("Nombre")
        positionColumnEmail = CSVData[0].index("Email")
        positionColumnInvoiced = CSVData[0].index("Facturado")
        positionColumnLocation = CSVData[0].index("Localidad")

        for i in range(1, len(CSVData)):
            CSVDataRow = []
            id = CSVData[i][positionColumnID].strip()
            name = CSVData[i][positionColumnName].strip()
            email = CSVData[i][positionColumnEmail].strip()
            invoiced = CSVData[i][positionColumnInvoiced].strip()
            location = CSVData[i][positionColumnLocation].strip()

            if id != "":
                CSVDataRow.append(id)
            if name != "":
                newName = self.replaceLetters(name)
                CSVDataRow.append(newName)
            if email != "":
                newEmail = self.replaceLetters(email)
                CSVDataRow.append(newEmail)
            if invoiced != "":
                newInvoiced = self.averageInvoiced(CSVData)
                CSVDataRow.append(newInvoiced)
            if location != "":
                CSVDataRow.append(location)

            CSVDataNew.append(CSVDataRow)

        return CSVDataNew

    def averageInvoiced(self, CSVData):
        # average = 25.100,0675
        count = 0.0
        totalInvoiced = 0.0
        positionColumnInvoiced = CSVData[0].index("Facturado")

        for i in range(1, len(CSVData)):
            invoiced = CSVData[i][positionColumnInvoiced].strip()
            if invoiced != "":
                count += 1
                invoiced = float(invoiced)
                totalInvoiced += invoiced
        averageInvoiced = self.average(totalInvoiced, count)
        return averageInvoiced

    def average(self, totalAmount, totalValues):
        return totalAmount / totalValues

    def writeCSV(self, list):
        with open('clientes_masked.csv', 'w', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerows(list)

    def replaceLetters(self, string):
        string = string.lower()
        letters = "abcdefghijklmnopqrstuvwxyz"
        for letter in letters:
            string = string.replace(letter, 'X').lstrip()
        return string

    def readFileCsv(self, pathCSV):
        try:
            with open(pathCSV) as file:
                reader = csv.reader(file)
                if not reader:
                    print("There are NOT DATA in file")
                CSVData = []
                for row in reader:
                    CSVData.append(row)
            return CSVData

        except IOError as e:
            print(e)


if __name__ == "__main__":
    dataMasking = DataMasking()
    dataMasking.loadProgram()
