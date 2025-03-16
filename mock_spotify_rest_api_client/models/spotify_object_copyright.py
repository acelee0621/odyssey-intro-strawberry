from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.spotify_object_copyright_type import SpotifyObjectCopyrightType

T = TypeVar("T", bound="SpotifyObjectCopyright")


@_attrs_define
class SpotifyObjectCopyright:
    """
    Attributes:
        text (str):
        type_ (SpotifyObjectCopyrightType):
    """

    text: str
    type_: SpotifyObjectCopyrightType

    def to_dict(self) -> dict[str, Any]:
        text = self.text

        type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "text": text,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        text = d.pop("text")

        type_ = SpotifyObjectCopyrightType(d.pop("type"))

        spotify_object_copyright = cls(
            text=text,
            type_=type_,
        )

        return spotify_object_copyright
