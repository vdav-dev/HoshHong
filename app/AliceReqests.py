import json


class AliceRequest(object):  # запрос
    def __init__(self, request_dict):
        self._request_dict = request_dict

    @property
    def version(self):
        return self._request_dict['version']

    @property
    def session(self):
        return self._request_dict['session']

    @property
    def session_state(self):
        if 'session_state' in self._request_dict.keys():
            return self._request_dict['session_state']
        return None

    @property
    def session_state_value(self):
        if self.session_state is None:
            return None
        return self.session_state['value']

    @property
    def user_id(self):
        return self.session['user_id']

    @property
    def is_screen(self):
        return 'screen' in self._request_dict['meta']['interfaces'].keys()

    @property
    def is_new_session(self):
        return bool(self.session['new'])

    @property
    def command(self):
        return self._request_dict['request']['command']

    def __str__(self):
        return str(self._request_dict)

    def __repr__(self):
        return self.dumps()


class AliceResponse(object):  # ответ
    def __init__(self, alice_request):
        self._response_dict = {
            "version": alice_request.version,
            "session": alice_request.session,
            "response": {
                "text": "",
                "end_session": False
            }
        }

    def dumps(self):
        return json.dumps(
            self._response_dict,
            ensure_ascii=False,
            indent=2
        )

    def set_text(self, text, tts=False):
        if tts:
            self._response_dict['response']['text'] = text[:1024]
            self._response_dict['response']['tts'] = text[:1024]
        else:
            self._response_dict['response']['text'] = text[:1024]

    def set_value(self, value):
        self._response_dict["session_state"] = {}
        self._response_dict["session_state"]["value"] = value

    def add_button(self, button):
        if 'buttons' not in self._response_dict['response'].keys():
            self._response_dict['response']['buttons'] = []
            self._response_dict['response']['buttons'].append({"title": button})
        else:
            self._response_dict['response']['buttons'].append({"title": button})

    def add_payload_to_button(self, index_of_button: int, payload: dict):
        self._response_dict['response']['buttons'][index_of_button]['payload'] = payload

    def add_url_to_button(self, index_of_button: int, url: str):
        self._response_dict['response']['buttons'][index_of_button]['url'] = url

    def add_hide_to_button(self, index_of_button: int, hide: bool):
        self._response_dict['response']['buttons'][index_of_button]['hide'] = hide

    def end(self):
        self._response_dict["response"]["end_session"] = True

    def __str__(self):
        return self.dumps()
