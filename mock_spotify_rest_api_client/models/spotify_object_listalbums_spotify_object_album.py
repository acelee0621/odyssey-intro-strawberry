from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.spotify_object_album import SpotifyObjectAlbum


T = TypeVar("T", bound="SpotifyObjectListalbumsSpotifyObjectAlbum")


@_attrs_define
class SpotifyObjectListalbumsSpotifyObjectAlbum:
    """
    Attributes:
        albums (list['SpotifyObjectAlbum']):
    """

    albums: list["SpotifyObjectAlbum"]

    def to_dict(self) -> dict[str, Any]:
        albums = []
        for albums_item_data in self.albums:
            albums_item = albums_item_data.to_dict()
            albums.append(albums_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "albums": albums,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.spotify_object_album import SpotifyObjectAlbum

        d = dict(src_dict)
        albums = []
        _albums = d.pop("albums")
        for albums_item_data in _albums:
            albums_item = SpotifyObjectAlbum.from_dict(albums_item_data)

            albums.append(albums_item)

        spotify_object_listalbums_spotify_object_album = cls(
            albums=albums,
        )

        return spotify_object_listalbums_spotify_object_album
