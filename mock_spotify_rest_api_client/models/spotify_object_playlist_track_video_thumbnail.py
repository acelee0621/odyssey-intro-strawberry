from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="SpotifyObjectPlaylistTrackVideoThumbnail")


@_attrs_define
class SpotifyObjectPlaylistTrackVideoThumbnail:
    """
    Attributes:
        url (Union[None, str]):
    """

    url: Union[None, str]

    def to_dict(self) -> dict[str, Any]:
        url: Union[None, str]
        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_url(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        url = _parse_url(d.pop("url"))

        spotify_object_playlist_track_video_thumbnail = cls(
            url=url,
        )

        return spotify_object_playlist_track_video_thumbnail
