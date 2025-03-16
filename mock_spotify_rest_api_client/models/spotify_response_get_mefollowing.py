from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.spotify_object_paginated_cursor_based_spotify_object_artist import (
        SpotifyObjectPaginatedCursorBasedSpotifyObjectArtist,
    )


T = TypeVar("T", bound="SpotifyResponseGETMefollowing")


@_attrs_define
class SpotifyResponseGETMefollowing:
    """
    Attributes:
        artists (SpotifyObjectPaginatedCursorBasedSpotifyObjectArtist):
    """

    artists: "SpotifyObjectPaginatedCursorBasedSpotifyObjectArtist"

    def to_dict(self) -> dict[str, Any]:
        artists = self.artists.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "artists": artists,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.spotify_object_paginated_cursor_based_spotify_object_artist import (
            SpotifyObjectPaginatedCursorBasedSpotifyObjectArtist,
        )

        d = dict(src_dict)
        artists = SpotifyObjectPaginatedCursorBasedSpotifyObjectArtist.from_dict(
            d.pop("artists")
        )

        spotify_response_get_mefollowing = cls(
            artists=artists,
        )

        return spotify_response_get_mefollowing
