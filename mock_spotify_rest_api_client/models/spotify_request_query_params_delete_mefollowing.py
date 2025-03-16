from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.spotify_request_query_params_delete_mefollowing_type import (
    SpotifyRequestQueryParamsDELETEMefollowingType,
)

T = TypeVar("T", bound="SpotifyRequestQueryParamsDELETEMefollowing")


@_attrs_define
class SpotifyRequestQueryParamsDELETEMefollowing:
    """
    Attributes:
        ids (str):
        type_ (SpotifyRequestQueryParamsDELETEMefollowingType):
    """

    ids: str
    type_: SpotifyRequestQueryParamsDELETEMefollowingType

    def to_dict(self) -> dict[str, Any]:
        ids = self.ids

        type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "ids": ids,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ids = d.pop("ids")

        type_ = SpotifyRequestQueryParamsDELETEMefollowingType(d.pop("type"))

        spotify_request_query_params_delete_mefollowing = cls(
            ids=ids,
            type_=type_,
        )

        return spotify_request_query_params_delete_mefollowing
