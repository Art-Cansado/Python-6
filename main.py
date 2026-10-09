
from contas import Conta, ContaCorrente, ContaPoupanca


def exibir_titulo(titulo):
    print("\n" + "=" * 60)
    print(titulo)
    print("=" * 60)


def demonstrar_excecao():
    """Demonstra o tratamento de operações inválidas."""
    exibir_titulo("TESTES DE VALIDACAO E EXCECOES")

    try:
        ContaCorrente("Carlos", "001", -100)
    except ValueError as erro:
        print(f"Erro ao criar conta: {erro}")

    try:
        conta_teste = ContaCorrente("Marina", "002", 100)
        conta_teste.depositar(-50)
    except ValueError as erro:
        print(f"Erro ao depositar: {erro}")

    try:
        conta_teste.sacar(500)
    except ValueError as erro:
        print(f"Erro ao sacar: {erro}")

    try:
        ContaPoupanca("Pedro", "003", 100, 150)
    except ValueError as erro:
        print(f"Erro na taxa de rendimento: {erro}")


def main():
    exibir_titulo("SISTEMA BANCARIO - POO")

    # Criacao de 10 objetos de contas.
    contas = [
        ContaCorrente("Ana", "CC001", 1500, 15),
        ContaPoupanca("Bruno", "CP001", 2000, 0.5),
        ContaCorrente("Carla", "CC002", 800, 20),
        ContaPoupanca("Daniel", "CP002", 3500, 0.7),
        ContaCorrente("Eduarda", "CC003", 1200, 12),
        ContaPoupanca("Felipe", "CP003", 2500, 0.6),
        ContaCorrente("Gabriela", "CC004", 950, 10),
        ContaPoupanca("Henrique", "CP004", 4000, 0.8),
        ContaCorrente("Isabela", "CC005", 1800, 15),
        ContaPoupanca("Joao", "CP005", 3000, 0.5)
    ]

    exibir_titulo("CONTAS CADASTRADAS")

    for conta in contas:
        print(conta)

    # Demonstracao de polimorfismo:
    # a mesma chamada produz resultados diferentes.
    exibir_titulo("POLIMORFISMO - CALCULO")

    for conta in contas:
        resultado = conta.calcular_rendimento()
        print(
            f"{type(conta).__name__} | {conta.titular} | "
            f"Resultado: R$ {resultado:.2f}"
        )

    # Demonstracao de deposito e saque.
    exibir_titulo("OPERACOES BANCARIAS")

    conta = contas[0]

    print("Antes:", conta)
    conta.depositar(300)
    print("Depois do deposito de R$ 300:", conta)

    conta.sacar(100)
    print("Depois do saque de R$ 100:", conta)

    # Aplicacao de rendimento na poupanca.
    poupanca = contas[1]

    print("\nAntes do rendimento:", poupanca)
    poupanca.aplicar_rendimento()
    print("Depois do rendimento:", poupanca)

    # Aplicacao da taxa de manutencao na conta corrente.
    corrente = contas[0]

    print("\nAntes da manutencao:", corrente)
    corrente.aplicar_manutencao()
    print("Depois da manutencao:", corrente)

    # Ordenacao usando o metodo especial __lt__.
    exibir_titulo("CONTAS ORDENADAS POR SALDO")

    for conta in sorted(contas):
        print(conta)

    # Demonstracao de __repr__.
    exibir_titulo("REPRESENTACAO TECNICA (__repr__)")

    print(repr(contas[0]))

    # Demonstracao de __eq__.
    exibir_titulo("COMPARACAO DE CONTAS (__eq__)")

    conta_a = contas[0]
    conta_b = ContaCorrente("Outro titular", "CC001", 500)

    print(f"Conta A: {conta_a.numero}")
    print(f"Conta B: {conta_b.numero}")
    print(f"Possuem o mesmo numero? {conta_a == conta_b}")

    # A classe abstrata nao pode ser instanciada diretamente.
    exibir_titulo("TESTE DA CLASSE ABSTRATA")

    try:
        Conta("Teste", "000", 100)
    except TypeError as erro:
        print(f"Erro esperado: {erro}")

    demonstrar_excecao()

    exibir_titulo("FIM DO SISTEMA")


if __name__ == "__main__":
    main()
