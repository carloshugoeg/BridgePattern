# Diagrama Bridge — Sistema de notificaciones

Mapeo del patrón Bridge al problema de `PROBLEMA.md`.

| UML (genérico) | Este problema |
|---|---|
| Abstraction | `Notificacion` |
| Implementation | `Canal` |
| Concrete Implementation | `CanalEmail` (+ SMS / WhatsApp después) |
| Refined Abstraction | `NotificacionUrgente` / con respaldo (después) |
| Client | quien arma `Notificacion(CanalEmail)` y llama `enviar` |

```mermaid
classDiagram
    direction TB

    class Cliente {
    }
    note for Cliente "Notificación normal por email\na ana@uni.edu:\n«Entrega del proyecto el viernes»"

    class Notificacion {
        - canal: Canal
        + enviar(destinatario, texto)
    }
    note for Notificacion "feature1 → canal.enviar(...)\nNo conoce el canal concreto"

    class Canal {
        <<interface>>
        + enviar(destinatario, texto)
    }
    note for Canal "Contrato entre parejas\n(Pareja A ↔ Pareja B)"

    class CanalEmail {
        + enviar(destinatario, texto)
    }
    note for CanalEmail "EMAIL a <destinatario>: <texto>"

    class NotificacionUrgente {
        + enviar(destinatario, texto)
    }
    note for NotificacionUrgente "opcional / etapas posteriores"

    class CanalSMS {
        + enviar(destinatario, texto)
    }
    class CanalWhatsApp {
        + enviar(destinatario, texto)
    }
    note for CanalSMS "etapas posteriores"
    note for CanalWhatsApp "etapas posteriores"

    Cliente --> Notificacion : usa
    Notificacion o--> Canal : bridge
    NotificacionUrgente --|> Notificacion : hereda
    CanalEmail ..|> Canal : realiza
    CanalSMS ..|> Canal : realiza
    CanalWhatsApp ..|> Canal : realiza
```

El puente es el agregado `Notificacion → Canal`: Pareja A crece en tipos de aviso y Pareja B en canales, sin tocar el código de la otra.
