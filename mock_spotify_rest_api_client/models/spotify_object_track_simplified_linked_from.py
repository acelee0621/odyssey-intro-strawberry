from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    Literal,
    TypeVar,
    cast,
)

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.spotify_object_external_url import SpotifyObjectExternalUrl


T = TypeVar("T", bound="SpotifyObjectTrackSimplifiedLinkedFrom")


@_attrs_define
class SpotifyObjectTrackSimplifiedLinkedFrom:
    """
    Attributes:
        external_urls (SpotifyObjectExternalUrl):
        href (str):
        id (str):
        type_ (Literal['track']):
        uri (str):
    """

    external_urls: "SpotifyObjectExternalUrl"
    href: str
    id: str
    type_: Literal["track"]
    uri: str

    def to_dict(self) -> dict[str, Any]:
        external_urls = self.external_urls.to_dict()

        href = self.href

        id = self.id

        type_ = self.type_

        uri = self.uri

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "external_urls": external_urls,
                "href": href,
                "id": id,
                "type": type_,
                "uri": uri,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.spotify_object_external_url import SpotifyObjectExternalUrl

        d = dict(src_dict)
        external_urls = SpotifyObjectExternalUrl.from_dict(d.pop("external_urls"))

        href = d.pop("href")

        id = d.pop("id")

        type_ = cast(Literal["track"], d.pop("type"))
        if type_ != "track":
            raise ValueError(f"type must match const 'track', got '{type_}'")

        uri = d.pop("uri")

        spotify_object_track_simplified_linked_from = cls(
            external_urls=external_urls,
            href=href,
            id=id,
            type_=type_,
            uri=uri,
        )

        return spotify_object_track_simplified_linked_from
