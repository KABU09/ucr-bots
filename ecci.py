import requests
from bs4 import BeautifulSoup
from time import sleep
from datetime import datetime
from pathlib import Path
import json
import logging

from dotenv import dotenv_values

config = dotenv_values(".env")

TELEGRAM_BOT_TOKEN = config["TELEGRAM_BOT_TOKEN"]

ECCI_SEND_SAVED_FILE_MESSAGE = True if config["ECCI_SEND_SAVED_FILE_MESSAGE"] == "True" else False

ECCI_SEND_NEW_UPDATE_MESSAGE= True if config["ECCI_SEND_NEW_UPDATE_MESSAGE"] == "True" else False

ECCI_CONSOLE_PRINT = True if config["ECCI_CONSOLE_PRINT"] == "True" else False

ECCI_CHECK_FOR_NEW_UPDATES_TEACHING_ASSISTANT = True if config["ECCI_CHECK_FOR_NEW_UPDATES_TEACHING_ASSISTANT"] == "True" else False

logging.basicConfig(filename=f'{config["ROOT_OUTPUT_FOLDER_NAME"]}/{config["ECCI_ROOT_FOLDER_NAME"]}/{config["ECCI_LOG_FILE_NAME"]}', level=logging.INFO,
                    format="%(asctime)s %(lineno)d %(levelname)s: %(message)s")

def send_msg(text, channel):
    url_req = "https://api.telegram.org/bot" + TELEGRAM_BOT_TOKEN + \
    "/sendMessage" + "?chat_id=" + channel + "&text=" + text
    results = requests.get(url_req)
    logging.info(f'Respuesta de Telegram para {channel}: {results.text}')

def save_file(url, counter, channel):
    r = requests.get(url)
    url_split = url.split('/')
    name = url_split[len(url_split) - 1]
    try:
        path = f'{config["ROOT_OUTPUT_FOLDER_NAME"]}/{config["ECCI_ROOT_FOLDER_NAME"]}/{config["ECCI_SCHEDULES_FOLDER_NAME"]}/{counter}. {str(datetime.now())[:-7].replace(":", ".")} {name}'
        with open(path, 'wb+') as f:
            f.write(r.content)
        file = Path(path)
        if file.is_file():
            res = f'El horario {name} ha sido guardado con exito'
            logging.info(res)
            if ECCI_SEND_SAVED_FILE_MESSAGE:
                send_msg(res, channel)
    except Exception as err:
        res = f'ERROR al guardar el horario {name}'
        logging.error(f"{res}:  {err}")
        if ECCI_SEND_SAVED_FILE_MESSAGE:
            send_msg(res, channel)

def save_html(data, counter, channel):
    try:
        path = f'{config["ROOT_OUTPUT_FOLDER_NAME"]}/{config["ECCI_ROOT_FOLDER_NAME"]}/{config["ECCI_TEACHING_ASSISTANT_FOLDER_NAME"]}/{counter}. {str(datetime.now())[:-7].replace(":", ".")} asistencia.html'
        with open(path, 'w+', encoding='utf-8') as html:
            html.write(data)
        file = Path(path)
        if file.is_file():
            res = f'La pagina de asistencias ha sido guardada con exito'
            logging.info(res)
            if ECCI_SEND_SAVED_FILE_MESSAGE:
                send_msg(res, channel)
    except Exception as err:
        res = f'ERROR al guardar la pagina de asistencias'
        logging.error(f"{res}:  {err}")
        if ECCI_SEND_SAVED_FILE_MESSAGE:
            send_msg(res, channel)

is_new = False

while True:
    try:
        from urllib3.exceptions import InsecureRequestWarning
        requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

        r = requests.get(f'{config["ECCI_URL_TEACHING_ASSISTANT_URL"]}', verify = False)

        #parse html
        soup = BeautifulSoup(r.content, "html.parser")

        
        a_horario = soup.select_one(
            '#header > div > div > div > div > div:nth-child(2) > div > div > nav > ul > li.active.dropdown.active > ul > li:nth-child(1) > a')

        
        #get saved data
        with open(f'{config["ROOT_OUTPUT_FOLDER_NAME"]}/{config["ECCI_ROOT_FOLDER_NAME"]}/{config["ECCI_SCHEDULE_JSON_FILE_NAME"]}', 'r') as horario_read:
            data = json.load(horario_read)

        #compare url
        if data['horario'] != a_horario['href']:
            is_new = True
            data['horario'] = a_horario['href']
            response = f'Nueva version de horario de ECCI {a_horario["href"]}'
            logging.info(response)
            if ECCI_SEND_NEW_UPDATE_MESSAGE:
                send_msg(response, config["ECCI_SCHEDULE_TELEGRAM_CHANNEL"])
            save_file(a_horario['href'], data['horario_counter'], config["ECCI_SCHEDULE_TELEGRAM_CHANNEL"])
            data['horario_counter'] += 1

        if ECCI_CHECK_FOR_NEW_UPDATES_TEACHING_ASSISTANT:
            asistencia = str(soup.select_one('.main'))
            #compare html
            if data['asistencia'] != asistencia:
                is_new = True
                data['asistencia'] = asistencia
                response = f'Nuevo Cambio en Asistencias {config["ECCI_URL_TEACHING_ASSISTANT_URL"]}'
                logging.info(response)
                save_html(asistencia, data['asistencia_counter'], config["ECCI_TEACHING_ASSISTANT_TELEGRAM_CHANNEL"])
                data['asistencia_counter'] += 1
                if ECCI_SEND_NEW_UPDATE_MESSAGE:
                    send_msg(response, config["ECCI_TEACHING_ASSISTANT_TELEGRAM_CHANNEL"])

        if is_new:
            with open(f'{config["ROOT_OUTPUT_FOLDER_NAME"]}/{config["ECCI_ROOT_FOLDER_NAME"]}/{config["ECCI_SCHEDULE_JSON_FILE_NAME"]}', 'w+') as horario_write:
                json.dump(data, horario_write, indent= 4)
                is_new = False

        if ECCI_CONSOLE_PRINT:
            print(f'{datetime.now()} Solicitud exitosa a la ECCI')
        sleep(int(config["TIME_BETWEEN_REQUESTS_IN_SECONDS"]))

    except Exception as err:
        if ECCI_CONSOLE_PRINT:
            print(f'{datetime.now()} Se cayo la ECCI {err}')
        logging.error(f"Error en ECCI:  {str(err)}")