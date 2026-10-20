# Tomato-AI · Web divulgativa

Página para la Semana de la Ciencia y la Tecnología de Murcia sobre el proyecto Tomato-AI (UPCT, Reto TomatoLED-NDVI).

- `index.html`: web completa (sin dependencias, salvo las fuentes de Google)
- `assets/`: imágenes
- `make_qr.py`: genera el QR de la web

## Publicar con GitHub Pages
1. Crea un repositorio `tomato-ai` en GitHub y sube estos archivos.
2. Settings → Pages → Branch `main` / carpeta `/ (root)` → Save.
3. La web quedará en `https://TU_USUARIO.github.io/tomato-ai/`.
4. `pip install qrcode[pil]` y `python make_qr.py https://TU_USUARIO.github.io/tomato-ai/`
