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

    return response._response_dict
