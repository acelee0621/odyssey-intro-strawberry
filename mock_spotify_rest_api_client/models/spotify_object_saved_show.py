from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.spotify_object_show import SpotifyObjectShow


T = TypeVar("T", bound="SpotifyObjectSavedShow")


@_attrs_define
class SpotifyObjectSavedShow:
    """
    Attributes:
        added_at (str):
        show (SpotifyObjectShow):
    """

    added_at: str
    show: "SpotifyObjectShow"

    def to_dict(self) -> dict[str, Any]:
        added_at = self.added_at

        show = self.show.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "added_at": added_at,
                "show": show,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.spotify_object_show import SpotifyObjectShow

        d = dict(src_dict)
        added_at = d.pop("added_at")

        show = SpotifyObjectShow.from_dict(d.pop("show"))

        spotify_object_saved_show = cls(
            added_at=added_at,
            show=show,
        )

        return spotify_object_saved_show
