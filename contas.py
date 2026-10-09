
from abc import ABC, abstractmethod


class Conta(ABC):
    """Classe abstrata que representa uma conta bancária."""

    def __init__(self, titular, numero, saldo=0.0):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("O titular deve possuir um nome válido.")
        self._titular = valor.strip()

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("O número da conta não pode ser vazio.")
        self._numero = valor.strip()

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise ValueError("O saldo deve ser numérico.")

        if valor < 0:
            raise ValueError("O saldo não pode ser negativo.")

        self._saldo = float(valor)

    def depositar(self, valor):
        """Adiciona dinheiro à conta."""
        self._validar_valor(valor)
        self.saldo += valor

    def sacar(self, valor):
        """Saca dinheiro respeitando as regras da conta."""
        self._validar_valor(valor)

        if valor > self.saldo:
            raise ValueError("Saldo insuficiente.")

        self.saldo -= valor

    @staticmethod
    def _validar_valor(valor):
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise ValueError("O valor deve ser numérico.")

        if valor <= 0:
            raise ValueError("O valor deve ser maior que zero.")

    @abstractmethod
    def calcular_rendimento(self):
        """Calcula o rendimento específico de cada tipo de conta."""
        pass

    def __str__(self):
        return (
            f"Conta {self.numero} | Titular: {self.titular} | "
            f"Saldo: R$ {self.saldo:.2f}"
        )

    def __repr__(self):
        return (
            f"{self.__class__.__name__}("
            f"titular={self.titular!r}, "
            f"numero={self.numero!r}, saldo={self.saldo!r})"
        )

    def __eq__(self, outra):
        if not isinstance(outra, Conta):
            return NotImplemented

        return self.numero == outra.numero

    def __lt__(self, outra):
        if not isinstance(outra, Conta):
            return NotImplemented

        return self.saldo < outra.saldo


class ContaCorrente(Conta):
    """Conta que aplica uma taxa de manutenção mensal."""

    def __init__(self, titular, numero, saldo=0.0, taxa_manutencao=15.0):
        super().__init__(titular, numero, saldo)
        self.taxa_manutencao = taxa_manutencao

    @property
    def taxa_manutencao(self):
        return self._taxa_manutencao

    @taxa_manutencao.setter
    def taxa_manutencao(self, valor):
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise ValueError("A taxa de manutenção deve ser numérica.")

        if valor < 0:
            raise ValueError("A taxa de manutenção não pode ser negativa.")

        self._taxa_manutencao = float(valor)

    def calcular_rendimento(self):
        """Retorna o saldo após descontar a taxa de manutenção."""
        return max(0.0, self.saldo - self.taxa_manutencao)

    def aplicar_manutencao(self):
        """Desconta a taxa se houver saldo suficiente."""
        if self.saldo < self.taxa_manutencao:
            raise ValueError("Saldo insuficiente para pagar a manutenção.")

        self.saldo -= self.taxa_manutencao

    def __str__(self):
        return (
            f"Conta Corrente {self.numero} | "
            f"Titular: {self.titular} | "
            f"Saldo: R$ {self.saldo:.2f} | "
            f"Taxa: R$ {self.taxa_manutencao:.2f}"
        )

    def __repr__(self):
        return (
            f"ContaCorrente(titular={self.titular!r}, "
            f"numero={self.numero!r}, saldo={self.saldo!r}, "
            f"taxa_manutencao={self.taxa_manutencao!r})"
        )


class ContaPoupanca(Conta):
    """Conta que calcula rendimento com base em uma taxa percentual."""

    def __init__(self, titular, numero, saldo=0.0, taxa_rendimento=0.5):
        super().__init__(titular, numero, saldo)
        self.taxa_rendimento = taxa_rendimento

    @property
    def taxa_rendimento(self):
        return self._taxa_rendimento

    @taxa_rendimento.setter
    def taxa_rendimento(self, valor):
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise ValueError("A taxa de rendimento deve ser numérica.")

        if not 0 <= valor <= 100:
            raise ValueError("A taxa deve estar entre 0 e 100.")

        self._taxa_rendimento = float(valor)

    def calcular_rendimento(self):
        """Calcula o saldo acrescido do rendimento percentual."""
        rendimento = self.saldo * (self.taxa_rendimento / 100)
        return self.saldo + rendimento

    def aplicar_rendimento(self):
        """Adiciona o rendimento calculado ao saldo."""
        self.saldo = self.calcular_rendimento()

    def __str__(self):
        return (
            f"Conta Poupança {self.numero} | "
            f"Titular: {self.titular} | "
            f"Saldo: R$ {self.saldo:.2f} | "
            f"Rendimento: {self.taxa_rendimento:.2f}%"
        )

    def __repr__(self):
        return (
            f"ContaPoupanca(titular={self.titular!r}, "
            f"numero={self.numero!r}, saldo={self.saldo!r}, "
            f"taxa_rendimento={self.taxa_rendimento!r})"
        )
