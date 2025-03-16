from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SpotifyRequestQueryParamsGETBrowsenewReleases")


@_attrs_define
class SpotifyRequestQueryParamsGETBrowsenewReleases:
    """
    Attributes:
        country (Union[Unset, str]):
        limit (Union[Unset, float]):
        offset (Union[Unset, float]):
    """

    country: Union[Unset, str] = UNSET
    limit: Union[Unset, float] = UNSET
    offset: Union[Unset, float] = UNSET

    def to_dict(self) -> dict[str, Any]:
        country = self.country

        limit = self.limit

        offset = self.offset

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if country is not UNSET:
            field_dict["country"] = country
        if limit is not UNSET:
            field_dict["limit"] = limit
        if offset is not UNSET:
            field_dict["offset"] = offset

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        country = d.pop("country", UNSET)

        limit = d.pop("limit", UNSET)

        offset = d.pop("offset", UNSET)

        spotify_request_query_params_get_browsenew_releases = cls(
            country=country,
            limit=limit,
            offset=offset,
        )

        return spotify_request_query_params_get_browsenew_releases
