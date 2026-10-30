from abc import ABC, abstractmethod


# ==========================================================
# PAREJA B: JERARQUÍA DE IMPLEMENTACIÓN (CANALES)
# ==========================================================
class CanalInterface(ABC):
    @abstractmethod
    def enviar(self, destinatario: str, texto: str):
        pass


class CanalEmail(CanalInterface):
    def enviar(self, destinatario: str, texto: str):
        print(f"EMAIL a {destinatario}: {texto}")


class CanalSMS(CanalInterface):
    def enviar(self, destinatario: str, texto: str):
        print(f"SMS a {destinatario}: {texto[:30]}")


class CanalWhatsApp(CanalInterface):
    def enviar(self, destinatario: str, texto: str):
        print(f"WHATSAPP a {destinatario}: {texto}")


# Canal falso que siempre falla para probar sin esperar a la Pareja B
class CanalFalso(CanalInterface):
    def enviar(self, destinatario: str, texto: str):
        raise RuntimeError("Fallo intencional en canal principal")


# ==========================================================
# PAREJA A: JERARQUÍA DE ABSTRACCIÓN (NOTIFICACIONES)
# ==========================================================
class Notificacion(ABC):
    def __init__(self, canal: CanalInterface):
        self.canal = canal  # Referencia al implementador (Bridge)

    @abstractmethod
    def enviar(self, destinatario: str, mensaje: str):
        pass


class NotificacionSimple(Notificacion):
    def enviar(self, destinatario: str, mensaje: str):
        self.canal.enviar(destinatario, mensaje)


NotificacionNormal = NotificacionSimple


class NotificacionAlerta(Notificacion):
    def enviar(self, destinatario: str, mensaje: str):
        texto_alerta = f"[ALERTA] {mensaje}"
        self.canal.enviar(destinatario, texto_alerta)


class NotificacionUrgente(Notificacion):
    def enviar(self, destinatario: str, mensaje: str):
        texto_urgente = f"⚠️ [URGENTE]: {mensaje}"
        self.canal.enviar(destinatario, texto_urgente)


# --- ETAPA 3: Notificación con respaldo ---
class NotificacionConRespaldo(Notificacion):
    def __init__(self, canal_principal: CanalInterface, canal_respaldo: CanalInterface):
        super().__init__(canal_principal)
        self.canal_respaldo = canal_respaldo

    def enviar(self, destinatario: str, mensaje: str):
        try:
            self.canal.enviar(destinatario, mensaje)
        except Exception:
            print("Canal no disponible, usando respaldo")
            # Cambia el canal actual al de respaldo para que desde entonces use solo el respaldo
            self.canal = self.canal_respaldo
            self.canal.enviar(destinatario, mensaje)


# ==========================================================
# ESCENARIO ETAPA 3 (Tarjeta de la imagen)
# ==========================================================
if __name__ == "__main__":
    canal_principal_falso = CanalFalso()
    canal_respaldo_email = CanalEmail()

    notif_respaldo = NotificacionConRespaldo(canal_principal_falso, canal_respaldo_email)

    # Dos envíos a ana@uni.edu
    notif_respaldo.enviar("ana@uni.edu", "Reunión a las 10")
    notif_respaldo.enviar("ana@uni.edu", "Traigan sus computadoras")
