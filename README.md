# 🎧 Videos Downloader

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Skynisys Downloader

Skynisys Downloader es una aplicación web interactiva desarrollada con Gradio que permite:

Descargar reels de Instagram, Facebook y videos de TikTok.

Descargar audio directamente desde SoundCloud en formato .m4a sin necesidad de FFmpeg.

Mostrar el progreso de la descarga en tiempo real y gestionar errores.

Generar archivos únicos con nombre aleatorio para evitar conflictos de archivos.

La interfaz incluye un diseño limpio con enlaces a redes y un footer personalizado.

🌟 Características

Soporte para múltiples plataformas: Instagram, Facebook, TikTok, SoundCloud

Descarga directa de audio en .m4a desde SoundCloud (sin FFmpeg)

Interfaz web amigable con Gradio Blocks

Manejo de errores y logs de descarga

Barra de progreso en tiempo real

<img width="1905" height="918" alt="Captura de pantalla 2025-10-15 152305" src="https://github.com/user-attachments/assets/dd047dcd-c4b0-4d5b-97b0-28c004fe5f13" />
🛠 Requisitos del sistema

Python >= 3.10

Sistema operativo: Windows, macOS o Linux

FFmpeg (opcional, solo para postprocesos y conversiones de audio/video)

Debe estar instalado y accesible desde la terminal (ffmpeg -version) si se desea usar postprocesos.

Descarga: https://ffmpeg.org/download.html

📦 Instalación de librerías necesarias

Instala las dependencias de Python:

pip install gradio yt-dlp

🚀 Uso

Ejecuta la aplicación:

python app.py


Pega la URL del contenido que quieras descargar.

Selecciona el tipo de descarga:

Instagram Reel

Facebook Reel

TikTok Video

SoundCloud Audio

Haz clic en Descargar y espera a que el progreso llegue al 100%.

El archivo descargado aparecerá en la carpeta downloads con un nombre único.
