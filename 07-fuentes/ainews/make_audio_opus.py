#!/usr/bin/env python3
"""Generate Cowork audio for resumen_20260520.md."""
import os, math, re, subprocess, sys

SOURCE = r"C:\Users\Luis\Documents\storm-knowledge-base\07-fuentes\ainews\202605\resumen_20260520.md"
AUDIO_DIR = r"C:\Users\Luis\Documents\storm-knowledge-base\07-fuentes\ainews\audio\20260520"
EDGE_TTS = r"C:\Users\Luis\AppData\Roaming\npm\edge-tts.CMD"
EDGE_VOICE = "es-MX-DaliaNeural"
CHUNK_SIZE = 6800

os.makedirs(AUDIO_DIR, exist_ok=True)

# Read and clean the markdown
with open(SOURCE, "r", encoding="utf-8") as f:
    text = f.read()

# Clean markdown artifacts
text = re.sub(r'\*{1,2}(.*?)\*{1,2}', r'\1', text)
text = re.sub(r'_{1,2}(.*?)_{1,2}', r'\1', text)
text = re.sub(r'^#+\s*', '', text, flags=re.MULTILINE)
text = re.sub(r'^[\*\-]\s+', '', text, flags=re.MULTILINE)
text = re.sub(r'\n{3,}', '\n\n', text)
text = text.strip()

print(f"Texto limpio: {len(text)} caracteres")

# Split into chunks at sentence boundaries
chunks = []
start = 0
while start < len(text):
    end = min(start + CHUNK_SIZE, len(text))
    
    if end < len(text):
        # Search backwards from end for a sentence boundary
        search_start = max(end - 500, start)
        search_area = text[search_start:end + 100]
        
        break_at = -1
        # Try period + space + capital letter (sentence end)
        for i in range(len(search_area) - 2, -1, -1):
            if (search_area[i] == '.' and i + 2 < len(search_area) 
                and search_area[i+1] == ' ' 
                and search_area[i+2].isupper()):
                break_at = search_start + i + 1
                break
        
        # Try paragraph break
        if break_at < 0:
            para = text.find('\n\n', search_start)
            if para > search_start and para <= end + 200:
                break_at = para
        
        if break_at > start:
            end = break_at
    
    chunk = text[start:end].strip()
    if chunk:
        chunks.append(chunk)
    start = end

print(f"Total chunks: {len(chunks)}")
for i, c in enumerate(chunks):
    print(f"  Chunk {i+1}: {len(c)} chars")

# Synthesize each chunk
part_files = []
for i, chunk in enumerate(chunks):
    part_num = i + 1
    txt_file = os.path.join(AUDIO_DIR, f"parte_{part_num:02d}.txt")
    mp3_file = os.path.join(AUDIO_DIR, f"parte_{part_num:02d}.mp3")
    
    with open(txt_file, "w", encoding="utf-8") as f:
        f.write(chunk)
    
    print(f"\n--- Synthesizing part {part_num}/{len(chunks)} ({len(chunk)} chars) ---")
    result = subprocess.run(
        [EDGE_TTS, "synthesize", "-v", EDGE_VOICE, "-f", txt_file, "--write-media", mp3_file],
        capture_output=True, text=True, timeout=120
    )
    print(result.stdout)
    if result.stderr:
        print("STDERR:", result.stderr[:500])
    
    if os.path.exists(mp3_file):
        size = os.path.getsize(mp3_file)
        print(f"  MP3 creado: {size} bytes")
        part_files.append(mp3_file)
    else:
        print(f"  ERROR: MP3 no creado para parte {part_num}")
        # Try inline fallback
        print("  Intentando fallback inline...")
        result = subprocess.run(
            [EDGE_TTS, "synthesize", "-v", EDGE_VOICE, "-t", chunk[:3000], "--write-media", mp3_file],
            capture_output=True, text=True, timeout=120
        )
        if os.path.exists(mp3_file):
            size = os.path.getsize(mp3_file)
            print(f"  MP3 creado (fallback): {size} bytes")
            part_files.append(mp3_file)

if len(part_files) == 0:
    print("ERROR: No se pudo generar ningún MP3")
    sys.exit(1)

# Concatenate all parts
concat_list = os.path.join(AUDIO_DIR, "concat_list.txt")
with open(concat_list, "w") as f:
    for pf in part_files:
        f.write(f"file '{pf}'\n")

final_mp3 = os.path.join(AUDIO_DIR, "reporte_ia_20260520_completo.mp3")
ffmpeg = r"C:\ffmpeg\bin\ffmpeg.exe"

print(f"\n--- Concatenating {len(part_files)} parts ---")
result = subprocess.run(
    [ffmpeg, "-f", "concat", "-safe", "0", "-i", concat_list,
     "-c", "copy", "-y", final_mp3],
    capture_output=True, text=True, timeout=120
)
print(result.stdout[-500:] if result.stdout else "")
if result.stderr:
    print(result.stderr[-500:])

if os.path.exists(final_mp3):
    size_mb = os.path.getsize(final_mp3) / (1024*1024)
    print(f"\n✅ AUDIO COMPLETO: {final_mp3}")
    print(f"   Tamaño: {size_mb:.1f} MB")
    
    # Get duration
    duration = subprocess.run(
        [ffmpeg, "-i", final_mp3, "-f", "null", "-"],
        capture_output=True, text=True, timeout=30
    )
    dur_match = re.search(r'Duration: (\d+:\d+:\d+\.\d+)', duration.stderr)
    if dur_match:
        print(f"   Duración: {dur_match.group(1)}")
else:
    print("ERROR: No se pudo generar el archivo final")
