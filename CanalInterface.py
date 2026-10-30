
from abc import ABC, abstractmethod


class CanalInterface(ABC):
    @abstractmethod
    def enviar(self, destinatario: str, texto: str):
        pass

class CanalEmail(CanalInterface):
    def enviar(self, destinatario: str, texto: str):
        print(f"EMAIL a {destinatario}: {texto}")

class CanalSMS(CanalInterface):
    def enviar(self, destinatario, texto):
        print(f"SMS a {destinatario}: {texto}")

class CanalWhatsApp(CanalInterface):
    def enviar(self, destinatario: str, texto: str):
        print(f"WHATSAPP a {destinatario}: {texto}")
        