import random

#def read_xyz(filename):
#	frames = []
#	with open(filename,'r') as file:
#		line = file.readline()
#		num_atoms = int(line.strip())
#		energy_line = next(file)
#		frame = [line,energy_line]
#		for _ in range(num_atoms):
#			frame.append(next(file))
#		frames.append(frame)
#	return frames

def read_xyz (file_path):
	frames = []
	atoms = []
	with open(file_path, 'r') as f:
		lines = f.readlines()
		n_frames = 0
		i = 0
		while i < len(lines):
			n_atoms = int(lines[i])
			energy_data = lines[i+1].strip()
			coords = []
			for j in range (i+2, i+2+n_atoms):
				atom_info = lines[j].split()
				coords.append([atom_info[0],float(atom_info[1]),float(atom_info[2]),float(atom_info[3]),float(atom_info[4]),float(atom_info[5]),float(atom_info[6])])
			frames.append({'num_atoms':n_atoms,'energy_data':energy_data,'coords':coords})
			i += n_atoms +2
	return frames
		

#def split_data(frames, train_ratio=0.8):
#		random.shuffle(frames)
#		split_idx = int(len(frames)*train_ratio)
#		return frames[:split_idx],frames[split_idx:]
#
#def save_frames(frames,filename):
#	print_xyz = open (filename,'a')
#	for frame in frames:
#		for line in frames:
#			print (line,file=print_xyz)


#print_log = open('print.log','a')
frames = read_xyz('train.xyz')
random.shuffle(frames)
train_ratio = 0.85
num_train = int(len(frames) * train_ratio)

with open('train.xyz','w') as train_file, open('test.xyz','w') as test_file:
	for i, frame in enumerate(frames):
		if i < num_train:
			file = train_file
		else:
			file = test_file
		file.write(str(frame['num_atoms']) + '\n')
		file.write(frame['energy_data'] + '\n')
		for atom in frame['coords']:
			file.write(f"{atom[0]} {atom[1]} {atom[2]} {atom[3]} {atom[4]} {atom[5]} {atom[6]}\n")

#print (frames,file = print_log)
#print (frames, file = print_log)
#train_frames, val_frames = split_data(all_frames,train_ratio =0.8)
#save_frames(train_frames,"train_set.xyz")
#save_frames(val_frames,"val_set.xyz")
