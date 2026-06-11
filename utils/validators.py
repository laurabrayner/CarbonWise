"""
MÓDULO: utils/validators.py
RESPONSÁVEIS: Geral (Pessoa 3 / Pessoa 4)

Este módulo contém funções auxiliares de validação de dados para garantir a consistência
do que é inserido no sistema, antes de passar para os controladores.
"""


def limpar_cnpj(cnpj_sujo: str) -> str:
    """
    Remove caracteres especiais de um CNPJ (deixando apenas números).
    
    Exemplo: "12.345.678/0001-90" -> "12345678000190"
    """
    if not cnpj_sujo:
        return ""
    return "".join(char for char in cnpj_sujo if char.isdigit())


def validar_cnpj_formato(cnpj: str) -> bool:
    """
    Verifica se o CNPJ possui exatamente 14 dígitos numéricos.
    Isso permite o uso de CNPJs fictícios e reais para testes.
    """
    cnpj_limpo = limpar_cnpj(cnpj)
    return len(cnpj_limpo) == 14
