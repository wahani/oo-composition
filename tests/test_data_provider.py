import pytest
from composition.data_provider import DataProvider


@pytest.fixture
def data_provider():
    return DataProvider()


class Test_DataProvider():

    def test_provider_dataset(self, data_provider):
        # act
        res = data_provider.provider_dataset
        # assert
        assert res.shape == [2, 2]

    def test_summarize(self, data_provider):
        # act
        res = data_provider.summarize
        # assert
        assert res.iloc[0,
                        0] == data_provider.provider_dataset.iloc[:, 0].mean()
        assert res.iloc[0,
                        1] == data_provider.provider_dataset.iloc[:, 1].mean()

    def test_summarize_rounded(self, data_provider):
        # act
        res = data_provider.summarize_rounded
        # assert
        assert res.iloc[0, 0] == data_provider.provider_dataset.iloc[:, 0].mean().round(
            0)
        assert res.iloc[0, 1] == data_provider.provider_dataset.iloc[:, 1].mean().round(
            0)
