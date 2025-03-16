from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="SpotifyObjectExternalUrl")


@_attrs_define
class SpotifyObjectExternalUrl:
    """
    Attributes:
        spotify (str):
    """

    spotify: str

    def to_dict(self) -> dict[str, Any]:
        spotify = self.spotify

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "spotify": spotify,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        spotify = d.pop("spotify")

        spotify_object_external_url = cls(
            spotify=spotify,
        )

        return spotify_object_external_url
