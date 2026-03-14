from pdfminer.high_level import extract_text
import tempfile

def extract_resume_text(uploaded_file):

    with tempfile.NamedTemporaryFile(delete=False) as tmp:

        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    text = extract_text(tmp_path)

    return text
