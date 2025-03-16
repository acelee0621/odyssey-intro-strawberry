from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.spotify_request_body_params_post_playlistsidtracks import (
        SpotifyRequestBodyParamsPOSTPlaylistsidtracks,
    )


T = TypeVar("T", bound="SpotifyRequestBodyParamsPOST")


@_attrs_define
class SpotifyRequestBodyParamsPOST:
    """
    Attributes:
        playlistsidtracks (SpotifyRequestBodyParamsPOSTPlaylistsidtracks):
    """

    playlistsidtracks: "SpotifyRequestBodyParamsPOSTPlaylistsidtracks"

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
        from ..models.spotify_request_body_params_post_playlistsidtracks import (
            SpotifyRequestBodyParamsPOSTPlaylistsidtracks,
        )

        d = dict(src_dict)
        playlistsidtracks = SpotifyRequestBodyParamsPOSTPlaylistsidtracks.from_dict(
            d.pop("/playlists/:id/tracks")
        )

        spotify_request_body_params_post = cls(
            playlistsidtracks=playlistsidtracks,
        )

        return spotify_request_body_params_post
