from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.spotify_object_disallows import SpotifyObjectDisallows


T = TypeVar("T", bound="SpotifyObjectActions")


@_attrs_define
class SpotifyObjectActions:
    """
    Attributes:
        disallows (SpotifyObjectDisallows):
    """

    disallows: "SpotifyObjectDisallows"

    def to_dict(self) -> dict[str, Any]:
        disallows = self.disallows.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "disallows": disallows,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.spotify_object_disallows import SpotifyObjectDisallows

        d = dict(src_dict)
        disallows = SpotifyObjectDisallows.from_dict(d.pop("disallows"))

        spotify_object_actions = cls(
            disallows=disallows,
        )

        return spotify_object_actions
