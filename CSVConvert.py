from os import listdir
import csv
import pandas
import xlrd


def convert_filelist_to_csv(xlsx_sheet_name, xlsx_filename_list):
    print("Converting")

    count_of_files = len(xlsx_filename_list)
    count_of_converted = 0
    for filename in xlsx_filename_list:
        dimensions = csv_from_excel(filename, xlsx_sheet_name, filename)
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


def confirm(message, error, state_true, state_false) -> bool:
    answer = ''
    while answer != state_true or answer != state_false:
        print("")
        answer = input(message)
        if answer == state_true:
            return True
        elif answer == state_false:
            return False
        else:
            print(error)
            print("")


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

    sheet = input("Enter the (common) sheet name: ")

    print("")

    ready = confirm("Convert all to CSV? Enter yes or no: ",
                    "Please enter yes or no.", 'yes', 'no')

    if ready:
        print("")
        print("Converting files...")
        convert_filelist_to_csv(sheet, list_xlsx)
    else:
        print("Aborting operation...")
        return

    print("=================================================")
    print(" CSVConvert completed execution.                 ")


main()
