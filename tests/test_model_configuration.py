
import pytest
from mkt.models import Marketplace

@pytest.mark.django_db
def test_configuration_model():
    marketplace = Marketplace(name='test',
                              description="testing",
                              contact_phone="234353435",
                              contact_email="victor@gmail.com",
                              technical_manager='hugo')
    marketplace.save()
    assert marketplace.name == "test"
    assert marketplace.description == "testing"
    assert marketplace.contact_phone == "234353435"
    assert marketplace.contact_email == "victor@gmail.com"
    assert marketplace.technical_manager == "hugo"

    assert str(marketplace) == marketplace.name
