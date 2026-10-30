# El problema

La universidad quiere avisar a sus estudiantes de entregas, reuniones e incidencias. Hoy solo envía **correos**, pero ya se sabe que vendrán **más canales** (SMS, WhatsApp...) y **más tipos de aviso** (urgentes, con respaldo si un canal falla...).

En cada grupo de 4, dos parejas trabajarán al mismo tiempo: una en los **tipos de notificación** y otra en los **canales**.

### SU MISIÓN
Diseñar y programar, en el lenguaje orientado a objetos que elijan, el sistema de notificaciones de modo que **cada pareja pueda crecer sin tocar el código de la otra.**

Los requisitos cambiarán por etapas, como en un proyecto real. Diseñen pensando en lo que todavía no conocen.

---

# Reglas

### PAREJA A • NOTIFICACIONES
**Jerarquía de abstracción**
Qué se notifica y cómo se comporta la notificación.
Ejemplos: notificación normal, urgente, con respaldo...

### PAREJA B • CANALES
**Jerarquía de implementación**
Por dónde sale el mensaje.
Ejemplos: email, SMS, WhatsApp...

*   **Grupos de 4 estudiantes**, divididos en **dos parejas**: la pareja A y la pareja B.
*   **Una computadora por pareja.** Cada grupo elige un lenguaje orientado a objetos; las dos parejas del grupo usan el mismo. **No hay código inicial.**
*   **Cada tarjeta trae una salida esperada.**
*   **Regla de oro:** no modifiquen clases de la otra pareja. Si lo hacen, o si cambian el contrato entre parejas, anótenlo.

---

# Etapa 1 • La base

**JUNTOS, PRIMERO EN PAPEL (~3 MIN)**
Acuerden el **contrato** entre notificaciones y canales: ¿qué operación ofrece un canal y qué recibe?

**PAREJA A**
Una **notificación** que envía un texto a un destinatario a través de un canal. La notificación no debe saber qué canal concreto usa.

**PAREJA B**
Un **canal de email** que muestra en consola:
`EMAIL a <destinatario>: <texto>`

### ESCENARIO
Notificación normal por email a `ana@uni.edu` : «Entrega del proyecto el viernes».

**SALIDA ESPERADA**
```text
EMAIL a ana@uni.edu: Entrega del proyecto el viernes