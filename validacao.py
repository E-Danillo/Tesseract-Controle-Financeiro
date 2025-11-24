def validar_valor(valor):
    try:
        valor = float(valor)
        if valor <= 0:
            return False, "O valor deve ser maior que zero."
        return True, valor
    except ValueError:
        return False, "Valor inválido. Digite um número."

def validar_descricao(desc):
    if desc is None:
        return True, ""
    if not isinstance(desc, str):
        return False, "Descrição deve ser texto."
    return True, desc.strip()
