import re

def mask_pii(text):
    entities = []

    patterns = {
        "full_name": r"\b([A-Z][a-z]+\s[A-Z][a-z]+)\b",
        "email": r"[\w.-]+@[\w.-]+",
        "phone_number": r"\b\d{10}\b",
        "dob": r"\b\d{2}[/-]\d{2}[/-]\d{4}\b",
        "aadhar_num": r"\b\d{4}\s\d{4}\s\d{4}\b",
        "credit_debit_no": r"\b(?:\d[ -]*?){13,16}\b",
        "cvv_no": r"\b\d{3}\b",
        "expiry_no": r"\b(0[1-9]|1[0-2])/[0-9]{2}\b"
    }

    masked_text = text

    for label, pattern in patterns.items():
        for match in re.finditer(pattern, masked_text):
            start, end = match.span()
            original = match.group()
            entities.append({
                "position": [start, end],
                "classification": label,
                "entity": original
            })
            masked_text = masked_text[:start] + f"[{label}]" + masked_text[end:]

    return masked_text, entities

def unmask_pii(masked_text, entities):
    for entity in reversed(entities):
        start, end = entity["position"]
        original = entity["entity"]
        masked_text = masked_text[:start] + original + masked_text[end:]
    return masked_text
