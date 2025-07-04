# This file was auto-generated by Fern from our API Definition.

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.stripe_webhook_response import StripeWebhookResponse
from .raw_client import AsyncRawWebhooksClient, RawWebhooksClient


class WebhooksClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawWebhooksClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawWebhooksClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawWebhooksClient
        """
        return self._raw_client

    def handle_stripe(
        self, *, stripe_signature: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> StripeWebhookResponse:
        """
        Handle Stripe webhook events.

        This endpoint receives webhook events from Stripe and updates the billing records.

        Parameters
        ----------
        stripe_signature : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StripeWebhookResponse
            Successful Response

        Examples
        --------
        from mirascope import Lilypad

        client = Lilypad(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.webhooks.handle_stripe()
        """
        _response = self._raw_client.handle_stripe(stripe_signature=stripe_signature, request_options=request_options)
        return _response.data


class AsyncWebhooksClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawWebhooksClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawWebhooksClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawWebhooksClient
        """
        return self._raw_client

    async def handle_stripe(
        self, *, stripe_signature: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> StripeWebhookResponse:
        """
        Handle Stripe webhook events.

        This endpoint receives webhook events from Stripe and updates the billing records.

        Parameters
        ----------
        stripe_signature : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StripeWebhookResponse
            Successful Response

        Examples
        --------
        import asyncio

        from mirascope import AsyncLilypad

        client = AsyncLilypad(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.webhooks.handle_stripe()


        asyncio.run(main())
        """
        _response = await self._raw_client.handle_stripe(
            stripe_signature=stripe_signature, request_options=request_options
        )
        return _response.data
