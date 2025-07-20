import os
import json
from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from app.services.helper import save_upload_to_temp_file, extract_clean
from app.services.prompt import chat_prompt
from app.services.llm import llm


router = APIRouter(prefix="", tags=["WhatsApp Lead Extraction Bot"])

@router.post('/upload-file')
async def upload_file(file: UploadFile = File(...)):
    """
    Upload a WhatsApp .txt file, extract lead info using LLM, and return structured JSON.
    """
    temp_file_path = None
    try:
        # Save the uploaded file to a temporary location
        temp_file_path = save_upload_to_temp_file(file)

        # Extract and clean text from WhatsApp chat
        chat_text = extract_clean(temp_file_path)

        # Generate structured lead JSON via LLM
        chain = chat_prompt | llm 
        response = chain.invoke({"chat_text": chat_text})

        # Parse and return the JSON content
        parsed_json = json.loads(response.content)
        return JSONResponse(content=parsed_json)

    except Exception as e:
        # Handle any error during upload, processing, or LLM call
        return JSONResponse(status_code=500, content={"error": str(e)})

    finally:
        # Always clean up the temporary file
        if temp_file_path and os.path.exists(temp_file_path):
            os.remove(temp_file_path)