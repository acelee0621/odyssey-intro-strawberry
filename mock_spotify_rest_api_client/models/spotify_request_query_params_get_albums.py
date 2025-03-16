from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SpotifyRequestQueryParamsGETAlbums")


@_attrs_define
class SpotifyRequestQueryParamsGETAlbums:
    """
    Attributes:
        ids (str):
        market (Union[Unset, str]):
    """

    ids: str
    market: Union[Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        ids = self.ids

        market = self.market

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "ids": ids,
            }
        )
        if market is not UNSET:
            field_dict["market"] = market

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ids = d.pop("ids")

        market = d.pop("market", UNSET)

        spotify_request_query_params_get_albums = cls(
            ids=ids,
            market=market,
        )

        return spotify_request_query_params_get_albums
