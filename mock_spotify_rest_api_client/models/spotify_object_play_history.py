from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.spotify_object_context import SpotifyObjectContext
    from ..models.spotify_object_track_simplified import SpotifyObjectTrackSimplified


T = TypeVar("T", bound="SpotifyObjectPlayHistory")


@_attrs_define
class SpotifyObjectPlayHistory:
    """
    Attributes:
        track (SpotifyObjectTrackSimplified):
        played_at (str):
        context (SpotifyObjectContext):
    """

    track: "SpotifyObjectTrackSimplified"
    played_at: str
    context: "SpotifyObjectContext"

    def to_dict(self) -> dict[str, Any]:
        track = self.track.to_dict()

        played_at = self.played_at

        context = self.context.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "track": track,
                "played_at": played_at,
                "context": context,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.spotify_object_context import SpotifyObjectContext
        from ..models.spotify_object_track_simplified import (
            SpotifyObjectTrackSimplified,
        )

        d = dict(src_dict)
        track = SpotifyObjectTrackSimplified.from_dict(d.pop("track"))

        played_at = d.pop("played_at")

        context = SpotifyObjectContext.from_dict(d.pop("context"))

        spotify_object_play_history = cls(
            track=track,
            played_at=played_at,
            context=context,
        )

        return spotify_object_play_history
