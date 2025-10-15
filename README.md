# 🎧 Skynisys Downloader

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Skynisys Downloader es una **aplicación web interactiva** desarrollada con **Gradio** que permite:  

- Descargar **reels de Instagram** y **Facebook**.  
- Extraer **audio MP3** de videos de **YouTube**.  
- Mostrar el progreso de la descarga en tiempo real y gestionar errores.  
- Generar archivos únicos para evitar conflictos.  

La interfaz incluye un diseño limpio con enlaces a redes sociales y un footer personalizado.  

---

## 🌟 Características

- Soporte para múltiples plataformas: **YouTube, Instagram, Facebook**  
- Descarga directa de **audio en MP3** desde YouTube  
- Interfaz web amigable con **Gradio Blocks**  
- Manejo de errores y logs de descarga  
- Barra de progreso en tiempo real  
- Footer con enlaces rápidos y botón para recargar la UI  

---

## 🛠 Requisitos

- **Python** >= 3.10  
- **Sistema operativo:** Windows, macOS o Linux  
- **FFmpeg** (para convertir a MP3 en descargas de YouTube)  
  - Asegúrate de que `ffmpeg` esté en tu variable de entorno `PATH`.  

---

## 📦 Instalación

1. Clonar el repositorio:  
```bash
git clone https://github.com/tu-usuario/skynisys-downloader.git
cd skynisys-downloader
