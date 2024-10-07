# adapters/repository/contas_repository.py

from domain.entities.conta import Conta
from domain.interfaces.repository import IContaRepository


class ContasRepositoryMemoria(IContaRepository):
    def obter_conta_por_id(self, conta_id: int) -> Conta:
        return Conta(conta_id, "Ageu Ribeiro", 100.0)