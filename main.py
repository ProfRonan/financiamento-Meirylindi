"""Arquivo principal que será interpretado pelo interpretador."""


def main():
    """Função principal que será rodada quando o script for passado para o interpretador."""
    valor_principal = float(input('Digite o valor principal:'))
    taxa_juro = float(input('Digite a taxa de juros mensal:'))
    tempo = int(input('Digite quantidade de meses:'))
    valor_total_devido = valor_principal * (1 + taxa_juro/100)**tempo
    valor_do_juros = valor_total_devido - valor_principal
    print(f'O valor dos juros é igual à {valor_do_juros:.2f}.')


if __name__ == '__main__':
    main()
