# Bot-de-Telegram-3

Este proyecto consiste en un bot básico para Telegram desarrollado en Python utilizando la librería TeleBot.

## Descripción

Este repositorio contiene el código fuente necesario para crear un bot de Telegram funcional. El bot está diseñado para responder a comandos básicos y puede ser extendido fácilmente para agregar nuevas funcionalidades según sea necesario.

## Configuración

Sigue estos pasos para configurar y ejecutar el bot en tu entorno local:

1. **Clonar el Repositorio**: Utiliza Git para clonar este repositorio en tu máquina local utilizando el siguiente comando:

    ```bash
    git clone https://github.com/tu_usuario/Bot-de-Telegram-3.git
    ```

2. **Instalar Dependencias**: Navega al directorio del proyecto y utiliza pip para instalar las dependencias necesarias:

    ```bash
    cd Bot-de-Telegram-3
    pip install -r requirements.txt
    ```

3. **Obtener Token de Bot**: Crea un nuevo bot en Telegram utilizando el BotFather y obtén el token del bot recién creado.

4. **Configurar el Token**: Abre el archivo `main.py` en un editor de texto y reemplaza `"TU_TOKEN_AQUÍ"` con el token obtenido en el paso anterior.

5. **Ejecutar el Bot**: Ejecuta el script `main.py` utilizando Python para iniciar el bot:

    ```bash
    python main.py
    ```

## Funcionalidades

El bot actualmente cuenta con las siguientes funcionalidades:

- **Comando `/start`**: Inicia el bot y muestra un mensaje de bienvenida al usuario.

- **Comando `/help`**: Proporciona información sobre cómo utilizar el bot y las funcionalidades disponibles.

- **Comando `/about`**: Muestra información sobre el bot, incluyendo detalles sobre su propósito y quién lo creó.

- **Comando `/excusa`**: Genera una excusa convincente utilizando elementos aleatorios de quien, acción, qué y cuándo.

## Personalización

Si deseas agregar nuevas funcionalidades o personalizar el comportamiento del bot, puedes modificar el archivo `main.py` según tus necesidades. La documentación de TeleBot puede ser útil para comprender cómo extender la funcionalidad del bot.

## Autoría

Este proyecto fue desarrollado por [Eduardo Hernández Guzmán](https://github.com/EduardoHernandezGuzman). Puedes encontrar más proyectos interesantes en mi perfil de GitHub.
