import os
import glob

folders = ['202603', '202604']
base_dir = r'c:\Users\Luis\Documents\Cowork\Cowork_System\02_Research\Trends'

for folder in folders:
    folder_path = os.path.join(base_dir, folder)
    if not os.path.isdir(folder_path):
        continue
    
    index_path = os.path.join(folder_path, 'indice_general.md')
    md_files = sorted(glob.glob(os.path.join(folder_path, 'resumen_*.md')))
    
    with open(index_path, 'w', encoding='utf-8') as index_file:
        index_file.write(f'# Índice General - {folder}\n\n')
        index_file.write('Este archivo contiene un resumen general de cada uno de los archivos en esta carpeta para facilitar la búsqueda con IA.\n\n')
        for md_file in md_files:
            filename = os.path.basename(md_file)
            
            # Read first paragraph
            first_paragraph = ""
            with open(md_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                for line in lines:
                    line = line.strip()
                    if line:
                        first_paragraph = line
                        break
            
            index_file.write(f'- **[{filename}](./{filename})**:\n  {first_paragraph}\n\n')
            
    print(f'Created {index_path}')
