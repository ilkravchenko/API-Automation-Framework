import typing

import allure
from httpx import AsyncClient, Response
from httpx._client import UseClientDefault
from httpx._types import (
    AuthTypes,
    CookieTypes,
    HeaderTypes,
    QueryParamTypes,
    RequestContent,
    RequestData,
    RequestExtensions,
    RequestFiles,
    TimeoutTypes,
    URLTypes,
)


class HTTPClient(AsyncClient):

    @allure.step('Making GET request to "{url}"')
    async def get(
        self,
        url: URLTypes,
        *,
        params: typing.Optional[QueryParamTypes] = None,
        headers: typing.Optional[HeaderTypes] = None,
        cookies: typing.Optional[CookieTypes] = None,
        auth: typing.Union[AuthTypes, UseClientDefault] = None,
        follow_redirects: typing.Union[bool, UseClientDefault] = None,
        timeout: typing.Union[TimeoutTypes, UseClientDefault] = None,
        extensions: typing.Optional[RequestExtensions] = None
    ) -> Response:
        return await super().get(
            url=url,
            params=params,
            headers=headers,
            cookies=cookies,
            auth=auth,
            follow_redirects=follow_redirects,
            timeout=timeout,
            extensions=extensions
        )

    @allure.step('Making POST request to "{url}"')
    async def post(
        self,
        url: URLTypes,
        *,
        content: typing.Optional[RequestContent] = None,
        data: typing.Optional[RequestData] = None,
        files: typing.Optional[RequestFiles] = None,
        json: typing.Optional[typing.Any] = None,
        params: typing.Optional[QueryParamTypes] = None,
        headers: typing.Optional[HeaderTypes] = None,
        cookies: typing.Optional[CookieTypes] = None,
        auth: typing.Union[AuthTypes, UseClientDefault] = None,
        follow_redirects: typing.Union[bool, UseClientDefault] = None,
        timeout: typing.Union[TimeoutTypes, UseClientDefault] = None,
        extensions: typing.Optional[RequestExtensions] = None
    ) -> Response:
        return await super().post(
            url=url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            auth=auth,
            follow_redirects=follow_redirects,
            timeout=timeout,
            extensions=extensions
        )

    @allure.step('Making PATCH request to "{url}"')
    async def patch(
        self,
        url: URLTypes,
        *,
        content: typing.Optional[RequestContent] = None,
        data: typing.Optional[RequestData] = None,
        files: typing.Optional[RequestFiles] = None,
        json: typing.Optional[typing.Any] = None,
        params: typing.Optional[QueryParamTypes] = None,
        headers: typing.Optional[HeaderTypes] = None,
        cookies: typing.Optional[CookieTypes] = None,
        auth: typing.Union[AuthTypes, UseClientDefault] = None,
        follow_redirects: typing.Union[bool, UseClientDefault] = None,
        timeout: typing.Union[TimeoutTypes, UseClientDefault] = None,
        extensions: typing.Optional[RequestExtensions] = None
    ) -> Response:
        return await super().patch(
            url=url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            auth=auth,
            follow_redirects=follow_redirects,
            timeout=timeout,
            extensions=extensions
        )

    @allure.step('Making DELETE request to "{url}"')
    async def delete(
        self,
        url: URLTypes,
        *,
        params: typing.Optional[QueryParamTypes] = None,
        headers: typing.Optional[HeaderTypes] = None,
        cookies: typing.Optional[CookieTypes] = None,
        auth: typing.Union[AuthTypes, UseClientDefault] = None,
        follow_redirects: typing.Union[bool, UseClientDefault] = None,
        timeout: typing.Union[TimeoutTypes, UseClientDefault] = None,
        extensions: typing.Optional[RequestExtensions] = None
    ) -> Response:
        return await super().delete(
            url=url,
            params=params,
            headers=headers,
            cookies=cookies,
            auth=auth,
            follow_redirects=follow_redirects,
            timeout=timeout,
            extensions=extensions
        )


class APIClient:

    def __init__(self, client: HTTPClient) -> None:
        self._client = client

    @property
    def client(self) -> HTTPClient:
        return self._client
