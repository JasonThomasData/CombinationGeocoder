import csv

class FileHandler:
    def read_file(self, file_name):
        with open(file_name, 'r') as csv_file_read:
            csv_reader = csv.reader(csv_file_read, delimiter = ',')
            rows_all = []
            for row in csv_reader:
                rows_all.append(row)
            return rows_all

    def save_file(self, file_name, csv_rows, row_matrix):
        with open(file_name, 'w') as csv_file_write:
            csv_writer = csv.writer(csv_file_write, delimiter = ',')
            existing_row_array = []
            for row in csv_rows:
                print row
                existing_row_array.append(row)
            for l in range(0, len(row_matrix)): #When I replaced csv_rows with row_matrix, it stopped saving lines that weren't in this file. I should abstract this out so this is access for each line, not for all lines and then saved. I should replace one line per save.
                print row_matrix[l]
                print l
                csv_writer.writerow(existing_row_array[l] + row_matrix[l])

#The thing that processes the data for saving should be in a seperate function.
#Perhaps a seperate class and module.
#Currently, rather than saving, it overwrites the entire file with the results. Find a way to add a result to each line.
#A cleaner way to do this would be to save one line at a time.
#This has the added benefit of never losing your progress if it explodes.