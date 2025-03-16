from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SpotifyRequestQueryParamsGETPlaylistsid")


@_attrs_define
class SpotifyRequestQueryParamsGETPlaylistsid:
    """
    Attributes:
        additional_types (Union[Unset, str]):
        fields (Union[Unset, str]):
        market (Union[Unset, str]):
    """

    additional_types: Union[Unset, str] = UNSET
    fields: Union[Unset, str] = UNSET
    market: Union[Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        additional_types = self.additional_types

        fields = self.fields

        market = self.market

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if additional_types is not UNSET:
            field_dict["additional_types"] = additional_types
        if fields is not UNSET:
            field_dict["fields"] = fields
        if market is not UNSET:
            field_dict["market"] = market

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        additional_types = d.pop("additional_types", UNSET)

        fields = d.pop("fields", UNSET)

        market = d.pop("market", UNSET)

        spotify_request_query_params_get_playlistsid = cls(
            additional_types=additional_types,
            fields=fields,
            market=market,
        )

        return spotify_request_query_params_get_playlistsid
