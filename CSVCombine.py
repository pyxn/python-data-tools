from os import listdir, read
import pandas


def csv_combine(all_files):

    data_frame_buffer = []

    count_filename = len(all_files)
    count_current = 1
    for filename in all_files:
        new_data_frame = pandas.read_csv(filename, index_col=None, header=0)
        count_row = len(new_data_frame.index)
        count_col = len(new_data_frame.columns)
        print("Merged " + str(count_current) + "/" +
              str(count_filename) + " data frames to buffer (" +
              str(count_row) + " R x " + str(count_col) + " C)")
        data_frame_buffer.append(new_data_frame)
        count_current += 1

    final_frame = pandas.concat(data_frame_buffer, axis=0, ignore_index=True)
    final_count_row = len(final_frame.index)
    final_count_col = len(final_frame.columns)

    print("Creating combined CSV file from merged data frames...")
    final_frame.to_csv('combined.csv', encoding='utf-8', index=False)
    print("Successfully created combined.csv (" +
          str(final_count_row) + " R x " + str(final_count_col) + " C)")


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
        answer = input("Combine all files? Enter yes or no: ")
        if answer == state_true:
            return True
        elif answer == state_false:
            return False
        else:
            print(error)
            print("")


def main():

    print("=================================================")
    print(" Initializing CSV Combine                        ")
    print("=================================================")
    print("")

    list_csv = find_filenames_with_suffix('./', '.csv')
    list_csv.sort()

    print("Detected these CSV Files: (" + str(len(list_csv)) + " total)")
    for filename in list_csv:
        print(filename)

    ready = confirm("Combine all files? Enter yes or no: ",
                    "Please enter yes or no.", 'yes', 'no')

    if ready:
        print("")
        print("Combining files...")
        csv_combine(list_csv)
    else:
        print("Aborting operation...")
        return

    print("=================================================")
    print(" CSVCombine completed execution.                 ")


main()
