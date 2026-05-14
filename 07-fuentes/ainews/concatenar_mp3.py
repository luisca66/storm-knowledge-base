"""
concatenar_mp3.py
Une los MP3 por partes de una carpeta diaria y genera un solo archivo final.

Pensado para el flujo de Cowork:
  - carpeta raiz: Trends/audio/YYYYMMDD/
  - archivos fuente: reporte_ia_YYYYMMDD_parte_01.mp3, etc.
  - salida final: reporte_ia_YYYYMMDD_completo.mp3

Requisitos:
  - Python 3.8+
  - ffmpeg instalado y disponible en el PATH

Usos tipicos:
  python concatenar_mp3.py --fecha 20260328
  python concatenar_mp3.py --carpeta C:/ruta/a/audio/20260328
  python concatenar_mp3.py --fecha 20260328 --output mi_archivo_final.mp3
"""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

BASE_AUDIO = Path(r"C:\Users\Luis\Documents\Cowork\Cowork_System\02_Research\Trends\audio")
PARTE_RE = re.compile(r"^reporte_ia_(\d{8})_parte_(\d+)\.mp3$", re.IGNORECASE)


def obtener_mp3s(carpeta: Path) -> list[Path]:
    """Devuelve solo los MP3 por partes, ordenados por numero de parte."""
    candidatos: list[tuple[int, Path]] = []

    for archivo in carpeta.iterdir():
        if not archivo.is_file():
            continue

        match = PARTE_RE.match(archivo.name)
        if not match:
            continue

        numero_parte = int(match.group(2))
        candidatos.append((numero_parte, archivo))

    candidatos.sort(key=lambda x: x[0])
    return [ruta for _, ruta in candidatos]


def detectar_fecha_desde_archivos(archivos: list[Path]) -> str | None:
    if not archivos:
        return None
    match = PARTE_RE.match(archivos[0].name)
    return match.group(1) if match else None


def concatenar(archivos: list[Path], salida: Path) -> None:
    """Concatena los archivos MP3 usando ffmpeg sin recodificar."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False, encoding="utf-8") as tmp:
        for ruta in archivos:
            ruta_ffmpeg = ruta.resolve().as_posix().replace("'", "'\\''")
            tmp.write(f"file '{ruta_ffmpeg}'\n")
        lista_path = tmp.name

    try:
        cmd = [
            "ffmpeg",
            "-y",
            "-f",
            "concat",
            "-safe",
            "0",
            "-i",
            lista_path,
            "-c",
            "copy",
            str(salida),
        ]
        print(f"Ejecutando: {' '.join(cmd)}\n")
        resultado = subprocess.run(cmd, capture_output=True, text=True)

        if resultado.returncode != 0:
            print("Error de ffmpeg:")
            print(resultado.stderr)
            sys.exit(1)

        print(f"Archivo creado: {salida}")
        print(f"Se unieron {len(archivos)} archivos.")
    finally:
        try:
            os.unlink(lista_path)
        except FileNotFoundError:
            pass


def resolver_carpeta(fecha: str | None, carpeta: str | None) -> Path:
    if carpeta:
        return Path(carpeta).expanduser().resolve()
    if fecha:
        return (BASE_AUDIO / fecha).resolve()
    return Path.cwd().resolve()


def main() -> None:
    parser = argparse.ArgumentParser(description="Une varios MP3 de un reporte diario en un solo archivo.")
    parser.add_argument(
        "-f", "--fecha",
        help="Fecha del reporte en formato YYYYMMDD. Busca en Trends/audio/YYYYMMDD",
    )
    parser.add_argument(
        "-c", "--carpeta",
        help="Carpeta especifica con los MP3 por partes. Si se usa, tiene prioridad sobre --fecha.",
    )
    parser.add_argument(
        "-o", "--output",
        help="Nombre del archivo de salida. Por defecto usa reporte_ia_YYYYMMDD_completo.mp3",
    )
    args = parser.parse_args()

    carpeta = resolver_carpeta(args.fecha, args.carpeta)
    if not carpeta.is_dir():
        print(f"La carpeta no existe: {carpeta}")
        sys.exit(1)

    archivos = obtener_mp3s(carpeta)
    if not archivos:
        print(f"No se encontraron archivos de partes con patron reporte_ia_YYYYMMDD_parte_XX.mp3 en: {carpeta}")
        sys.exit(1)

    fecha_detectada = args.fecha or detectar_fecha_desde_archivos(archivos)
    output_name = args.output or (
        f"reporte_ia_{fecha_detectada}_completo.mp3" if fecha_detectada else "reporte_ia_completo.mp3"
    )

    if not output_name.lower().endswith(".mp3"):
        output_name += ".mp3"

    salida = carpeta / output_name

    print(f"Carpeta: {carpeta}")
    print(f"Archivos encontrados ({len(archivos)}):\n")
    for i, archivo in enumerate(archivos, 1):
        print(f"  {i}. {archivo.name}")
    print()
    print(f"Salida final: {salida.name}\n")

    concatenar(archivos, salida)


if __name__ == "__main__":
    main()
