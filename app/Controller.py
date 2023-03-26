import json
import os
import ydb
import ydb.iam
from AliceReqests import AliceResponse, AliceRequest


def handler(event, context):
    request = AliceRequest(event)
    response = AliceResponse(request)
    if request.is_new_session:
        response.set_text(
            "Привет! Ты попал в навык «Реши задачу»! Возьми ручку и тетрадку, и давай решать задачи. Начинаем?",
            tts=True)
        response.add_button('Да')
        response.add_button('Нет')
        response.set_session_state_value("greeting")
    if request.state_session_value == "greeting" and request.command == "нет":
        response.set_text("Очень жаль что ты уходишь, возвращайся скорее")
        response.end()
    elif request.state_session_value == "greeting" and request.command == "да":
        response.set_text("Какую тему выберем?")
    return response._response_dict


print(handler(json.load(open("test.json")), 1))