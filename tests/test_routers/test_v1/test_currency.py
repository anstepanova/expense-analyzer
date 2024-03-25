"""Tests for currency endpoints."""

import pytest
from fastapi import status


class TestCurrency:
    """Tests for currency endpoints."""

    PATH = '/v1/currency'
    """Path to create and retrieve all endpoints."""
    PATH_TO_ITEM = '/v1/currency/{currency_id}'
    """Path to endpoints which work with one item."""

    @pytest.mark.parametrize('item_id', [1, 2, 3, 100, 1000])
    def test_get_currency_item_by_id(self, test_client, item_id):
        """Tests getting currency item by id :param test_client: test_client
        fixture :param item_id: item_id of currency which have to be read
        :return: None."""

        response = test_client.get(self.PATH_TO_ITEM.format(currency_id=item_id))
        assert response.status_code == status.HTTP_200_OK, response.json()

    @pytest.mark.parametrize(
        'item_data', [
            {
                'name': 'usd',
                'exchange_rate_to_nominate_currency': 1,
            },
            {
                'name': 'eur',
                'exchange_rate_to_nominate_currency': 0.91,
            },
            {
                'name': 'gbp',
                'exchange_rate_to_nominate_currency': 0.78,
            },
        ],
    )
    def test_create_currency_item(self, test_client, item_data):
        """Tests creating currency item with given data :param test_client:

        test_client fixture
        :param item_data: data for new currency item
        :return: None.
        """
        response = test_client.post(self.PATH, data=item_data)
        assert response.status_code == status.HTTP_201_CREATED, response.json()

    @pytest.mark.parametrize(
        'old_item_data, new_item_data', [
            (
                    {
                        'name': 'usd',
                        'exchange_rate_to_nominate_currency': 1,
                    },
                    {
                        'name': 'USD',
                        'exchange_rate_to_nominate_currency': 1,
                    },
            ),
            (
                    {
                        'name': 'usd',
                        'exchange_rate_to_nominate_currency': 1,
                    },
                    {
                        'name': 'USD',
                    },
            ),
            (
                    {
                        'name': 'eur',
                        'exchange_rate_to_nominate_currency': 0.91,
                    },
                    {
                        'name': 'EUR',
                        'exchange_rate_to_nominate_currency': 0.92,
                    },
            ),
            (
                    {
                        'name': 'eur',
                        'exchange_rate_to_nominate_currency': 1,
                    },
                    {
                        'exchange_rate_to_nominate_currency': 0.92,
                    },
            ),
        ],
    )
    def test_patch_currency_item(self, test_client, old_item_data, new_item_data):
        """Tests creating and updating currency item with given data :param
        test_client: test_client fixture :param old_item_data: data for
        creating new currency item :param new_item_data: data for updating the
        created currency item :return: None."""
        created_response = test_client.post(self.PATH, data=old_item_data)
        assert created_response.status_code == status.HTTP_200_OK, created_response.json()
        created_data = created_response.json()
        assert 'id' in created_data, created_data
        assert created_data.get('id') is not None
        patch_response = test_client.patch(
            self.PATH_TO_ITEM.format(currency_id=created_data.get('id')),
            data=new_item_data,
        )
        assert patch_response.status_code == status.HTTP_200_OK, patch_response.json()

    def test_delete_currency_item(self, test_client):
        """Tests deleting currency item :param test_client: test_client fixture
        :return: None."""

    def test_get_all_currency_item(self, test_client):
        """Tests getting all currency item :param test_client: test_client
        fixture :return: None."""
