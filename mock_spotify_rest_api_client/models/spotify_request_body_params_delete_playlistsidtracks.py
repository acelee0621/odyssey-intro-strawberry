from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.spotify_request_body_params_delete_playlistsidtracks_tracks_item import (
        SpotifyRequestBodyParamsDELETEPlaylistsidtracksTracksItem,
    )


T = TypeVar("T", bound="SpotifyRequestBodyParamsDELETEPlaylistsidtracks")


@_attrs_define
class SpotifyRequestBodyParamsDELETEPlaylistsidtracks:
    """
    Attributes:
        tracks (list['SpotifyRequestBodyParamsDELETEPlaylistsidtracksTracksItem']):
        snapshot_id (Union[Unset, str]):
    """

    tracks: list["SpotifyRequestBodyParamsDELETEPlaylistsidtracksTracksItem"]
    snapshot_id: Union[Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        tracks = []
        for tracks_item_data in self.tracks:
            tracks_item = tracks_item_data.to_dict()
            tracks.append(tracks_item)

        snapshot_id = self.snapshot_id

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "tracks": tracks,
            }
        )
        if snapshot_id is not UNSET:
            field_dict["snapshot_id"] = snapshot_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.spotify_request_body_params_delete_playlistsidtracks_tracks_item import (
            SpotifyRequestBodyParamsDELETEPlaylistsidtracksTracksItem,
        )

        d = dict(src_dict)
        tracks = []
        _tracks = d.pop("tracks")
        for tracks_item_data in _tracks:
            tracks_item = (
                SpotifyRequestBodyParamsDELETEPlaylistsidtracksTracksItem.from_dict(
                    tracks_item_data
                )
            )

            tracks.append(tracks_item)

        snapshot_id = d.pop("snapshot_id", UNSET)

        spotify_request_body_params_delete_playlistsidtracks = cls(
            tracks=tracks,
            snapshot_id=snapshot_id,
        )

        return spotify_request_body_params_delete_playlistsidtracks
