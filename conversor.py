from PIL import Image
from pypdf import PdfReader
from docx import Document
from reportlab.pdfgen import canvas


def txt_para_pdf(entrada, saida):

    c = canvas.Canvas(saida)

    with open(
        entrada,
        "r",
        encoding="utf-8"
    ) as f:

        y = 800

        for linha in f:

            c.drawString(
                50,
                y,
                linha.strip()
            )

            y -= 20

            if y < 50:
                c.showPage()
                y = 800

    c.save()

    print("TXT → PDF concluído")


def pdf_para_txt(entrada, saida):

    reader = PdfReader(entrada)

    texto = ""

    for pagina in reader.pages:

        texto += (
            pagina.extract_text()
            + "\n"
        )

    with open(
        saida,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(texto)

    print("PDF → TXT concluído")


def imagem_para_pdf(
    entrada,
    saida
):

    img = Image.open(entrada)

    if img.mode != "RGB":
        img = img.convert("RGB")

    img.save(saida)

    print("Imagem → PDF concluído")


def docx_para_txt(
    entrada,
    saida
):

    doc = Document(
        entrada
    )

    texto = "\n".join(
        p.text
        for p in doc.paragraphs
    )

    with open(
        saida,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(texto)

    print("DOCX → TXT concluído")