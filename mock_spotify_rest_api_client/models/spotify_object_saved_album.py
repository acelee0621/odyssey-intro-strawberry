from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.spotify_object_album import SpotifyObjectAlbum


T = TypeVar("T", bound="SpotifyObjectSavedAlbum")


@_attrs_define
class SpotifyObjectSavedAlbum:
    """
    Attributes:
        added_at (str):
        album (SpotifyObjectAlbum):
    """

    added_at: str
    album: "SpotifyObjectAlbum"

    def to_dict(self) -> dict[str, Any]:
        added_at = self.added_at

        album = self.album.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "added_at": added_at,
                "album": album,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.spotify_object_album import SpotifyObjectAlbum

        d = dict(src_dict)
        added_at = d.pop("added_at")

        album = SpotifyObjectAlbum.from_dict(d.pop("album"))

        spotify_object_saved_album = cls(
            added_at=added_at,
            album=album,
        )

        return spotify_object_saved_album
