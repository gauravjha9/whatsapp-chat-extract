import os
import re
import shutil
from tempfile import NamedTemporaryFile
from fastapi import UploadFile


def save_upload_to_temp_file(file: UploadFile) -> str:
    """
    Save an uploaded file to a temporary file and return the file path.
    """
    with NamedTemporaryFile(delete=False) as temp_file:
        shutil.copyfileobj(file.file, temp_file)
        return temp_file.name


def clean_chat(raw_text: str) -> str:
    """
    Cleans a raw WhatsApp chat text by removing timestamps
    and extracting sender-message pairs in 'Sender: Message' format.
    """
    lines = raw_text.strip().split("\n")
    cleaned = []
    for line in lines:
        match = re.match(r'\[\d{1,2}:\d{2}(?:\s?[APap][Mm])?(?:, .*?)?\] (.*?): (.*)', line)
        if match:
            sender, message = match.groups()
            cleaned.append(f"{sender.strip()}: {message.strip()}")
    return "\n".join(cleaned)


def extract_clean(file_path: str) -> str:
    """
    Reads a WhatsApp .txt file and returns cleaned chat content.
    Handles encoding issues and passes content to clean_chat().
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            raw_text = f.read()
    except UnicodeDecodeError:
        with open(file_path, 'r', encoding='latin1') as f:
            raw_text = f.read()

    return clean_chat(raw_text)

