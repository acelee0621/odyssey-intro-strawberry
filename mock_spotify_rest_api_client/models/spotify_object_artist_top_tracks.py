from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.spotify_object_track import SpotifyObjectTrack


T = TypeVar("T", bound="SpotifyObjectArtistTopTracks")


@_attrs_define
class SpotifyObjectArtistTopTracks:
    """
    Attributes:
        tracks (list['SpotifyObjectTrack']):
    """

    tracks: list["SpotifyObjectTrack"]

    def to_dict(self) -> dict[str, Any]:
        tracks = []
        for tracks_item_data in self.tracks:
            tracks_item = tracks_item_data.to_dict()
            tracks.append(tracks_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "tracks": tracks,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.spotify_object_track import SpotifyObjectTrack

        d = dict(src_dict)
        tracks = []
        _tracks = d.pop("tracks")
        for tracks_item_data in _tracks:
            tracks_item = SpotifyObjectTrack.from_dict(tracks_item_data)

            tracks.append(tracks_item)

        spotify_object_artist_top_tracks = cls(
            tracks=tracks,
        )

        return spotify_object_artist_top_tracks
