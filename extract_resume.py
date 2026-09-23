from pathlib import Path
from pypdf import PdfReader

pdf = Path(r'C:\Users\acer\portfolio\static\resume\resume.pdf')
print('exists:', pdf.exists())
reader = PdfReader(str(pdf))
print('pages:', len(reader.pages))
out = ''
for i, page in enumerate(reader.pages[:40], 1):
    txt = page.extract_text() or ''
    out += f'--- PAGE {i} ---\n{txt}\n'
print(out[:50000])
