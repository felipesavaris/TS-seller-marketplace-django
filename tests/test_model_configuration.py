
import pytest
from mkt.models import Configuration

@pytest.mark.django_db
def test_configuration_model():
    configuration = Configuration(endpoint="https://www.google.com/",
                                  secret_key="234353435",
                                  apis="https://www.google.com/")
    configuration.save()
    assert configuration.endpoint == "https://www.google.com/"
    assert configuration.secret_key == "234353435"
    assert configuration.apis == "https://www.google.com/"
    assert str(configuration) == configuration.secret_key
