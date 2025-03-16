from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="SpotifyObjectExplicitContentSettings")


@_attrs_define
class SpotifyObjectExplicitContentSettings:
    """
    Attributes:
        filter_enabled (bool):
        filter_locked (bool):
    """

    filter_enabled: bool
    filter_locked: bool

    def to_dict(self) -> dict[str, Any]:
        filter_enabled = self.filter_enabled

        filter_locked = self.filter_locked

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "filter_enabled": filter_enabled,
                "filter_locked": filter_locked,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        filter_enabled = d.pop("filter_enabled")

        filter_locked = d.pop("filter_locked")

        spotify_object_explicit_content_settings = cls(
            filter_enabled=filter_enabled,
            filter_locked=filter_locked,
        )

        return spotify_object_explicit_content_settings
