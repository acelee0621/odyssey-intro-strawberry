from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.spotify_object_recommendation_seed import (
        SpotifyObjectRecommendationSeed,
    )
    from ..models.spotify_object_track import SpotifyObjectTrack


T = TypeVar("T", bound="SpotifyObjectRecommendations")


@_attrs_define
class SpotifyObjectRecommendations:
    """
    Attributes:
        seeds (list['SpotifyObjectRecommendationSeed']):
        tracks (list['SpotifyObjectTrack']):
    """

    seeds: list["SpotifyObjectRecommendationSeed"]
    tracks: list["SpotifyObjectTrack"]

    def to_dict(self) -> dict[str, Any]:
        seeds = []
        for seeds_item_data in self.seeds:
            seeds_item = seeds_item_data.to_dict()
            seeds.append(seeds_item)

        tracks = []
        for tracks_item_data in self.tracks:
            tracks_item = tracks_item_data.to_dict()
            tracks.append(tracks_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "seeds": seeds,
                "tracks": tracks,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.spotify_object_recommendation_seed import (
            SpotifyObjectRecommendationSeed,
        )
        from ..models.spotify_object_track import SpotifyObjectTrack

        d = dict(src_dict)
        seeds = []
        _seeds = d.pop("seeds")
        for seeds_item_data in _seeds:
            seeds_item = SpotifyObjectRecommendationSeed.from_dict(seeds_item_data)

            seeds.append(seeds_item)

        tracks = []
        _tracks = d.pop("tracks")
        for tracks_item_data in _tracks:
            tracks_item = SpotifyObjectTrack.from_dict(tracks_item_data)

            tracks.append(tracks_item)

        spotify_object_recommendations = cls(
            seeds=seeds,
            tracks=tracks,
        )

        return spotify_object_recommendations
