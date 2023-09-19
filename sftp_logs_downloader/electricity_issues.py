import zipfile
from os import listdir
from os.path import isfile, join
from statistics import mean, mode
from heapq import nsmallest

mypath = "all_logs_electricity_check\\"

zip_files_list = []
#for f in mypath
zip_files_list = [f for f in listdir(mypath) if isfile(join(mypath, f)) and '.zip' in f]
files_with_high_on_off = []

for zip_file in zip_files_list:
    zip_file= "all_logs_electricity_check\\" + zip_file
    try:
        with zipfile.ZipFile(zip_file, mode='r') as zf:
            on_off_values_list = []
            # Print a table of contents in the directory
            for file_name in zf.namelist():
                if "OnOffLog" in file_name:
                    with zf.open(file_name) as myfile:
                        lines = myfile.readlines()
                        for line in lines:
                            float(str(line).split(';')[3])
                            on_off_values_list.append(float(str(line).split(';')[3]))      

                        max_value = max(on_off_values_list)
                        if max_value >= 500:
                            files_with_high_on_off.append(zip_file.split("\\az-")[1])
                            files_with_high_on_off.append(file_name)
                            files_with_high_on_off.append(max_value)
            #print(nsmallest(10, on_off_unique_values_list))
    except zipfile.BadZipFile:
        print('Issue with zipfile.')
print(files_with_high_on_off)
file = open('electricity_issues.txt','w')
for file_item in files_with_high_on_off:
    file.write(str(file_item)+"\n")
file.close()