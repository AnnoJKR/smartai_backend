from src.engines.utils import convert_pdf_to_image, preprocess_image_for_ocr
import os

# Select one of your real forms to test
# Ensure 'test_form.pdf' exists in data/raw_pdfs/ or change the name below
pdf_path = os.path.join("data", "raw_pdfs", "Debit-Card-Issuance-V1.pdf") 

print(f"Testing pipeline on: {pdf_path}")

# 1. Test Conversion (PDF -> Image)
raw_img = convert_pdf_to_image(pdf_path)
if raw_img:
    print("✅ Step 1: PDF converted to Image.")
    
    # 2. Test Enhancement (Image -> Clean B&W)
    clean_img = preprocess_image_for_ocr(raw_img)
    print("✅ Step 2: Image cleaned and binarized.")
    
    # Save output to verify
    clean_img.save("debug_clean_view.png")
    print("SUCCESS: Check 'debug_clean_view.png' in your folder. It should look like a sharp photocopy.")
else:
    print("❌ Error: Could not find the PDF. Check the filename in data/raw_pdfs/")