from AliceReqests import AliceResponse, AliceRequest


def handler(event, context):
    request = AliceRequest(event)
    response = AliceResponse(request)
    response.set_text("Ты крутой!!!")
    return response._response_dict
