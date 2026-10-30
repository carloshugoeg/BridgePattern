from abc import ABC, abstractmethod
from CanalInterface import CanalInterface


class Notificacion(ABC):
    def __init__(self, canal: CanalInterface):
        self.canal = canal  # Referencia al implementador (Bridge)

    @abstractmethod
    def enviar(self, destinatario: str, mensaje: str):
        pass


class NotificacionSimple(Notificacion):
    def enviar(self, destinatario: str, mensaje: str):
        self.canal.enviar(destinatario, mensaje)


# Alias para coincidir con la terminología de "Notificación normal" en PROBLEMA.md
NotificacionNormal = NotificacionSimple


class NotificacionAlerta(Notificacion):
    def enviar(self, destinatario: str, mensaje: str):
        texto_alerta = f"[ALERTA] {mensaje}"
        self.canal.enviar(destinatario, texto_alerta)


class NotificacionUrgente(Notificacion):
    def enviar(self, destinatario: str, mensaje: str):
        texto_urgente = f"⚠️ [URGENTE]: {mensaje}"
        self.canal.enviar(destinatario, texto_urgente)


# ==========================================================
# ETAPA 3: NOTIFICACIÓN CON RESPALDO (Pareja A)
# ==========================================================
class NotificacionConRespaldo(Notificacion):
    def __init__(self, canal_principal: CanalInterface, canal_respaldo: CanalInterface):
        super().__init__(canal_principal)
        self.canal_respaldo = canal_respaldo

    def enviar(self, destinatario: str, mensaje: str):
        try:
            self.canal.enviar(destinatario, mensaje)
        except Exception:
            print("Canal no disponible, usando respaldo")
            # Cambia el canal activo al respaldo para que desde ahora use solo este
            self.canal = self.canal_respaldo
            self.canal.enviar(destinatario, mensaje)
