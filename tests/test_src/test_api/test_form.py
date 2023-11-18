from typing import Any

from fastapi import status
from httpx import AsyncClient, Response

from src.enums.type_field import TypeField


class TestForm:
    url = '/api/form/validate'

    async def test__when_get__then__error_with_405(self, client: AsyncClient):
        response: Response = await client.get(url=self.url)

        expected_status = status.HTTP_405_METHOD_NOT_ALLOWED
        real_status = response.status_code

        assert expected_status == real_status

    async def test__when_put__then__error_with_405(self, client: AsyncClient):
        response: Response = await client.put(url=self.url, json={})

        expected_status = status.HTTP_405_METHOD_NOT_ALLOWED
        real_status = response.status_code

        assert expected_status == real_status

    async def test__when_patch__then__error_with_405(
        self,
        client: AsyncClient,
    ):
        response: Response = await client.patch(url=self.url, json={})

        expected_status = status.HTTP_405_METHOD_NOT_ALLOWED
        real_status = response.status_code

        assert expected_status == real_status

    async def test__when_delete__then__error_with_405(
        self,
        client: AsyncClient,
    ):
        response: Response = await client.delete(url=self.url)

        expected_status = status.HTTP_405_METHOD_NOT_ALLOWED
        real_status = response.status_code

        assert expected_status == real_status

    async def test__when_post_without_template__then__return_data_with_200(
        self,
        client: AsyncClient,
    ):
        data: dict[str, Any] = {
            'user_name': 'user_name',
            'user_birth_date': '10.10.2023',
            'user_birth_date_copy': '2023-12-10',
            'user_email': 'email@email.com',
            'user_phone': '+7 999 999 99 99',
        }

        response: Response = await client.post(url=self.url, json=data)

        expected_status = status.HTTP_200_OK
        real_status = response.status_code

        expected_data = {
            'user_name': TypeField.text,
            'user_birth_date': TypeField.date,
            'user_birth_date_copy': TypeField.date,
            'user_email': TypeField.email,
            'user_phone': TypeField.phone,
        }
        real_data = response.json()

        assert expected_status == real_status
        assert expected_data == real_data

    async def test__when_post_with_not_valid_data__then__return_data_with_200(
        self,
        client: AsyncClient,
    ):
        data: dict[str, Any] = {
            'user_birth_date': '10102023',
            'user_birth_date_copy': '20231210',
            'user_email': 'emailemail.com',
            'user_phone': '+79999999999',
        }

        response: Response = await client.post(url=self.url, json=data)

        expected_status = status.HTTP_200_OK
        real_status = response.status_code

        expected_data = {
            'user_birth_date': TypeField.text,
            'user_birth_date_copy': TypeField.text,
            'user_email': TypeField.text,
            'user_phone': TypeField.text,
        }
        real_data = response.json()

        assert expected_status == real_status
        assert expected_data == real_data

    async def test__when_post_with_user_template__then__return_template_name(
        self,
        client: AsyncClient,
        forms,
    ):
        data: dict[str, Any] = {
            'user_phone': '+7 999 999 99 99',
        }

        response: Response = await client.post(url=self.url, json=data)

        expected_status = status.HTTP_200_OK
        real_status = response.status_code

        expected_data = {
            'name': 'user_template',
        }
        real_data = response.json()

        assert expected_status == real_status
        assert expected_data == real_data

    async def test__when_post_with_order_template__then__return_template_name(
        self,
        client: AsyncClient,
        forms,
    ):
        data: dict[str, Any] = {
            'order_description': 'order_description',
            'order_date': '10.10.2020',
        }

        response: Response = await client.post(url=self.url, json=data)

        expected_status = status.HTTP_200_OK
        real_status = response.status_code

        expected_data = {
            'name': 'order_template',
        }
        real_data = response.json()

        assert expected_status == real_status
        assert expected_data == real_data
