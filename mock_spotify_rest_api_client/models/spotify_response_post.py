from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.spotify_response_post_playlistsidtracks import (
        SpotifyResponsePOSTPlaylistsidtracks,
    )


T = TypeVar("T", bound="SpotifyResponsePOST")


@_attrs_define
class SpotifyResponsePOST:
    """
    Attributes:
        playlistsidtracks (SpotifyResponsePOSTPlaylistsidtracks):
    """

    playlistsidtracks: "SpotifyResponsePOSTPlaylistsidtracks"

    def to_dict(self) -> dict[str, Any]:
        playlistsidtracks = self.playlistsidtracks.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "/playlists/:id/tracks": playlistsidtracks,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.spotify_response_post_playlistsidtracks import (
            SpotifyResponsePOSTPlaylistsidtracks,
        )

        d = dict(src_dict)
        playlistsidtracks = SpotifyResponsePOSTPlaylistsidtracks.from_dict(
            d.pop("/playlists/:id/tracks")
        )

        spotify_response_post = cls(
            playlistsidtracks=playlistsidtracks,
        )

        return spotify_response_post
