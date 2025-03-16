from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.spotify_response_delete_playlistsidtracks import (
        SpotifyResponseDELETEPlaylistsidtracks,
    )


T = TypeVar("T", bound="SpotifyResponseDELETE")


@_attrs_define
class SpotifyResponseDELETE:
    """
    Attributes:
        playlistsidtracks (SpotifyResponseDELETEPlaylistsidtracks):
    """

    playlistsidtracks: "SpotifyResponseDELETEPlaylistsidtracks"

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
        from ..models.spotify_response_delete_playlistsidtracks import (
            SpotifyResponseDELETEPlaylistsidtracks,
        )

        d = dict(src_dict)
        playlistsidtracks = SpotifyResponseDELETEPlaylistsidtracks.from_dict(
            d.pop("/playlists/:id/tracks")
        )

        spotify_response_delete = cls(
            playlistsidtracks=playlistsidtracks,
        )

        return spotify_response_delete
