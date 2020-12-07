# Especificação do exercício

Faça um script que calcule o valor de um juros seguindo uma taxa de juros mensal.
O script deve receber três valores do usuário.

1. O valor principal.
2. A taxa de juros mensal em **%** (ou seja, digitar *3* para uma taxa de *3%*).
3. O tempo em meses.

Em seguida o script deve calcular quanto é o valor dos juros ao final do período em mêses quando se realiza um empréstimo dado pelo valor principal considerando a taxa de juros inserida.

Em seguida o script deve exibir a seguinte mensagem: `O valor dos juros é igual à [valor dos juros com duas casas decimais].`.
É obrigatório o uso de `f'string'` para formatar a saída.

Dica: a taxa de júros é dada por `valor_total_devido = valor_principal * (1 + taxa_juros)^tempo`, considere nessa fórmula que `a^b` é igual à `a` elevado à `b`.
