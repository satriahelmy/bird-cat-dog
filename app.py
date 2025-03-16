import gradio as gr
from ultralytics import YOLO
# Load model dari Hugging Face
model = YOLO("https://huggingface.co/satriahelmy/klasifikasi-binatang/resolve/main/best.pt")
# Daftar kelas sesuai model
class_names = ['bird','cat','dog']
def classify_image(image):
    results = model(image)  # Jalankan model pada gambar
    probs = results[0].probs  # Ambil hasil probabilitas
    # Prediksi kelas dengan probabilitas tertinggi
    top1_index = probs.top1
    top1_label = class_names[top1_index]
    return f"Predicted Class: {top1_label}"
demo = gr.Interface(
    fn=classify_image,
    inputs=gr.Image(type="pil"),
    outputs="text",
    title="Animal Classify Demo"
)
demo.launch(share=True)