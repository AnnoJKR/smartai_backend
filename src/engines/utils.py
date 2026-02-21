import fitz  # PyMuPDF
from PIL import Image, ImageOps, ImageEnhance
import io

def convert_pdf_to_image(pdf_path, dpi=300):
    try:
        doc = fitz.open(pdf_path)
        page = doc.load_page(0)
        pix = page.get_pixmap(dpi=dpi) 
        img_data = pix.tobytes("png")
        image = Image.open(io.BytesIO(img_data))
        return image
    except Exception as e:
        print(f"Error converting PDF: {e}")
        return None

def preprocess_image_for_ocr(image):
    gray_image = ImageOps.grayscale(image)
    enhancer = ImageEnhance.Contrast(gray_image)
    enhanced_image = enhancer.enhance(2.0)
    binary_image = enhanced_image.point(lambda x: 0 if x < 128 else 255, '1')
    return binary_image.convert("RGB")