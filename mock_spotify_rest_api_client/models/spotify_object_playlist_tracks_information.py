from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="SpotifyObjectPlaylistTracksInformation")


@_attrs_define
class SpotifyObjectPlaylistTracksInformation:
    """
    Attributes:
        href (str):
        total (float):
    """

    href: str
    total: float

    def to_dict(self) -> dict[str, Any]:
        href = self.href

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "href": href,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        href = d.pop("href")

        total = d.pop("total")

        spotify_object_playlist_tracks_information = cls(
            href=href,
            total=total,
        )

        return spotify_object_playlist_tracks_information
