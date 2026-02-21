from src.engines.utils import convert_pdf_to_image, preprocess_image_for_ocr
from src.engines.ocr import OCREngine
import os
import time

# Setup
pdf_path = os.path.join("data", "raw_pdfs", "Debit-Card-Issuance-V1.pdf")

print("--- STARTING PIPELINE TEST ---")

# Step 1: Initialize Engine
start_time = time.time()
engine = OCREngine()
print(f"✅ Engine Loaded in {time.time() - start_time:.2f} seconds")

# Step 2: Vision Processing
print("running vision pipeline...")
raw_img = convert_pdf_to_image(pdf_path)
clean_img = preprocess_image_for_ocr(raw_img)

# Step 3: Run OCR
print("running OCR scan (this might take 10-20 seconds on CPU)...")
results = engine.extract_layout(clean_img)

# Step 4: Validate
if results:
    print(f"\n✅ OCR SUCCESS! Detected {len(results)} text elements.")
    print("--- First 5 Detected Fields ---")
    for i in range(min(5, len(results))):
        line = results[i]
        # PaddleOCR returns: [ [[x,y]...], ("Text", Score) ]
        text = line[1][0]
        score = line[1][1]
        print(f"  [{i+1}] Text: '{text}' (Confidence: {score:.2f})")