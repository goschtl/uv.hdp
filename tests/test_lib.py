from uv.hdp.lib import TCusaWebService
from uv.models import models


cws = TCusaWebService("/Users/ck/work/hdp/uvc_hdpws/uvc_hdpws/data/")


def test_vp():
    person = cws.get_person_by_id("33")
    assert isinstance(person, models.VersichertePerson) is True


def test_unternehmen():
    unternehmen = cws.get_unternehmen_by_mnr("33")
    assert isinstance(unternehmen, models.Unternehmen) is True


def test_versichertenfall():
    fall = cws.get_versicherungsfall_by_id("33")
    assert isinstance(fall, models.VersichertenFall) is True
