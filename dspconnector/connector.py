import requests
from django.conf import settings
from datetime import date, timedelta


class DSPConnectorException(Exception):

    response = None

    def __init__(self, resp):
        if resp:
            self.message = "Exception due to status code: %s" % resp.status_code
            self.response = resp
        else:
            self.message = "Connection error, please try again later."
            self.response = None


class DSPConnectorV12(object):

    @staticmethod
    def get_topics():
        return DSPConnectorV12._get(DSPConnectorV12.generate_url('/get_topics'))

    @staticmethod
    def get_news(topic_ids=list()):
        ids = ','.join(map(str, topic_ids)) if isinstance(topic_ids, dict) else topic_ids
        return DSPConnectorV12._get(DSPConnectorV12.generate_url(
            endpoint='/get_news',
            parameter='?topic_ids={}'.format(ids)
        ))

    @staticmethod
    def search_news(topic_ids='', params=None):
        # Default value for params
        params = params or {
            'since': (date.today()-timedelta(1)).strftime('%d-%m-%Y'),
            'cursor': -1
        }

        # topic_ids can be: STRING of comma separated ids or LIST of integers
        ids = ','.join(map(str, topic_ids)) if isinstance(topic_ids, list) else topic_ids
        parameters = '?topic_ids={}'.format(ids)

        for key, value in params.iteritems():
            parameters += "&{key}={value}".format(key=key, value=value)

        url = DSPConnectorV12.generate_url(
            endpoint='/search_news',
            parameter=parameters)
        return DSPConnectorV12._get(url)

    @staticmethod
    def get_audiences(topic_id):
        return DSPConnectorV12._get(DSPConnectorV12.generate_url(
            endpoint='/get_audiences',
            parameter='?topic_id={}'.format(topic_id))
        )

    @staticmethod
    def generate_url(endpoint, parameter=None):
        return settings.DSP_BASE_URL + '/api/v1.2' + endpoint + parameter if parameter else settings.DSP_BASE_URL + '/api/v1.2' + endpoint

    @staticmethod
    def _wrapper_request(response):
        if response and response.status_code < 205:
            return response.json()
        raise DSPConnectorException(response)

    @staticmethod
    def _get(url):
        try:
            response = requests.get(url, timeout=8)
        except:
            response = None
        return DSPConnectorV12._wrapper_request(response=response)


class DSPConnector(object):

    @staticmethod
    def get_themes():
        return DSPConnector._get(DSPConnector.generate_url(endpoint=settings.DSP_GET_THEMES))

    @staticmethod
    def get_feeds(theme_name, date='yesterday', cursor=-1):
        return DSPConnector._get(DSPConnector.generate_url(endpoint=settings.DSP_GET_FEEDS,
                                                           parameter='?themename={}&date={}&cursor={}'.format(
                                                               theme_name, date, cursor)))
    
    @staticmethod
    def get_influencers(theme_name):
        return DSPConnector._get(DSPConnector.generate_url(endpoint=settings.DSP_GET_INFLUENCERS,
                                                           parameter='?themename={}'.format(theme_name)))

    @staticmethod
    def generate_url(endpoint, parameter=None):
        return settings.DSP_API_URL + endpoint + parameter if parameter else settings.DSP_API_URL + endpoint

    @staticmethod
    def _wrapper_request(response):
        if response and response.status_code < 205:
            return response.json()
        raise DSPConnectorException(response)

    @staticmethod
    def _get(url):
        try:
            response = requests.get(url, timeout=8)
        except:
            response = None
        return DSPConnector._wrapper_request(response=response)
