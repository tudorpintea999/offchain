import pytest

from pytest_httpx import HTTPXMock

from offchain.metadata.adapters.base_adapter import AdapterConfig
from offchain.metadata.adapters import (
    ARWeaveAdapter,
    HTTPAdapter,
    IPFSAdapter,
)
from offchain.metadata.fetchers.metadata_fetcher import MetadataFetcher


class TestMetadataFetcher:
    def test_metadata_fetcher_register_adapter(self):  # type: ignore[no-untyped-def]
        fetcher = MetadataFetcher()
        adapter = IPFSAdapter()
        fetcher.register_adapter(adapter, "ipfs://")
        assert fetcher.sess.adapters.get("ipfs://") == adapter

    @pytest.mark.asyncio
    async def test_gen_fetch_data_adapter(self):  # type: ignore[no-untyped-def]
        fetcher = MetadataFetcher()
        content = await fetcher.gen_fetch_content(
            "data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzIwIiBoZWlnaHQ9IjMyMCIgdmlld0JveD0iMCAwIDMyMCAzMjAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgc2hhcGUtcmVuZGVyaW5nPSJjcmlzcEVkZ2VzIj48cmVjdCB3aWR0aD0iMTAwJSIgaGVpZ2h0PSIxMDAlIiBmaWxsPSIjZDVkN2UxIiAvPjxyZWN0IHdpZHRoPSIxMDAiIGhlaWdodD0iMTAiIHg9IjExMCIgeT0iMjYwIiBmaWxsPSIjZmU1MDBjIiAvPjxyZWN0IHdpZHRoPSIxMDAiIGhlaWdodD0iMTAiIHg9IjExMCIgeT0iMjcwIiBmaWxsPSIjZmU1MDBjIiAvPjxyZWN0IHdpZHRoPSIyMCIgaGVpZ2h0PSIxMCIgeD0iMTEwIiB5PSIyODAiIGZpbGw9IiNmZTUwMGMiIC8+PHJlY3Qgd2lkdGg9IjcwIiBoZWlnaHQ9IjEwIiB4PSIxNDAiIHk9IjI4MCIgZmlsbD0iI2ZlNTAwYyIgLz48cmVjdCB3aWR0aD0iMjAiIGhlaWdodD0iMTAiIHg9IjExMCIgeT0iMjkwIiBmaWxsPSIjZmU1MDBjIiAvPjxyZWN0IHdpZHRoPSI3MCIgaGVpZ2h0PSIxMCIgeD0iMTQwIiB5PSIyOTAiIGZpbGw9IiNmZTUwMGMiIC8+PHJlY3Qgd2lkdGg9IjIwIiBoZWlnaHQ9IjEwIiB4PSIxMTAiIHk9IjMwMCIgZmlsbD0iI2ZlNTAwYyIgLz48cmVjdCB3aWR0aD0iNzAiIGhlaWdodD0iMTAiIHg9IjE0MCIgeT0iMzAwIiBmaWxsPSIjZmU1MDBjIiAvPjxyZWN0IHdpZHRoPSIyMCIgaGVpZ2h0PSIxMCIgeD0iMTEwIiB5PSIzMTAiIGZpbGw9IiNmZTUwMGMiIC8+PHJlY3Qgd2lkdGg9IjcwIiBoZWlnaHQ9IjEwIiB4PSIxNDAiIHk9IjMxMCIgZmlsbD0iI2ZlNTAwYyIgLz48cmVjdCB3aWR0aD0iMzAiIGhlaWdodD0iMTAiIHg9IjE1MCIgeT0iMjYwIiBmaWxsPSIjZTVlNWRlIiAvPjxyZWN0IHdpZHRoPSIyMCIgaGVpZ2h0PSIxMCIgeD0iMTkwIiB5PSIyNjAiIGZpbGw9IiNlNWU1ZGUiIC8+PHJlY3Qgd2lkdGg9IjMwIiBoZWlnaHQ9IjEwIiB4PSIxMTAiIHk9IjI3MCIgZmlsbD0iI2U1ZTVkZSIgLz48cmVjdCB3aWR0aD0iMzAiIGhlaWdodD0iMTAiIHg9IjE1MCIgeT0iMjcwIiBmaWxsPSIjZTVlNWRlIiAvPjxyZWN0IHdpZHRoPSIyMCIgaGVpZ2h0PSIxMCIgeD0iMTkwIiB5PSIyNzAiIGZpbGw9IiNlNWU1ZGUiIC8+PHJlY3Qgd2lkdGg9IjIwIiBoZWlnaHQ9IjEwIiB4PSIxMTAiIHk9IjI4MCIgZmlsbD0iI2U1ZTVkZSIgLz48cmVjdCB3aWR0aD0iMzAiIGhlaWdodD0iMTAiIHg9IjE1MCIgeT0iMjgwIiBmaWxsPSIjZTVlNWRlIiAvPjxyZWN0IHdpZHRoPSIyMCIgaGVpZ2h0PSIxMCIgeD0iMTEwIiB5PSIyOTAiIGZpbGw9IiNlNWU1ZGUiIC8+PHJlY3Qgd2lkdGg9IjEwIiBoZWlnaHQ9IjEwIiB4PSIyMDAiIHk9IjI5MCIgZmlsbD0iI2U1ZTVkZSIgLz48cmVjdCB3aWR0aD0iMzAiIGhlaWdodD0iMTAiIHg9IjE2MCIgeT0iMzAwIiBmaWxsPSIjZTVlNWRlIiAvPjxyZWN0IHdpZHRoPSIxMCIgaGVpZ2h0PSIxMCIgeD0iMjAwIiB5PSIzMDAiIGZpbGw9IiNlNWU1ZGUiIC8+PHJlY3Qgd2lkdGg9IjEwIiBoZWlnaHQ9IjEwIiB4PSIxMjAiIHk9IjMxMCIgZmlsbD0iI2U1ZTVkZSIgLz48cmVjdCB3aWR0aD0iMTAiIGhlaWdodD0iMTAiIHg9IjE0MCIgeT0iMzEwIiBmaWxsPSIjZTVlNWRlIiAvPjxyZWN0IHdpZHRoPSIzMCIgaGVpZ2h0PSIxMCIgeD0iMTYwIiB5PSIzMTAiIGZpbGw9IiNlNWU1ZGUiIC8+PHJlY3Qgd2lkdGg9IjEwIiBoZWlnaHQ9IjEwIiB4PSIyMDAiIHk9IjMxMCIgZmlsbD0iI2U1ZTVkZSIgLz48cmVjdCB3aWR0aD0iMjAiIGhlaWdodD0iMTAiIHg9IjE1MCIgeT0iNzAiIGZpbGw9IiNmZmMxMTAiIC8+PHJlY3Qgd2lkdGg9IjIwIiBoZWlnaHQ9IjEwIiB4PSIxNTAiIHk9IjgwIiBmaWxsPSIjZmZjMTEwIiAvPjxyZWN0IHdpZHRoPSI0MCIgaGVpZ2h0PSIxMCIgeD0iMTQwIiB5PSI5MCIgZmlsbD0iI2ZmYzExMCIgLz48cmVjdCB3aWR0aD0iNDAiIGhlaWdodD0iMTAiIHg9IjE0MCIgeT0iMTAwIiBmaWxsPSIjZmZjMTEwIiAvPjxyZWN0IHdpZHRoPSI2MCIgaGVpZ2h0PSIxMCIgeD0iMTMwIiB5PSIxMTAiIGZpbGw9IiNkMDhiMTEiIC8+PHJlY3Qgd2lkdGg9IjYwIiBoZWlnaHQ9IjEwIiB4PSIxMzAiIHk9IjEyMCIgZmlsbD0iIzAwMDAwMCIgLz48cmVjdCB3aWR0aD0iMjAiIGhlaWdodD0iMTAiIHg9IjkwIiB5PSIxMzAiIGZpbGw9IiNmZmMxMTAiIC8+PHJlY3Qgd2lkdGg9IjIwIiBoZWlnaHQ9IjEwIiB4PSIxMTAiIHk9IjEzMCIgZmlsbD0iI2QwOGIxMSIgLz48cmVjdCB3aWR0aD0iMjAiIGhlaWdodD0iMTAiIHg9IjEzMCIgeT0iMTMwIiBmaWxsPSIjZmZjMTEwIiAvPjxyZWN0IHdpZHRoPSIyMCIgaGVpZ2h0PSIxMCIgeD0iMTUwIiB5PSIxMzAiIGZpbGw9IiNkMDhiMTEiIC8+PHJlY3Qgd2lkdGg9IjIwIiBoZWlnaHQ9IjEwIiB4PSIxNzAiIHk9IjEzMCIgZmlsbD0iI2ZmYzExMCIgLz48cmVjdCB3aWR0aD0iMjAiIGhlaWdodD0iMTAiIHg9IjE5MCIgeT0iMTMwIiBmaWxsPSIjZDA4YjExIiAvPjxyZWN0IHdpZHRoPSIyMCIgaGVpZ2h0PSIxMCIgeD0iMjEwIiB5PSIxMzAiIGZpbGw9IiNmZmMxMTAiIC8+PHJlY3Qgd2lkdGg9IjE0MCIgaGVpZ2h0PSIxMCIgeD0iOTAiIHk9IjE0MCIgZmlsbD0iIzAwMDAwMCIgLz48cmVjdCB3aWR0aD0iMTYwIiBoZWlnaHQ9IjEwIiB4PSI4MCIgeT0iMTUwIiBmaWxsPSIjZmZjOTI1IiAvPjxyZWN0IHdpZHRoPSIxNjAiIGhlaWdodD0iMTAiIHg9IjgwIiB5PSIxNjAiIGZpbGw9IiNmZmM5MjUiIC8+PHJlY3Qgd2lkdGg9IjE2MCIgaGVpZ2h0PSIxMCIgeD0iODAiIHk9IjE3MCIgZmlsbD0iI2ZmYzkyNSIgLz48cmVjdCB3aWR0aD0iMTYwIiBoZWlnaHQ9IjEwIiB4PSI4MCIgeT0iMTgwIiBmaWxsPSIjZmZjOTI1IiAvPjxyZWN0IHdpZHRoPSIxNjAiIGhlaWdodD0iMTAiIHg9IjgwIiB5PSIxOTAiIGZpbGw9IiNmZmM5MjUiIC8+PHJlY3Qgd2lkdGg9IjE2MCIgaGVpZ2h0PSIxMCIgeD0iODAiIHk9IjIwMCIgZmlsbD0iI2ZmYzkyNSIgLz48cmVjdCB3aWR0aD0iMTYwIiBoZWlnaHQ9IjEwIiB4PSI4MCIgeT0iMjEwIiBmaWxsPSIjZmZjOTI1IiAvPjxyZWN0IHdpZHRoPSIxNjAiIGhlaWdodD0iMTAiIHg9IjgwIiB5PSIyMjAiIGZpbGw9IiNmZmM5MjUiIC8+PHJlY3Qgd2lkdGg9IjIwIiBoZWlnaHQ9IjEwIiB4PSI4MCIgeT0iMjMwIiBmaWxsPSIjZmZjOTI1IiAvPjxyZWN0IHdpZHRoPSIzMCIgaGVpZ2h0PSIxMCIgeD0iMTAwIiB5PSIyMzAiIGZpbGw9IiNkMDhiMTEiIC8+PHJlY3Qgd2lkdGg9IjExMCIgaGVpZ2h0PSIxMCIgeD0iMTMwIiB5PSIyMzAiIGZpbGw9IiNmZmM5MjUiIC8+PHJlY3Qgd2lkdGg9IjQwIiBoZWlnaHQ9IjEwIiB4PSI4MCIgeT0iMjQwIiBmaWxsPSIjZmZjOTI1IiAvPjxyZWN0IHdpZHRoPSI0MCIgaGVpZ2h0PSIxMCIgeD0iMTIwIiB5PSIyNDAiIGZpbGw9IiNkMDhiMTEiIC8+PHJlY3Qgd2lkdGg9IjgwIiBoZWlnaHQ9IjEwIiB4PSIxNjAiIHk9IjI0MCIgZmlsbD0iI2ZmYzkyNSIgLz48cmVjdCB3aWR0aD0iMTYwIiBoZWlnaHQ9IjEwIiB4PSI4MCIgeT0iMjUwIiBmaWxsPSIjZmZjOTI1IiAvPjxyZWN0IHdpZHRoPSI4MCIgaGVpZ2h0PSIxMCIgeD0iODAiIHk9IjE0MCIgZmlsbD0iIzAwMDAwMCIgLz48cmVjdCB3aWR0aD0iODAiIGhlaWdodD0iMTAiIHg9IjE3MCIgeT0iMTQwIiBmaWxsPSIjMDAwMDAwIiAvPjxyZWN0IHdpZHRoPSIxMCIgaGVpZ2h0PSIxMCIgeD0iODAiIHk9IjE1MCIgZmlsbD0iIzAwMDAwMCIgLz48cmVjdCB3aWR0aD0iMjAiIGhlaWdodD0iMTAiIHg9IjkwIiB5PSIxNTAiIGZpbGw9IiNmZmZmZmYiIC8+PHJlY3Qgd2lkdGg9IjUwIiBoZWlnaHQ9IjEwIiB4PSIxMTAiIHk9IjE1MCIgZmlsbD0iIzAwMDAwMCIgLz48cmVjdCB3aWR0aD0iMTAiIGhlaWdodD0iMTAiIHg9IjE3MCIgeT0iMTUwIiBmaWxsPSIjMDAwMDAwIiAvPjxyZWN0IHdpZHRoPSIyMCIgaGVpZ2h0PSIxMCIgeD0iMTgwIiB5PSIxNTAiIGZpbGw9IiNmZmZmZmYiIC8+PHJlY3Qgd2lkdGg9IjUwIiBoZWlnaHQ9IjEwIiB4PSIyMDAiIHk9IjE1MCIgZmlsbD0iIzAwMDAwMCIgLz48cmVjdCB3aWR0aD0iMTAiIGhlaWdodD0iMTAiIHg9IjgwIiB5PSIxNjAiIGZpbGw9IiMwMDAwMDAiIC8+PHJlY3Qgd2lkdGg9IjIwIiBoZWlnaHQ9IjEwIiB4PSI5MCIgeT0iMTYwIiBmaWxsPSIjZmZmZmZmIiAvPjxyZWN0IHdpZHRoPSI1MCIgaGVpZ2h0PSIxMCIgeD0iMTEwIiB5PSIxNjAiIGZpbGw9IiMwMDAwMDAiIC8+PHJlY3Qgd2lkdGg9IjEwIiBoZWlnaHQ9IjEwIiB4PSIxNzAiIHk9IjE2MCIgZmlsbD0iIzAwMDAwMCIgLz48cmVjdCB3aWR0aD0iMjAiIGhlaWdodD0iMTAiIHg9IjE4MCIgeT0iMTYwIiBmaWxsPSIjZmZmZmZmIiAvPjxyZWN0IHdpZHRoPSI1MCIgaGVpZ2h0PSIxMCIgeD0iMjAwIiB5PSIxNjAiIGZpbGw9IiMwMDAwMDAiIC8+PHJlY3Qgd2lkdGg9IjQwIiBoZWlnaHQ9IjEwIiB4PSI1MCIgeT0iMTcwIiBmaWxsPSIjMDAwMDAwIiAvPjxyZWN0IHdpZHRoPSIyMCIgaGVpZ2h0PSIxMCIgeD0iOTAiIHk9IjE3MCIgZmlsbD0iI2ZmZmZmZiIgLz48cmVjdCB3aWR0aD0iNzAiIGhlaWdodD0iMTAiIHg9IjExMCIgeT0iMTcwIiBmaWxsPSIjMDAwMDAwIiAvPjxyZWN0IHdpZHRoPSIyMCIgaGVpZ2h0PSIxMCIgeD0iMTgwIiB5PSIxNzAiIGZpbGw9IiNmZmZmZmYiIC8+PHJlY3Qgd2lkdGg9IjUwIiBoZWlnaHQ9IjEwIiB4PSIyMDAiIHk9IjE3MCIgZmlsbD0iIzAwMDAwMCIgLz48cmVjdCB3aWR0aD0iMTAiIGhlaWdodD0iMTAiIHg9IjUwIiB5PSIxODAiIGZpbGw9IiMwMDAwMDAiIC8+PHJlY3Qgd2lkdGg9IjEwIiBoZWlnaHQ9IjEwIiB4PSI4MCIgeT0iMTgwIiBmaWxsPSIjMDAwMDAwIiAvPjxyZWN0IHdpZHRoPSIyMCIgaGVpZ2h0PSIxMCIgeD0iOTAiIHk9IjE4MCIgZmlsbD0iI2ZmZmZmZiIgLz48cmVjdCB3aWR0aD0iNTAiIGhlaWdodD0iMTAiIHg9IjExMCIgeT0iMTgwIiBmaWxsPSIjMDAwMDAwIiAvPjxyZWN0IHdpZHRoPSIxMCIgaGVpZ2h0PSIxMCIgeD0iMTcwIiB5PSIxODAiIGZpbGw9IiMwMDAwMDAiIC8+PHJlY3Qgd2lkdGg9IjIwIiBoZWlnaHQ9IjEwIiB4PSIxODAiIHk9IjE4MCIgZmlsbD0iI2ZmZmZmZiIgLz48cmVjdCB3aWR0aD0iNTAiIGhlaWdodD0iMTAiIHg9IjIwMCIgeT0iMTgwIiBmaWxsPSIjMDAwMDAwIiAvPjxyZWN0IHdpZHRoPSIxMCIgaGVpZ2h0PSIxMCIgeD0iNTAiIHk9IjE5MCIgZmlsbD0iIzAwMDAwMCIgLz48cmVjdCB3aWR0aD0iMTAiIGhlaWdodD0iMTAiIHg9IjgwIiB5PSIxOTAiIGZpbGw9IiMwMDAwMDAiIC8+PHJlY3Qgd2lkdGg9IjIwIiBoZWlnaHQ9IjEwIiB4PSI5MCIgeT0iMTkwIiBmaWxsPSIjZmZmZmZmIiAvPjxyZWN0IHdpZHRoPSI1MCIgaGVpZ2h0PSIxMCIgeD0iMTEwIiB5PSIxOTAiIGZpbGw9IiMwMDAwMDAiIC8+PHJlY3Qgd2lkdGg9IjEwIiBoZWlnaHQ9IjEwIiB4PSIxNzAiIHk9IjE5MCIgZmlsbD0iIzAwMDAwMCIgLz48cmVjdCB3aWR0aD0iMjAiIGhlaWdodD0iMTAiIHg9IjE4MCIgeT0iMTkwIiBmaWxsPSIjZmZmZmZmIiAvPjxyZWN0IHdpZHRoPSI1MCIgaGVpZ2h0PSIxMCIgeD0iMjAwIiB5PSIxOTAiIGZpbGw9IiMwMDAwMDAiIC8+PHJlY3Qgd2lkdGg9IjEwIiBoZWlnaHQ9IjEwIiB4PSI4MCIgeT0iMjAwIiBmaWxsPSIjMDAwMDAwIiAvPjxyZWN0IHdpZHRoPSIyMCIgaGVpZ2h0PSIxMCIgeD0iOTAiIHk9IjIwMCIgZmlsbD0iI2ZmZmZmZiIgLz48cmVjdCB3aWR0aD0iNTAiIGhlaWdodD0iMTAiIHg9IjExMCIgeT0iMjAwIiBmaWxsPSIjMDAwMDAwIiAvPjxyZWN0IHdpZHRoPSIxMCIgaGVpZ2h0PSIxMCIgeD0iMTcwIiB5PSIyMDAiIGZpbGw9IiMwMDAwMDAiIC8+PHJlY3Qgd2lkdGg9IjIwIiBoZWlnaHQ9IjEwIiB4PSIxODAiIHk9IjIwMCIgZmlsbD0iI2ZmZmZmZiIgLz48cmVjdCB3aWR0aD0iNTAiIGhlaWdodD0iMTAiIHg9IjIwMCIgeT0iMjAwIiBmaWxsPSIjMDAwMDAwIiAvPjxyZWN0IHdpZHRoPSI4MCIgaGVpZ2h0PSIxMCIgeD0iODAiIHk9IjIxMCIgZmlsbD0iIzAwMDAwMCIgLz48cmVjdCB3aWR0aD0iODAiIGhlaWdodD0iMTAiIHg9IjE3MCIgeT0iMjEwIiBmaWxsPSIjMDAwMDAwIiAvPjwvc3ZnPg=="  # noqa
        )
        assert content is not None

    @pytest.mark.asyncio
    async def test_gen_fetch_ipfs_adapter(self):  # type: ignore[no-untyped-def]
        fetcher = MetadataFetcher()
        content = await fetcher.gen_fetch_content(
            "ipfs://bafkreiboyxwytfyufln3uzyzaixslzvmrqs5ezjo2cio2fymfqf6u57u6u"  # noqa
        )
        assert content is not None

    @pytest.mark.asyncio
    async def test_gen_fetch_arweave_adapter(self):  # type: ignore[no-untyped-def]
        fetcher = MetadataFetcher()
        content = await fetcher.gen_fetch_content(
            "ar://-G92LjB-wFj-FCGx040NgniW_Ypy_Cbh3Jq1HUD6l7A"  # noqa
        )
        assert content is not None

    @pytest.mark.asyncio
    async def test_gen_fetch_base_adapter(self):  # type: ignore[no-untyped-def]
        fetcher = MetadataFetcher()
        content = await fetcher.gen_fetch_content(
            "https://meta.sadgirlsbar.io/8403.json"  # noqa
        )
        assert content is not None

    @pytest.mark.asyncio
    async def test_gen_fetch_mime_type_and_size(self):  # type: ignore[no-untyped-def]
        fetcher = MetadataFetcher()
        result = await fetcher.gen_fetch_mime_type_and_size(
            "https://ipfs.io/ipfs/QmQaYaf3Q2oCBaUfUvV6mBP58EjbUTbMk6dC1o4YGjeWCo"
        )
        assert result == ("image/png", "2887641")  # type: ignore[comparison-overlap]
        print(result)

    @pytest.mark.asyncio
    async def test_gen_fetch_mime_type_and_size_http(self, httpx_mock: HTTPXMock):  # type: ignore[no-untyped-def]
        expected_headers = {"content-type": "image/png", "content-length": "99639"}
        httpx_mock.add_response(method="HEAD", headers=expected_headers)
        fetcher = MetadataFetcher()
        result = await fetcher.gen_fetch_mime_type_and_size(
            "https://d4ldbtmwfs9ii.cloudfront.net/7273.png"  # noqa
        )
        assert result == (
            expected_headers["content-type"],
            expected_headers["content-length"],
        )

    @pytest.mark.asyncio
    async def test_gen_fetch_mime_type_and_size_ipfs(self, httpx_mock: HTTPXMock):  # type: ignore[no-untyped-def]
        expected_headers = {"content-type": "image/png", "content-length": "1251767"}
        httpx_mock.add_response(method="HEAD", headers=expected_headers)
        fetcher = MetadataFetcher()
        result = await fetcher.gen_fetch_mime_type_and_size(
            "ipfs://QmV4MseQF2QDDYbmxtg7eEQ9vMuYNntPQrR3arXHnK4yGX/150.png"
        )
        assert result == (
            expected_headers["content-type"],
            expected_headers["content-length"],
        )

    @pytest.mark.asyncio
    async def test_gen_fetch_mime_type_and_size_arweave(self, httpx_mock: HTTPXMock):  # type: ignore[no-untyped-def]
        expected_headers = {"content-type": "image/png", "content-length": "235779"}
        httpx_mock.add_response(method="HEAD", headers=expected_headers)
        fetcher = MetadataFetcher()
        result = await fetcher.gen_fetch_mime_type_and_size(
            "ar://veLMprs2c--Rl6nXCeakR5FG9K8y4WXt62iLxayrflo/1032.png"
        )
        assert result == (
            expected_headers["content-type"],
            expected_headers["content-length"],
        )

    @pytest.mark.asyncio
    async def test_gen_fetch_mime_type_and_size_data(self):  # type: ignore[no-untyped-def]
        expected_headers = {"content-type": "image/svg+xml", "content-length": "1853"}
        fetcher = MetadataFetcher()
        result = await fetcher.gen_fetch_mime_type_and_size(
            "data:image/svg+xml;base64,PHN2ZyBpZD0iaDNpNXR6IiB2aWV3Qm94PSIwIDAgNDggNDgiIHdpZHRoPSIxMDAlIiBoZWlnaHQ9IjEwMCUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHZlcnNpb249IjEuMSIgPgoKPGltYWdlIHg9IjAiIHk9IjAiIHdpZHRoPSI0OCIgaGVpZ2h0PSI0OCIgaW1hZ2UtcmVuZGVyaW5nPSJwaXhlbGF0ZWQiIHByZXNlcnZlQXNwZWN0UmF0aW89InhNaWRZTWlkIiB4bGluazpocmVmPSJkYXRhOmltYWdlL3BuZztiYXNlNjQsaVZCT1J3MEtHZ29BQUFBTlNVaEVVZ0FBQUZBQUFBQlFDQU1BQUFDNXp3S2ZBQUFBWUZCTVZFVlFZWHIveUFFK1QxNy9rZ0I0YVdJUkVST3RwcHNhSGl3QUFBQVhtc3pKeGJ4MFhCUndxY2IvN2dKbGJIOWZiNGE1NWQ3L3RBRFBsdzFyWEZmOTVpMFBEQXVBa3F5bGhqTFQ4KzdLeU1jL1BUamh3ai8yeHk0VmFvcU1yc0t4MTlDSW1CMllBQUFENUVsRVFWUjRBZTJVaVpLak9CQkVzUllKdWZFMUFsbzJxSGYrL3k4M2xTQUt4Z1NodnZaKzl1QjB0WGxSTlFVVXh4dzBPZWJ3VndqZnRQYXRjNjJuOHROQ3JmczJ1RGJpUXFYMXA0VlYxWWVCd3VDSHZxbytLOVFoQk9kYmp1emNFSUwrckhCd2JoYUNyeEhDQ0w1VzZCeU1meFBoMjRwbjRmcnZHVUt0dXlYWXNnanhwVnVpZFphd1hLSjFQL2cyNG9laDBsMjVKRmRvU29NM1hnME9UU08zWHNNcUQvekZ4NFR4UkVLWENKdHM0V0NDTVVOOEJZUE1aUHhjR0ppWU00V3RPWnVoTlhpZERUTFRNSnhUb1dYQnhFS204R0VleHNURFN6dzhYaGI1bDBKMmg2M0JtNzFJUTVLSHVmRFJwVWpoZzF2ZW90bW81QXFiYkRLRm9OTnJ1bzBLeUJJU3JWNWVTdklTa2ZoSXNWTkhJVk40dTkvdm8xRGlnL0VEd2g1YnZOOXV0OUtBcmZpUkRwdXlhV0piaHBFalB3eHFqQjhRR2hLRkVwa1l1MG9wdFNWVUU4ZlQ4U1FaUWdGM1dZb1BrMkxYRjBYQnM4YVhPaDFWcEpoUXNhb3VCSm4vaDhTQXJZZ09TVExDemRObllheE9RdVNNTGZmcFBPbVF3bGVDRG9HNi9IN0JHNWxDN3BOQ2lZOFVPeVhuUlJSUGx3N1hRcFV4OGxxb2tFUjRuWVZFcVNJS2Nha0FXaHJDeUNLRWFlVGtROXdhbWVDdjNMS1p0N3dSSUdRanlRZHcrdWJJcXNnU3lzajAwWTdUeDdRV29tdU0vSXhlOElzUUNXOEl0MGFtVUsyYll0VGxqT2JJWUMza3lQWUpyZTBtdXJ6ZDd2RXl2RVdoQnJOd1JJRTlZZmNrL0hrREN5R2FJbHBYVlRVSlgrMTV4dHJ4T0grZUZ5UWhMMnh0dXFydm81Q2QxYlgzM3RweEtmWXdBd09QbHJYeFk5M2g2R09IVVFnWHNiWHRPdS8xaFVJNVAwTkkzOCtGOEFRZ3JQRjNYMWZUbHUwUE1BcW53QUkvVmtMNjBLV01EQ0ZNdnF2eHo5WTloSkYwdnFLUWlQQjVLVEx5cTZvNnVHcThmVHpPUWs1STRVSGd5SW5uTFhOa0gyMzFBVG9MMUNXTi9Cc1loUWdhVEFVZUU3TGxKTFNqejBaaHo1dDVzOE9kcFNRbW9jZWM0T0FHNSsxOFlZTjFoeFpJaDV1WERaZGlhL2JYTzNEQXpKT1FJK2NMNmJ1elE0ditJaitDRFhYd2ZubzQ3SGU0WUxwc1pDbnNUOGVKd3dGeEpSenBsTjFsTGJSUmlONEc2MXpnYmdyWjhqc3BTN3ZBKytDQ0NLWERmTFJlQ2V2Z1hBMm1od01XdmZ1UTRRMXVsMVg1RXJIOVdRY0lBWVNLdTk2OS9KTHdJSnlYMzZ3N09EY0tMVnp3dldVTDdlSTNFZ2JzcEZvSXdlNURCc0tOb2xMekl3cjlVamNKSXhTU2ZTRklGbmxFMWRRUlcwenNQMlE0OHJwS0lkTzJjUGNoQStIcTYvZ2J1YjNxbWI1SVpDeEZPSUJWaHdrdnd0MW5Bb1NwdU5laGw0RnpoWUpkQ24yMDRTQSt0U0VVWnFGVXJRaVpjRWltQ2Z0dVlKQzBnZnhxZzJMMUlSYUpHK1FJcDArUmZLOVFGZC9GRlUvWjYrWDZQaTQ0YTVtRmExRjlNZjhML3hmK0hZUi9BRVJPMzlYOE5Fb1VBQUFBQUVsRlRrU3VRbUNDIi8+Cgo8L3N2Zz4="  # noqa
        )
        assert result == (
            expected_headers["content-type"],
            expected_headers["content-length"],
        )

    @pytest.mark.asyncio
    async def test_gen_async_adapter(self, httpx_mock: HTTPXMock):
        ADAPTER_CONFIGS: list[AdapterConfig] = [
            AdapterConfig(
                adapter_cls=ARWeaveAdapter,
                mount_prefixes=["ar://"],
                host_prefixes=["https://arweave.net/"],
            ),
            AdapterConfig(
                adapter_cls=IPFSAdapter,
                mount_prefixes=[
                    "ipfs://",
                    "https://gateway.pinata.cloud/",
                    "https://ipfs.io/",
                ],
                host_prefixes=["https://gateway.pinata.cloud/ipfs/"],
            ),
            AdapterConfig(
                adapter_cls=HTTPAdapter,
                mount_prefixes=["https://", "http://"],
            ),
        ]

        ARWEAVE_URI = "ar://-G92LjB-wFj-FCGx040NgniW_Ypy_Cbh3Jq1HUD6l7A"
        IPFS_URIs = [
            "ipfs://bafkreiboyxwytfyufln3uzyzaixslzvmrqs5ezjo2cio2fymfqf6u57u6u",
            "https://gateway.pinata.cloud/ipfs/QmY3Lz7DfQPtPkK4n5StZcqc2zA6cmJC7wcAgzYXvGQLGm/485",
            "https://ipfs.io/ipfs/QmQaYaf3Q2oCBaUfUvV6mBP58EjbUTbMk6dC1o4YGjeWCo",
        ]
        HTTPS_URI = "https://ipfs.decentralized-content.com/ipfs/QmY3Lz7DfQPtPkK4n5StZcqc2zA6cmJC7wcAgzYXvGQLGm/485"
        fetcher = MetadataFetcher(async_adapter_configs=ADAPTER_CONFIGS)

        assert isinstance(
            fetcher._get_async_adapter_for_uri(ARWEAVE_URI), ARWeaveAdapter
        )
        for IPFS_URI in IPFS_URIs:
            assert isinstance(fetcher._get_async_adapter_for_uri(IPFS_URI), IPFSAdapter)
            assert isinstance(fetcher._get_async_adapter_for_uri(IPFS_URI), IPFSAdapter)
            assert isinstance(fetcher._get_async_adapter_for_uri(IPFS_URI), IPFSAdapter)
        assert isinstance(fetcher._get_async_adapter_for_uri(HTTPS_URI), HTTPAdapter)
