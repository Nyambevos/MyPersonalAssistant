from abc import ABC, abstractmethod


class AssistantAbstract(ABC):
    @abstractmethod
    def main_loop(self):
        pass