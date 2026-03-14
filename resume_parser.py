from pdfminer.high_level import extract_text
import tempfile

def extract_resume_text(uploaded_file):

    with tempfile.NamedTemporaryFile(delete=False) as tmp:

        tmp.write(uploaded_file.read())
        path = tmp.name

    text = extract_text(path)

    return text
