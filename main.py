from conversor import *

while True:

    print("""
===== FILE CONVERTER =====

1 TXT → PDF
2 PDF → TXT
3 IMAGEM → PDF
4 DOCX → TXT
5 SAIR

""")

    op = input(
        "Escolha: "
    )

    if op == "5":
        break

    entrada = input(
        "Arquivo origem: "
    )

    saida = input(
        "Arquivo destino: "
    )

    try:

        if op == "1":
            txt_para_pdf(
                entrada,
                saida
            )

        elif op == "2":
            pdf_para_txt(
                entrada,
                saida
            )

        elif op == "3":
            imagem_para_pdf(
                entrada,
                saida
            )

        elif op == "4":
            docx_para_txt(
                entrada,
                saida
            )

        else:
            print(
                "Opção inválida"
            )

    except Exception as e:

        print(
            "Erro:",
            e
        )