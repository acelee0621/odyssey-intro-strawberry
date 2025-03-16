from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.spotify_object_restrictions_reason import SpotifyObjectRestrictionsReason

T = TypeVar("T", bound="SpotifyObjectRestrictions")


@_attrs_define
class SpotifyObjectRestrictions:
    """
    Attributes:
        reason (SpotifyObjectRestrictionsReason):
    """

    reason: SpotifyObjectRestrictionsReason

    def to_dict(self) -> dict[str, Any]:
        reason = self.reason.value

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "reason": reason,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reason = SpotifyObjectRestrictionsReason(d.pop("reason"))

        spotify_object_restrictions = cls(
            reason=reason,
        )

        return spotify_object_restrictions
