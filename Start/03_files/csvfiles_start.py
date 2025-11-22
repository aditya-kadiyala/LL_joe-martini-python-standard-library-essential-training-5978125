# Reading and writing Comma Separate Values files with Python
import csv


# TODO: list the dialects that are available to use
print(csv.list_dialects())

# TODO: Open a CSV file and read each row of data
def reader_sample():
    with open("StockQuotes.csv") as datafile:
        reader = csv.reader(datafile)
        for row in reader:
            print(row)


# TODO: Use the CSV module Sniffer to see what dialect of CSV this is
def use_sniffer():
    with open("StockQuotes.csv") as datafile:
        dialect = csv.Sniffer().sniff(datafile.read(1024))
        datafile.seek(0)
        has_header = csv.Sniffer().has_header(datafile.read(1024))
        datafile.seek(0)
        print("Headers: ", str(has_header))
        print(dialect.delimiter)
        print(dialect.escapechar)
        print(dialect.quotechar)

# TODO: Write data to a CSV file
def writer_sample():
    with open("SampleData.csv", mode="w") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["Name", "Department", "Location"])
        csvwriter.writerow(["John Doe", "Accounting", "CA"])
        csvwriter.writerow(["Jane Doe", "Engineering", "WA"])
        csvwriter.writerow(["John Due", "HR", "NY"])


# Exercise the samples
# reader_sample()
use_sniffer()
writer_sample()
