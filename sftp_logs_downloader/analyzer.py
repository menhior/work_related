import zipfile
from os import listdir
from os.path import isfile, join
from statistics import mean, mode
from heapq import nsmallest

reg_key = input("Please enter registration key: ")
separator = input('Please enter value for separator: ')

mypath = "downloaded_logs\\" + reg_key + '\\'

zip_files_list = []
#for f in mypath
zip_files_list = [f for f in listdir(mypath) if isfile(join(mypath, f)) and '.zip' in f]

for zip_file in zip_files_list:
    zip_file= "downloaded_logs\\" + reg_key + '\\' + zip_file
    try:
        with zipfile.ZipFile(zip_file, mode='r') as zf:
            on_off_values_list = []
            # Print a table of contents in the directory
            for file_name in zf.namelist():
                if "OnOffLog" in file_name:
                    with zf.open(file_name) as myfile:
                        lines = myfile.readlines()
                        for line in lines:
                            on_off_values_list.append(float(str(line).split(';')[3]))      
            a = 0
            b = 0
            c = 0
            d = 0
            largest_cut_off = 0
            split_range = len(on_off_values_list)//int(separator)
            for i in range(split_range):
                a = int(separator) * i
                b = int(separator) * (i + 1)
                list_to_check = on_off_values_list[a:b]
                difference = max(list_to_check) - min(list_to_check)
                if difference > largest_cut_off:
                    largest_cut_off = difference
                    c = a
                    d = b
            if largest_cut_off > 3:
                print('Mean value of file:', str(mean(on_off_values_list)))
                print('Mode value of file:', str(mode(on_off_values_list)))
                print('Largest cutoff range:', largest_cut_off)
                print(on_off_values_list[c:d])

                on_off_unique_values_list = list(set(on_off_values_list))
                on_off_unique_values_list.sort()
                on_off_unique_values_list.append(zip_file)
            
            #print(nsmallest(10, on_off_unique_values_list))
    except zipfile.BadZipFile:
        print('Issue with zipfile.')
