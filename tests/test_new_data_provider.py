import pytest
from composition.new_data_provider import NewDataProvider
from composition.data_provider import DataProvider


@pytest.fixture
def new_data_provider():
    return NewDataProvider()


class Test_NewDataProviderClass:
    def test_summarize(self, new_data_provider):
        # act
        res = new_data_provider.summarize()
        # assert
        assert (res == DataProvider().provider_dataset.merge(
            new_data_provider.new_provider_dataset)).all(
            axis=None)

    def test_summarize_rounded(self, new_data_provider):
        # assert
        with pytest.raises(ValueError):
            new_data_provider.summarize_rounded()
