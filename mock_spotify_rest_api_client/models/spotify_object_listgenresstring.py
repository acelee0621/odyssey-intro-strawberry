from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="SpotifyObjectListgenresstring")


@_attrs_define
class SpotifyObjectListgenresstring:
    """
    Attributes:
        genres (list[str]):
    """

    genres: list[str]

    def to_dict(self) -> dict[str, Any]:
        genres = self.genres

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "genres": genres,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        genres = cast(list[str], d.pop("genres"))

        spotify_object_listgenresstring = cls(
            genres=genres,
        )

        return spotify_object_listgenresstring
