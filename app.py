from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import List, Tuple
import uvicorn
from utils import mask_pii, unmask_pii
from models import classify_email

app = FastAPI()

class Entity(BaseModel):
    position: Tuple[int, int]
    classification: str
    entity: str

class EmailRequest(BaseModel):
    input_email_body: str

class EmailResponse(BaseModel):
    input_email_body: str
    list_of_masked_entities: List[Entity]
    masked_email: str
    category_of_the_email: str

@app.post("/classify", response_model=EmailResponse)
async def classify(request: EmailRequest):
    email_text = request.input_email_body
    masked_email, entities = mask_pii(email_text)
    category = classify_email(masked_email)

    entity_objs = [Entity(position=e["position"], classification=e["classification"], entity=e["entity"]) for e in entities]

    return EmailResponse(
        input_email_body=email_text,
        list_of_masked_entities=entity_objs,
        masked_email=masked_email,
        category_of_the_email=category
    )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
