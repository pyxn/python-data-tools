from os import listdir
import csv
import pandas
import xlrd


def convert_filelist_to_csv(xlsx_filename_list):
    print("Converting")

    count_of_files = len(xlsx_filename_list)
    count_of_converted = 0
    for filename in xlsx_filename_list:
        dimensions = csv_from_excel(filename, 'results', filename)
        count_of_converted += 1
        print("Converted " + str(count_of_converted) +
              "/" + str(count_of_files) + " files... (" + str(dimensions[0]) + " R x " + str(dimensions[1]) + " C)")


def csv_from_excel(filename_input, filename_input_sheet, filename_output):
    data_xls = pandas.read_excel(
        filename_input, filename_input_sheet, dtype=str, index_col=None)
    data_row_count = len(data_xls.index)
    data_column_count = len(data_xls.columns)
    new_filename = filename_input + '.csv'
    data_xls.to_csv(new_filename, encoding='utf-8', index=False)

    return data_row_count, data_column_count


def find_filenames_with_suffix(path_to_dir, suffix):

    filenames = listdir(path_to_dir)
    filenames_with_suffix_only = []

    for filename in filenames:
        if filename.endswith(suffix):
            filenames_with_suffix_only.append(filename)

    return filenames_with_suffix_only


def main():

    print("=================================================")
    print(" Initializing CSV Convert                        ")
    print("=================================================")
    print("")

    list_xlsx = find_filenames_with_suffix('./', '.xlsx')
    list_xlsx.sort()

    print("Detected these XLSX Files " + "(" + str(len(list_xlsx)) + " total):")
    for filename in list_xlsx:
        print(filename)

    answer = ''
    while answer != 'yes' or answer != 'no':
        answer = input("Combine convert all to CSV? Enter yes or no: ")
        if answer == "yes":
            print("")
            print("Combining files...")
            convert_filelist_to_csv(list_xlsx)
            break
        elif answer == "no":
            print("Aborting operation...")
            return
        else:
            print("Please enter yes or no.")
            print("")

    print("=================================================")
    print(" CSVCombine completed execution.                 ")


main()
