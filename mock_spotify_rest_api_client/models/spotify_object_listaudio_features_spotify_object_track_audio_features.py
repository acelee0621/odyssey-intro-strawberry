from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.spotify_object_track_audio_features import (
        SpotifyObjectTrackAudioFeatures,
    )


T = TypeVar("T", bound="SpotifyObjectListaudioFeaturesSpotifyObjectTrackAudioFeatures")


@_attrs_define
class SpotifyObjectListaudioFeaturesSpotifyObjectTrackAudioFeatures:
    """
    Attributes:
        audio_features (list['SpotifyObjectTrackAudioFeatures']):
    """

    audio_features: list["SpotifyObjectTrackAudioFeatures"]

    def to_dict(self) -> dict[str, Any]:
        audio_features = []
        for audio_features_item_data in self.audio_features:
            audio_features_item = audio_features_item_data.to_dict()
            audio_features.append(audio_features_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "audio_features": audio_features,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.spotify_object_track_audio_features import (
            SpotifyObjectTrackAudioFeatures,
        )

        d = dict(src_dict)
        audio_features = []
        _audio_features = d.pop("audio_features")
        for audio_features_item_data in _audio_features:
            audio_features_item = SpotifyObjectTrackAudioFeatures.from_dict(
                audio_features_item_data
            )

            audio_features.append(audio_features_item)

        spotify_object_listaudio_features_spotify_object_track_audio_features = cls(
            audio_features=audio_features,
        )

        return spotify_object_listaudio_features_spotify_object_track_audio_features
