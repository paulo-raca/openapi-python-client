from http import HTTPStatus
from typing import Any, Dict, List, Optional, cast

import httpx

from ...client import Client
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/tests/basic_lists/floats".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[float]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = cast(List[float], response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[float]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
) -> Response[List[float]]:
    """Get Basic List Of Floats

     Get a list of floats

    Returns:
        Response[List[float]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
) -> Optional[List[float]]:
    """Get Basic List Of Floats

     Get a list of floats

    Returns:
        Response[List[float]]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
) -> Response[List[float]]:
    """Get Basic List Of Floats

     Get a list of floats

    Returns:
        Response[List[float]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
) -> Optional[List[float]]:
    """Get Basic List Of Floats

     Get a list of floats

    Returns:
        Response[List[float]]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
