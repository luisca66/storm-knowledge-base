import os
import re

dir_path = r"h:\Clases\A Little bit of Philosophy"

def clean_text(text):
    if not text: return text
    text = text[0].upper() + text[1:]
    # Be more precise with standalone i
    text = re.sub(r'\b i \b', ' I ', text, flags=re.IGNORECASE)
    text = re.sub(r'\bi\'m\b', 'I\'m', text, flags=re.IGNORECASE)
    text = re.sub(r'\bi\'ve\b', 'I\'ve', text, flags=re.IGNORECASE)
    text = re.sub(r'\bi\'ll\b', 'I\'ll', text, flags=re.IGNORECASE)
    text = re.sub(r'\bi\'d\b', 'I\'d', text, flags=re.IGNORECASE)

    text = text.strip()
    if text and not text.endswith('.'):
        text += '.'
    return text

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
            
    output = []
    current_words = []

    for line in lines:
        line = line.strip()
        if not line: continue
        if re.match(r'^\d+:\d\d(:\d\d)?$', line): continue
        
        # Assume lines starting with an uppercase letter and short length are Section Headers.
        if line[0].isupper() and len(line) < 100:
            if current_words:
                out_p = clean_text(' '.join(current_words))
                output.append(out_p + '\n')
                current_words = []
            output.append(f'## {line}\n')
        else:
            words = line.split()
            current_words.extend(words)
            
            if len(current_words) > 80:
                out_p = clean_text(' '.join(current_words))
                output.append(out_p + '\n')
                current_words = []

    if current_words:
        out_p = clean_text(' '.join(current_words))
        output.append(out_p + '\n')

    md_path = file_path[:-4] + '.md'
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(output))
        
    os.remove(file_path)
    print(f"Converted: {os.path.basename(file_path)} -> {os.path.basename(md_path)}")

count = 0
for root, dirs, files in os.walk(dir_path):
    for file in files:
        if file.endswith('.txt'):
            file_path = os.path.join(root, file)
            process_file(file_path)
            count += 1

print(f"Conversion complete. Processed {count} files.")
