# 🎧 Videos Downloader

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**Skynisys Downloader** es una aplicación web interactiva desarrollada con **Gradio** que permite:  

- Descargar **reels de Instagram** y **Facebook**.  
- Extraer **audio MP3** de videos de **YouTube**.  
- Mostrar el progreso de la descarga en tiempo real y gestionar errores.  
- Generar archivos únicos con nombre aleatorio para evitar conflictos de archivos.  

La interfaz incluye un diseño limpio con enlaces a redes y un footer personalizado.  

---

## 🌟 Características

- Soporte para múltiples plataformas: **YouTube, Instagram, Facebook**  
- Descarga directa de **audio en MP3** desde YouTube  
- Interfaz web amigable con **Gradio Blocks**  
- Manejo de errores y logs de descarga  
- Barra de progreso en tiempo real  

---
<img width="1905" height="918" alt="Captura de pantalla 2025-10-15 152305" src="https://github.com/user-attachments/assets/dd047dcd-c4b0-4d5b-97b0-28c004fe5f13" />

## 🛠 Requisitos del sistema

- **Python** >= 3.10  
- **Sistema operativo:** Windows, macOS o Linux  
- **FFmpeg** (obligatorio para convertir a MP3 y procesar videos)  
  - Debe estar instalado y accesible desde la terminal (`ffmpeg -version`)  
  - Descarga: [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)  

---

## 📦 Instalación de librerías necesarias

Instala las dependencias de Python:

```bash
pip install gradio yt-dlp



