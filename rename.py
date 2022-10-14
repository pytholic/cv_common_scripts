import os

path = os.getcwd()

for folder in os.listdir(path):
	folder_path = os.path.join(path, folder)
	idx = 1
	for img in os.listdir(folder_path):
		os.rename(img, f'{idx}.jpg')
		idx+=1
	
