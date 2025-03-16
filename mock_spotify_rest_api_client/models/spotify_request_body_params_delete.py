from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.spotify_request_body_params_delete_mealbums import (
        SpotifyRequestBodyParamsDELETEMealbums,
    )
    from ..models.spotify_request_body_params_delete_meepisodes import (
        SpotifyRequestBodyParamsDELETEMeepisodes,
    )
    from ..models.spotify_request_body_params_delete_mefollowing import (
        SpotifyRequestBodyParamsDELETEMefollowing,
    )
    from ..models.spotify_request_body_params_delete_metracks import (
        SpotifyRequestBodyParamsDELETEMetracks,
    )
    from ..models.spotify_request_body_params_delete_playlistsidtracks import (
        SpotifyRequestBodyParamsDELETEPlaylistsidtracks,
    )


T = TypeVar("T", bound="SpotifyRequestBodyParamsDELETE")


@_attrs_define
class SpotifyRequestBodyParamsDELETE:
    """
    Attributes:
        mealbums (SpotifyRequestBodyParamsDELETEMealbums):
        meepisodes (SpotifyRequestBodyParamsDELETEMeepisodes):
        mefollowing (SpotifyRequestBodyParamsDELETEMefollowing):
        metracks (SpotifyRequestBodyParamsDELETEMetracks):
        playlistsidtracks (SpotifyRequestBodyParamsDELETEPlaylistsidtracks):
    """

    mealbums: "SpotifyRequestBodyParamsDELETEMealbums"
    meepisodes: "SpotifyRequestBodyParamsDELETEMeepisodes"
    mefollowing: "SpotifyRequestBodyParamsDELETEMefollowing"
    metracks: "SpotifyRequestBodyParamsDELETEMetracks"
    playlistsidtracks: "SpotifyRequestBodyParamsDELETEPlaylistsidtracks"

    def to_dict(self) -> dict[str, Any]:
        mealbums = self.mealbums.to_dict()

        meepisodes = self.meepisodes.to_dict()

        mefollowing = self.mefollowing.to_dict()

        metracks = self.metracks.to_dict()

        playlistsidtracks = self.playlistsidtracks.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "/me/albums": mealbums,
                "/me/episodes": meepisodes,
                "/me/following": mefollowing,
                "/me/tracks": metracks,
                "/playlists/:id/tracks": playlistsidtracks,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.spotify_request_body_params_delete_mealbums import (
            SpotifyRequestBodyParamsDELETEMealbums,
        )
        from ..models.spotify_request_body_params_delete_meepisodes import (
            SpotifyRequestBodyParamsDELETEMeepisodes,
        )
        from ..models.spotify_request_body_params_delete_mefollowing import (
            SpotifyRequestBodyParamsDELETEMefollowing,
        )
        from ..models.spotify_request_body_params_delete_metracks import (
            SpotifyRequestBodyParamsDELETEMetracks,
        )
        from ..models.spotify_request_body_params_delete_playlistsidtracks import (
            SpotifyRequestBodyParamsDELETEPlaylistsidtracks,
        )

        d = dict(src_dict)
        mealbums = SpotifyRequestBodyParamsDELETEMealbums.from_dict(d.pop("/me/albums"))

        meepisodes = SpotifyRequestBodyParamsDELETEMeepisodes.from_dict(
            d.pop("/me/episodes")
        )

        mefollowing = SpotifyRequestBodyParamsDELETEMefollowing.from_dict(
            d.pop("/me/following")
        )

        metracks = SpotifyRequestBodyParamsDELETEMetracks.from_dict(d.pop("/me/tracks"))

        playlistsidtracks = SpotifyRequestBodyParamsDELETEPlaylistsidtracks.from_dict(
            d.pop("/playlists/:id/tracks")
        )

        spotify_request_body_params_delete = cls(
            mealbums=mealbums,
            meepisodes=meepisodes,
            mefollowing=mefollowing,
            metracks=metracks,
            playlistsidtracks=playlistsidtracks,
        )

        return spotify_request_body_params_delete
