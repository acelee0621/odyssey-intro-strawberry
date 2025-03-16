from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.spotify_object_context_type import SpotifyObjectContextType

if TYPE_CHECKING:
    from ..models.spotify_object_external_url import SpotifyObjectExternalUrl


T = TypeVar("T", bound="SpotifyObjectContext")


@_attrs_define
class SpotifyObjectContext:
    """
    Attributes:
        type_ (SpotifyObjectContextType):
        href (str):
        external_urls (SpotifyObjectExternalUrl):
        uri (str):
    """

    type_: SpotifyObjectContextType
    href: str
    external_urls: "SpotifyObjectExternalUrl"
    uri: str

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        href = self.href

        external_urls = self.external_urls.to_dict()

        uri = self.uri

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "type": type_,
                "href": href,
                "external_urls": external_urls,
                "uri": uri,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.spotify_object_external_url import SpotifyObjectExternalUrl

        d = dict(src_dict)
        type_ = SpotifyObjectContextType(d.pop("type"))

        href = d.pop("href")

        external_urls = SpotifyObjectExternalUrl.from_dict(d.pop("external_urls"))

        uri = d.pop("uri")

        spotify_object_context = cls(
            type_=type_,
            href=href,
            external_urls=external_urls,
            uri=uri,
        )

        return spotify_object_context
