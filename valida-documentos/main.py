from valida_documentos import Documento

cpf = "71198430877"
cnpj = "65832151000151"

documento1 = Documento.cria_documento(cpf)
documento2 = Documento.cria_documento(cnpj)

print(documento1)
print(documento2)
