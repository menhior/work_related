import os
import time


for i in range(5):
	for i in range(10):
		os.startfile("file_1.docx", "print")
		time.sleep(2)
		os.startfile("file_2.docx", "print")
		time.sleep(2)
		os.startfile("file_3.docx", "print")
		time.sleep(10)