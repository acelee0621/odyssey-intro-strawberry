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


T = TypeVar("T", bound="SpotifyObjectPlaylistEpisodeArtist")


@_attrs_define
class SpotifyObjectPlaylistEpisodeArtist:
    """
    Attributes:
        external_urls (SpotifyObjectExternalUrl):
        href (str):
        id (str):
        name (str):
        type_ (Literal['show']):
        uri (str):
    """

    external_urls: "SpotifyObjectExternalUrl"
    href: str
    id: str
    name: str
    type_: Literal["show"]
    uri: str

    def to_dict(self) -> dict[str, Any]:
        external_urls = self.external_urls.to_dict()

        href = self.href

        id = self.id

        name = self.name

        type_ = self.type_

        uri = self.uri

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "external_urls": external_urls,
                "href": href,
                "id": id,
                "name": name,
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

        name = d.pop("name")

        type_ = cast(Literal["show"], d.pop("type"))
        if type_ != "show":
            raise ValueError(f"type must match const 'show', got '{type_}'")

        uri = d.pop("uri")

        spotify_object_playlist_episode_artist = cls(
            external_urls=external_urls,
            href=href,
            id=id,
            name=name,
            type_=type_,
            uri=uri,
        )

        return spotify_object_playlist_episode_artist
