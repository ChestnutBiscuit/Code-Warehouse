import os

searce_dir = 'home/deepmd-date/dpgen/Nafion/data/INCAR/AIMD/353KAIMD/14C12wnpt'

for subdir, dirs, files in os.walk(searce_dir):
    force_path = os.path.join(subdir,'force.raw')
    if os.path.exists(force_path):
        with open(force_path,'r') as file:
            lines = file.readlines()
            target_lines = [line for line in lines if 'e+01' in line]
        print (f"Found {len(target_lines)} exceed 10")
        print (force_path)
        line_numbers = [i for i, line in enumerate(lines) if 'e+01' in line]
        print (line_numbers)
    
    for filename in ['energy.raw', 'coord.raw', 'box.raw', 'virial.raw','force.raw']:
        file_path = os.path.join(subdir, filename)
        if os.path.exists(file_path):
            with open(file_path,'r') as file:
                lines = file.readlines()
            with open(file_path,'w') as file:
                for i, line in enumerate(lines):
                    if i not in line_numbers:
                        file.write(line)
                    if i in line_numbers:
                        print (i)
