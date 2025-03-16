from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="SpotifyObjectImage")


@_attrs_define
class SpotifyObjectImage:
    """
    Attributes:
        url (str):
        height (float):
        width (float):
    """

    url: str
    height: float
    width: float

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        height = self.height

        width = self.width

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "url": url,
                "height": height,
                "width": width,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        height = d.pop("height")

        width = d.pop("width")

        spotify_object_image = cls(
            url=url,
            height=height,
            width=width,
        )

        return spotify_object_image
