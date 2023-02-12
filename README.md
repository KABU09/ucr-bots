# Bots de la UCR (no oficiales)

Bots hechos inicialmente para uso personal, pero que pueden ser de utilidad para otros.

## Horarios ECCI

Fue creado dada la necesidad de estar al tanto de los cambios en los horarios publicados por la ECCI. Por ejemplo, si se abrió un grupo nuevo, se cerró otro o se modificó la hora de un grupo.

Enlace para unirse al canal de Telegram [@horariosecci](https://t.me/horariosecci)

Envía notificaciones sobre nuevos horarios publicados por la ECCI.

Es posible revisar el historial de horarios mediante un enlace de OneDrive.

## Asistencias ECCI

Enlace para unirse al canal de Telegram [@asistenciasecci](https://t.me/asistenciasecci)

Envía notificaciones sobre nuevas versiones de la página de asistencias de la ECCI.

Es posible revisar el historial de html mediante un enlace de OneDrive.

## Instrucciones para correrlo de forma local

1. Instalar [Python 3.x+](https://www.python.org/downloads/)
2. Crear un entorno virtual con `python -m venv venv`
3. Instalar dependencias con `pip install -r requirements.txt`
4. Rellenar las variables de entorno faltantes del archivo `.env`
5. Correr el bot con `py ecci.py`

### Variables de entorno

| Variable | Descripción | Valor por defecto |
| --- | --- | --- |
| ROOT_OUTPUT_FOLDER_NAME | Nombre de la carpeta donde se guardan los resultados del bot | output |
| ECCI_ROOT_FOLDER_NAME | Nombre de la carpeta donde se guardan los archivos de la ECCI | ECCI |
| ECCI_LOG_FILE_NAME | Nombre del archivo de log | ecci.log |
| ECCI_SCHEDULE_JSON_FILE_NAME | Nombre del archivo json donde se guardan datos para el funcionamiento del bot | horarios.json |
| ECCI_SCHEDULES_FOLDER_NAME | Nombre de la carpeta donde se guardan los archivos de los horarios | horarios |
| ECCI_TEACHING_ASSISTANT_FOLDER_NAME | Nombre de la carpeta donde se guardan los archivos de las asistencias | asistencias |
| ECCI_URL_TEACHING_ASSISTANT_URL | URL de la página de asistencias de la ECCI. También es usada para los horarios | https://ecci.ucr.ac.cr/asistencias |
| ECCI_SEND_NEW_UPDATE_MESSAGE | Enviar mensaje de actualización | True |
| ECCI_SEND_SAVED_FILE_MESSAGE | Enviar mensaje de archivo guardado | False |
| ECCI_CONSOLE_PRINT | Imprimir en consola | True |
| ECCI_CHECK_FOR_NEW_UPDATES_TEACHING_ASSISTANT | Revisar si hay nuevas versiones de la página de asistencias | False |
| ECCI_SCHEDULE_TELEGRAM_CHANNEL | Canal de Telegram donde se envían los mensajes de los horarios | Sin valor por defecto. El formato es `@nombredelcanal` |
| ECCI_TEACHING_ASSISTANT_TELEGRAM_CHANNEL | Canal de Telegram donde se envían los mensajes de las asistencias | Sin valor por defecto. El formato es `@nombredelcanal` |
| TELEGRAM_BOT_TOKEN | Token del bot de Telegram | Sin valor por defecto. Se debe obtener un [token](https://core.telegram.org/bots#how-do-i-create-a-bot)  |
| TIME_BETWEEN_REQUESTS_IN_SECONDS | Tiempo entre peticiones| 20 |


# UCR Bots (unofficial)

Bots made initially for personal use, but that can be useful for others.

## ECCI Schedules

It was created due to the need to keep up to date with changes in the schedules published by ECCI. For example, if a new group was opened, another was closed or the schedule of a group was modified.

Link to join the Telegram channel [@horariosecci](https://t.me/horariosecci)

Sends notifications about new schedules published by ECCI.

It is possible to review the schedule history through a OneDrive link.

## ECCI Teaching Assistants

Link to join the Telegram channel [@asistenciasecci](https://t.me/asistenciasecci)

Sends notifications about new versions of the ECCI teaching assistants page.

It is possible to review the html history through a OneDrive link.

## Instructions to run it locally

1. Install [Python 3.x+](https://www.python.org/downloads/)
2. Create a virtual environment with `python -m venv venv`
3. Install dependencies with `pip install -r requirements.txt`
4. Fill in the missing environment variables in the `.env` file
5. Run the bot with `py ecci.py`

## Environment variables

| Variable | Description | Default value |
| --- | --- | --- |
| ROOT_OUTPUT_FOLDER_NAME | Name of the folder where the bot results are saved | output |
| ECCI_ROOT_FOLDER_NAME | Name of the folder where the ECCI files are saved | ECCI |
| ECCI_LOG_FILE_NAME | Name of the log file | ecci.log |
| ECCI_SCHEDULE_JSON_FILE_NAME | Name of the json file where data for the bot operation is saved | horarios.json |
| ECCI_SCHEDULES_FOLDER_NAME | Name of the folder where the schedule files are saved | horarios |
| ECCI_TEACHING_ASSISTANT_FOLDER_NAME | Name of the folder where the teaching assistant files are saved | asistencias |
| ECCI_URL_TEACHING_ASSISTANT_URL | ECCI teaching assistant page URL. It is also used for the schedules | https://ecci.ucr.ac.cr/asistencias |
| ECCI_SEND_NEW_UPDATE_MESSAGE | Send update message | True |
| ECCI_SEND_SAVED_FILE_MESSAGE | Send saved file message | False |
| ECCI_CONSOLE_PRINT | Print in console | True |
| ECCI_CHECK_FOR_NEW_UPDATES_TEACHING_ASSISTANT | Check if there are new versions of the teaching assistant page | False |
| ECCI_SCHEDULE_TELEGRAM_CHANNEL | Telegram channel where the schedule messages are sent | No default value. The format is `@channelname` |
| ECCI_TEACHING_ASSISTANT_TELEGRAM_CHANNEL | Telegram channel where the teaching assistant messages are sent | No default value. The format is `@channelname` |
| TELEGRAM_BOT_TOKEN | Telegram bot token | No default value. You must obtain a [token](https://core.telegram.org/bots#how-do-i-create-a-bot)  |
| TIME_BETWEEN_REQUESTS_IN_SECONDS | Time between requests| 20 |