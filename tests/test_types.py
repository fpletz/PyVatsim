import pathlib
import pytest
from pydantic import ValidationError

from pyvatsim.types import VatsimData, VatsimEndpoints


def read_file_fixture(request, fn):
    file = pathlib.Path(request.node.fspath.strpath)
    with file.with_name(fn).open() as f:
        return f.read()


@pytest.fixture
def status_json(request):
    return read_file_fixture(request, "status.json")


def test_fails_on_wrong_data():
    with pytest.raises(ValidationError):
        VatsimData.model_validate_json('{"foo":"bar"}')


def test_validates_status_json(status_json):
    VatsimEndpoints.model_validate_json(status_json)
