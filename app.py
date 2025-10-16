import gradio as gr
import yt_dlp
import os
import uuid

def download_media(url, option, progress=gr.Progress()):
    output_dir = "downloads"
    os.makedirs(output_dir, exist_ok=True)
    unique_id = uuid.uuid4().hex
    filename_base = os.path.join(output_dir, f"{unique_id}")

    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
        'progress_hooks': [],
        'outtmpl': filename_base + ".%(ext)s",
        'noplaylist': True,
    }

    # Hook de progreso
    def hook(d):
        if d['status'] == 'downloading':
            try:
                downloaded = d.get('downloaded_bytes', 0)
                total = d.get('total_bytes', 1)
                progress(downloaded / total, desc=f"Descargando... {downloaded / total * 100:.1f}%")
            except Exception:
                pass
        elif d['status'] == 'finished':
            progress(1.0, desc="Procesando archivo...")

    ydl_opts['progress_hooks'] = [hook]

    # Configuración según tipo
    if option in ["Instagram Reel", "Facebook Reel"]:
        ydl_opts['format'] = 'best'  # video completo
    elif option == "YouTube Audio":
        ydl_opts['format'] = 'bestaudio/best'  # solo audio

    # Descarga principal
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        # Buscar archivo descargado
        if option in ["Instagram Reel", "Facebook Reel"]:
            for ext in ['mp4', 'mkv', 'webm']:
                candidate = f"{filename_base}.{ext}"
                if os.path.exists(candidate):
                    progress(1.0, desc="✅ Descarga completa")
                    return candidate, f"✅ ¡Descarga completada correctamente ({ext})!"
        else:  # YouTube Audio
            for ext in ['webm', 'm4a', 'opus']:
                candidate = f"{filename_base}.{ext}"
                if os.path.exists(candidate):
                    progress(1.0, desc="✅ Descarga completa")
                    return candidate, f"✅ ¡Audio descargado correctamente ({ext})!"

        return None, "⚠️ No se encontró el archivo descargado."

    except Exception as e:
        error_path = os.path.join(output_dir, f"{unique_id}_error.txt")
        with open(error_path, "w", encoding="utf-8") as f:
            f.write(f"Error al descargar:\n{str(e)}")
        return error_path, f"❌ Error durante la descarga:\n{str(e)}"


# Footer personalizado
custom_html = """
<style>
.footer-links { text-align: center; margin-top: 210px; margin-bottom: 10px; font-size: 15px; }
.footer-links a { color: #00ffff; text-decoration: none; }
.footer-links a:hover { text-decoration: underline; }
</style>
<div class="footer-links">
    <a href="https://weblink-f7e51.web.app/">weblink</a>
     • 
    <a href="https://github.com/Gnirvin">Github</a>
     • 
    <a href="https://gradio.app">Gradio</a>
     • 
    <a href="https://www.instagram.com/creative.ia_art/">Instagram</a>
     • 
    ⚡ <span class="version-tag">Skynisys Downloader v2.0.0</span>
</div>
"""

# Interfaz principal
with gr.Blocks(title="Skynisys Downloader") as demo:
    gr.Markdown("## ⚡ Skynisys Downloader")
    gr.Markdown("Descarga **Instagram Reels, Facebook Reels** o **solo el audio de YouTube**.")

    with gr.Row():
        url = gr.Textbox(label="🔗 URL", placeholder="Pega aquí el enlace...")
        tipo = gr.Radio(
            choices=["Instagram Reel", "Facebook Reel", "YouTube Audio"],
            label="📦 Tipo de descarga"
        )

    archivo = gr.File(label="📁 Archivo descargado")
    estado = gr.Textbox(label="📜 Estado de la descarga")

    btn = gr.Button("⬇️ Descargar")
    btn.click(download_media, [url, tipo], [archivo, estado])

    gr.HTML(custom_html)

demo.launch()


demo.launch()

