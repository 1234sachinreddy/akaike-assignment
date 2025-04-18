# Email Classification API with PII Masking

This project implements an email classification system for support teams with PII masking and API deployment using FastAPI.

## 🚀 Features
- Detects and masks personal information (PII) like name, email, phone number, etc.
- Classifies emails into categories like Billing Issues, Technical Support, etc.
- Returns output in the required structured JSON format.
- Deployable via FastAPI (Hugging Face or local server).

## 📦 Project Structure
```
.
├── app.py              # FastAPI app
├── models.py           # ML Model training and inference
├── utils.py            # PII masking/unmasking logic
├── requirements.txt    # Python dependencies
├── README.md           # Project overview and setup
```

## 🛠 Setup Instructions
```bash
pip install -r requirements.txt
python app.py
```

## 🧪 API Usage
**Endpoint:** `/classify`
**Method:** `POST`

### Input JSON
```json
{
  "input_email_body": "Hi, my name is John Doe and I need help with billing."
}
```

### Output JSON
```json
{
  "input_email_body": "Hi, my name is John Doe and I need help with billing.",
  "list_of_masked_entities": [
    {
      "position": [17, 25],
      "classification": "full_name",
      "entity": "John Doe"
    }
  ],
  "masked_email": "Hi, my name is [full_name] and I need help with billing.",
  "category_of_the_email": "Billing Issues"
}
```
