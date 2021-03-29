# -*- coding: utf-8 -*-
# # Copyright (c) 2007-2020 NovaReto GmbH
# # cklinger@novareto.de


from requests import Session
from zeep import Client, Transport

from uv.models.models import VersichertePerson, VersichertenFall, Unternehmen
from zeep.helpers import serialize_object


BASE_URL = "http://127.0.0.1:8080/webservice/"
BASE_URL = "https://srv-app01/rul310ws/"

AUTH_SERVICE = "de.hdpgmbh.framework.tools.services.runtime.CLoginService?wsdl"
MUB_SERVICE = "de.hdpgmbh.mubsrv.business.srvdomain.CdsMUBSRV?wsdl"
RUL_SERVICE = "de.hdpgmbh.rulsrv.business.srvdomain.CdsRulSrv?wsdl"


class CusaWebService(object):
    """ Cusa Web Service"""

    def __init__(self, url, login, password):
        session = Session()
        session.verify = False
        self.BASE_URL = url
        self.transport = Transport(session=session)
        self.session_token = self.login(login, password)

    def login(self, login, password):
        auth_service = Client(self.BASE_URL + AUTH_SERVICE, transport=self.transport)
        login_request_type = auth_service.get_type("ns1:cLoginRequest")
        login_request = login_request_type(loginName=login, password=password)
        result = auth_service.service.login(login_request)
        return result.sessionToken

    def get_unternehmen_by_az(self, az):
        client = Client(self.BASE_URL + MUB_SERVICE, transport=self.transport)
        result = client.service.rtvUnternehmenByAZ(self.session_token, az)
        return result

    def get_betriebsstaette_by_az(self, az):
        client = Client(self.BASE_URL + MUB_SERVICE, transport=self.transport)
        result = client.service.rtvBetriebsstaetteByAZ(self.session_token, az)
        return result

    def get_person_by_id(self, pid):
        client = Client(self.BASE_URL + RUL_SERVICE, transport=self.transport)
        result = serialize_object(
            client.service.rtvVersichertePersonByID(self.session_token, pid)
        )
        return VersichertePerson(**result)

    def get_unternehmen_by_mnr(self, mnr):
        client = Client(self.BASE_URL + RUL_SERVICE, transport=self.transport)
        result = serialize_object(
            client.service.rtvMitgliedByMitgliedsnummer01(self.session_token, mnr)
        )
        return Unternehmen(**result)

    def get_versicherungsfall_by_id(self, pid):
        client = Client(self.BASE_URL + RUL_SERVICE, transport=self.transport)
        result = serialize_object(
            client.service.rtvVersicherungsfallByID(self.session_token, pid)
        )
        return VersichertenFall(**result)


class TCusaWebService(CusaWebService):
    def __init__(self, data_dir):
        self.data_dir = data_dir

    def get_person_by_id(self, pid):
        with open(self.data_dir + "versicherteperson.json", "r") as json:
            return VersichertePerson.parse_raw(json.read())

    def get_unternehmen_by_mnr(self, mnr):
        with open(self.data_dir + "unternehmen.json", "r") as json:
            return Unternehmen.parse_raw(json.read())

    def get_versicherungsfall_by_id(self, pid):
        with open(self.data_dir + "versichertenfall.json", "r") as json:
            return VersichertenFall.parse_raw(json.read())
