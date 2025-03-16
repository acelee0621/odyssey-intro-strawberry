from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.spotify_object_episode import SpotifyObjectEpisode


T = TypeVar("T", bound="SpotifyObjectListepisodesSpotifyObjectEpisode")


@_attrs_define
class SpotifyObjectListepisodesSpotifyObjectEpisode:
    """
    Attributes:
        episodes (list['SpotifyObjectEpisode']):
    """

    episodes: list["SpotifyObjectEpisode"]

    def to_dict(self) -> dict[str, Any]:
        episodes = []
        for episodes_item_data in self.episodes:
            episodes_item = episodes_item_data.to_dict()
            episodes.append(episodes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "episodes": episodes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.spotify_object_episode import SpotifyObjectEpisode

        d = dict(src_dict)
        episodes = []
        _episodes = d.pop("episodes")
        for episodes_item_data in _episodes:
            episodes_item = SpotifyObjectEpisode.from_dict(episodes_item_data)

            episodes.append(episodes_item)

        spotify_object_listepisodes_spotify_object_episode = cls(
            episodes=episodes,
        )

        return spotify_object_listepisodes_spotify_object_episode
