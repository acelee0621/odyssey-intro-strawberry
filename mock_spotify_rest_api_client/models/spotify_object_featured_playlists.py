from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.spotify_object_paginated_spotify_object_playlist_simplified import (
        SpotifyObjectPaginatedSpotifyObjectPlaylistSimplified,
    )


T = TypeVar("T", bound="SpotifyObjectFeaturedPlaylists")


@_attrs_define
class SpotifyObjectFeaturedPlaylists:
    """
    Attributes:
        message (str):
        playlists (SpotifyObjectPaginatedSpotifyObjectPlaylistSimplified):
    """

    message: str
    playlists: "SpotifyObjectPaginatedSpotifyObjectPlaylistSimplified"

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        playlists = self.playlists.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "message": message,
                "playlists": playlists,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.spotify_object_paginated_spotify_object_playlist_simplified import (
            SpotifyObjectPaginatedSpotifyObjectPlaylistSimplified,
        )

        d = dict(src_dict)
        message = d.pop("message")

        playlists = SpotifyObjectPaginatedSpotifyObjectPlaylistSimplified.from_dict(
            d.pop("playlists")
        )

        spotify_object_featured_playlists = cls(
            message=message,
            playlists=playlists,
        )

        return spotify_object_featured_playlists
