# domain/interfaces/repositories.py

from abc import ABC, abstractmethod

class IContaRepository(ABC):
    @abstractmethod
    def obter_conta_por_id(self, conta_id: int):
        pass