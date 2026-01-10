import pytest
from app.config import get_base_url


@pytest.mark.smoke
def test_env_dev():
    assert "dev" in get_base_url("dev")


@pytest.mark.regression
@pytest.mark.parametrize("env", ["uat", "prod"])
def test_env_known(env):
    assert env in get_base_url(env)


@pytest.mark.regression
def test_env_unknown():
    with pytest.raises(ValueError):
        get_base_url("something else")
