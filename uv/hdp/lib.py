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
EDOK_SERVICE = "de.hdpgmbh.rulsrv.business.srvdomain.CdsEdokRegistrieren?wsdl"


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

    # 1.1   RULS001
    def get_verifyExistsVersfallByVersfallAZ(self, pid):
        client = Client(self.BASE_URL + RUL_SERVICE, transport=self.transport)
        result = serialize_object(
            client.service.verifyExistsVersfallByVersfallAZ(self.session_token, pid)
        )
        return result

    # 1.2   RULS002
    def get_rtvVersfallByAZ(self, pid):
        client = Client(self.BASE_URL + RUL_SERVICE, transport=self.transport)
        result = serialize_object(
            client.service.rtvVersfallByAZ(self.session_token, pid)
        )
        return result

    # 1.3   RULS003
    def get_verifyExistsVersfaelleByUnternehmenAZ(self, pid):
        client = Client(self.BASE_URL + RUL_SERVICE, transport=self.transport)
        result = serialize_object(
            client.service.verifyExistsVersfaelleByUnternehmenAZ(self.session_token, pid)
        )
        return result

    ## 1.4   RULS004
    #def get_rtvListVersfaelleWithUnfalldatumAfterVgldatumByUnternehmensAZ(self, pid):
    #    client = Client(self.BASE_URL + RUL_SERVICE, transport=self.transport)
    #    request_type = client.get_type('ns0:rtvListVersfaelleWithUnfalldatumAfterVgldatumByUnternehmensAZ')
    #    constraint = client.get_type('ns1:listConstraint')(start=1, max=10, isOverflowAllowed=True)
    #    result = client.service.rtvListVersfaelleWithUnfalldatumAfterVgldatumByUnternehmensAZ(
    #        sessionToken=self.session_token, unternehmenAZ=pid, listConstraint=constraint)
    #    return result

    # 1.13   RULS014
    def get_rtvVersicherungsfallByID(self, pid):
        client = Client(self.BASE_URL + RUL_SERVICE, transport=self.transport)
        result = serialize_object(
            client.service.rtvVersicherungsfallByID(self.session_token, pid)
        )
        return result

    # 1.14   RULS015
    def get_rtvVersichertePersonByID(self, pid):
        client = Client(self.BASE_URL + RUL_SERVICE, transport=self.transport)
        result = serialize_object(
            client.service.rtvVersichertePersonByID(self.session_token, pid)
        )
        return result

    # 1.15   RULS016
    def get_rtvMitgliedByMitgliedsnummer01(self, pid):
        client = Client(self.BASE_URL + RUL_SERVICE, transport=self.transport)
        result = serialize_object(
            client.service.rtvMitgliedByMitgliedsnummer01(self.session_token, pid)
        )
        return result

    # 1.16   RULS017
    def get_rtvIKDatensatzByIKNummer(self, pid):
        client = Client(self.BASE_URL + RUL_SERVICE, transport=self.transport)
        result = serialize_object(
            client.service.rtvIKDatensatzByIKNummer(self.session_token, pid)
        )
        return result

    # 1.17   RULS018
    def get_rtvAufbereiteteAdresseByIKNummer(self, pid):
        client = Client(self.BASE_URL + RUL_SERVICE, transport=self.transport)
        result = serialize_object(
            client.service.rtvAufbereiteteAdresseByIKNummer(self.session_token, pid)
        )
        return result

    # 1.18   RULS019
    def get_rtvAufbereiteteAdresseByPersonID(self, pid):
        client = Client(self.BASE_URL + RUL_SERVICE, transport=self.transport)
        result = serialize_object(
            client.service.rtvAufbereiteteAdresseByPersonID(self.session_token, pid)
        )
        return result

    # 1.19   RULS020
    def get_rtvAufbereiteteAdresseByMitgliedsnummer(self, pid):
        client = Client(self.BASE_URL + RUL_SERVICE, transport=self.transport)
        result = serialize_object(
            client.service.rtvAufbereiteteAdresseByMitgliedsnummer(self.session_token, pid)
        )
        return result

    # 1.48.
    def get_bereitstellen_eingangsdokument_id(self):
        client = Client(self.BASE_URL + EDOK_SERVICE, transport=self.transport)
        result = serialize_object(
            client.service.rtvNewDokumentID(self.session_token)
        )
        return result

    # 1.60.
    def get_verifyRtvBerufskrankheitsFallByAktenzeichen(self, pid):
        client = Client(self.BASE_URL + RUL_SERVICE, transport=self.transport)
        result = serialize_object(
            client.service.verifyRtvBerufskrankheitsFallByAktenzeichen(self.session_token, pid)
        )
        return result

    # 1.64.
    def get_verifyVersicherungsfallIsArbeitsunfall(self, pid):
        client = Client(self.BASE_URL + RUL_SERVICE, transport=self.transport)
        #import pdb; pdb.set_trace()
        result = serialize_object(
            client.service.verifyVersicherungsfallIsArbeitsunfall(self.session_token, pid)
        )
        return result

    # 1.65.
    def get_rtvverifyVersicherungsfallIsBKFall(self, pid):
        client = Client(self.BASE_URL + RUL_SERVICE, transport=self.transport)
        result = serialize_object(
            client.service.verifyVersicherungsfallIsBKFall(self.session_token, pid)
        )
        return result

    # 1.67   RULS072
    def get_rtvListZugeordneteIKAdressen(self, pid):
        client = Client(self.BASE_URL + RUL_SERVICE, transport=self.transport)
        request_type = client.get_type('ns0:rtvListZugeordneteIKAdressen')
        constraint = client.get_type('ns1:listConstraint')(start=1, max=10, isOverflowAllowed=True)
        result = client.service.rtvListZugeordneteIKAdressen(
            sessionToken=self.session_token, versfallID=pid, listConstraint=constraint)
        return result

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
