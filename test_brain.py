from src.engines.llm import LLMEngine

# This is the actual text your OCR just found (I copied it from your logs)
test_data = """
IDFC FIRST Bank
DEBIT CARD ISSUANCE/RE-ISSUANCE FORM
Please fill in Black Ink and in CAPITAL LETTERS
Date
Name of the Applicant
Account Number
"""

print("--- TESTING BRAIN ---")
engine = LLMEngine()

# Test 1: Identify the form
print("Thinking...")
analysis = engine.analyze_form(test_data)
print("\n[AI Analysis Result]:")
print(analysis)

# Test 2: Ask for help on a specific field
print("\n[Testing Field Guidance]:")
guidance = engine.ask_field_guidance("Account Number", test_data)
print(f"User asked: 'What is Account Number?'")
print(f"AI Answered: {guidance}")