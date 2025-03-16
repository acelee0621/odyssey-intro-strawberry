from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="SpotifyRequestQueryParamsPUTMeshows")


@_attrs_define
class SpotifyRequestQueryParamsPUTMeshows:
    """
    Attributes:
        ids (str):
    """

    ids: str

    def to_dict(self) -> dict[str, Any]:
        ids = self.ids

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "ids": ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ids = d.pop("ids")

        spotify_request_query_params_put_meshows = cls(
            ids=ids,
        )

        return spotify_request_query_params_put_meshows
