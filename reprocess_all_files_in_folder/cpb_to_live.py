import os

for filename in os.listdir(os.getcwd()):
	if os.path.isfile(os.path.join(os.getcwd(), filename)) and '.py' not in filename:
		
		with open(filename, 'r') as f:
			lines = f.readlines()
			live_lines_list = []
			for line in lines:
				if line[26] == '1':	
					live_lines_list.append(line)
				else:
					pass

		#folder_name = file_name[:-4]
		folder_name = "files_cleaned"
		folder_path = os.path.join(os.getcwd(), folder_name)
		print(folder_name)
		#print(live_lines_list)
		if not os.path.exists(folder_path):
		        os.makedirs(folder_path)


		new_file_path = os.path.join(folder_path, filename)
		print(new_file_path)
		with open(new_file_path, 'w') as file:
		    # Convert the list to a single string using join
		    for item in live_lines_list:
		        file.write(item)