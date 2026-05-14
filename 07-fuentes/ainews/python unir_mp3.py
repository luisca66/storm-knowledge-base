import os
from pydub import AudioSegment

def unir_archivos_mp3(lista_archivos, nombre_salida="resultado.mp3"):
    """
    Une varios archivos MP3 en uno solo en el orden proporcionado en la lista.
    """
    if not lista_archivos:
        print("Error: La lista de archivos está vacía.")
        return

    # Verificar que el primer archivo exista antes de empezar
    if not os.path.exists(lista_archivos[0]):
        print(f"Error: El archivo inicial {lista_archivos[0]} no existe.")
        return

    try:
        print(f"Cargando pista base: {lista_archivos[0]}")
        # Cargar el primer archivo de audio
        audio_combinado = AudioSegment.from_mp3(lista_archivos[0])
    except Exception as e:
        print(f"Error al cargar el archivo {lista_archivos[0]}: {e}")
        return

    # Iterar sobre los archivos restantes en el orden dado
    for archivo in lista_archivos[1:]:
        if not os.path.exists(archivo):
            print(f"Advertencia: El archivo {archivo} no fue encontrado. Se omitirá.")
            continue
            
        try:
            print(f"Añadiendo pista: {archivo}")
            siguiente_audio = AudioSegment.from_mp3(archivo)
            # La concatenación se hace simplemente usando el operador de suma
            audio_combinado += siguiente_audio
        except Exception as e:
            print(f"Error al procesar el archivo {archivo}: {e}")

    # Exportar el resultado final
    try:
        print(f"Exportando el archivo final como: {nombre_salida}...")
        # El bitrate y otros parámetros se pueden ajustar aquí si es necesario
        audio_combinado.export(nombre_salida, format="mp3")
        print("Proceso completado.")
    except Exception as e:
        print(f"Error al exportar el archivo: {e}")

# Bloque de ejecución principal
if __name__ == "__main__":
    # Define aquí la lista de archivos en el orden exacto que deseas
    # Puedes usar rutas absolutas si los archivos no están en la misma carpeta que el script
    archivos_a_unir = [
        "audio_1.mp3",
        "audio_2.mp3",
        "audio_3.mp3"
    ]
    
    archivo_final = "mezcla_completa.mp3"
    
    unir_archivos_mp3(archivos_a_unir, archivo_final)