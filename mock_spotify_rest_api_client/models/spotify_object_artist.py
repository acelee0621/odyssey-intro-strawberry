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
    from ..models.spotify_object_followers import SpotifyObjectFollowers
    from ..models.spotify_object_image import SpotifyObjectImage


T = TypeVar("T", bound="SpotifyObjectArtist")


@_attrs_define
class SpotifyObjectArtist:
    """
    Attributes:
        external_urls (SpotifyObjectExternalUrl):
        followers (SpotifyObjectFollowers):
        genres (list[str]):
        href (str):
        id (str):
        images (list['SpotifyObjectImage']):
        name (str):
        popularity (float):
        type_ (Literal['artist']):
        uri (str):
    """

    external_urls: "SpotifyObjectExternalUrl"
    followers: "SpotifyObjectFollowers"
    genres: list[str]
    href: str
    id: str
    images: list["SpotifyObjectImage"]
    name: str
    popularity: float
    type_: Literal["artist"]
    uri: str

    def to_dict(self) -> dict[str, Any]:
        external_urls = self.external_urls.to_dict()

        followers = self.followers.to_dict()

        genres = self.genres

        href = self.href

        id = self.id

        images = []
        for images_item_data in self.images:
            images_item = images_item_data.to_dict()
            images.append(images_item)

        name = self.name

        popularity = self.popularity

        type_ = self.type_

        uri = self.uri

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "external_urls": external_urls,
                "followers": followers,
                "genres": genres,
                "href": href,
                "id": id,
                "images": images,
                "name": name,
                "popularity": popularity,
                "type": type_,
                "uri": uri,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.spotify_object_external_url import SpotifyObjectExternalUrl
        from ..models.spotify_object_followers import SpotifyObjectFollowers
        from ..models.spotify_object_image import SpotifyObjectImage

        d = dict(src_dict)
        external_urls = SpotifyObjectExternalUrl.from_dict(d.pop("external_urls"))

        followers = SpotifyObjectFollowers.from_dict(d.pop("followers"))

        genres = cast(list[str], d.pop("genres"))

        href = d.pop("href")

        id = d.pop("id")

        images = []
        _images = d.pop("images")
        for images_item_data in _images:
            images_item = SpotifyObjectImage.from_dict(images_item_data)

            images.append(images_item)

        name = d.pop("name")

        popularity = d.pop("popularity")

        type_ = cast(Literal["artist"], d.pop("type"))
        if type_ != "artist":
            raise ValueError(f"type must match const 'artist', got '{type_}'")

        uri = d.pop("uri")

        spotify_object_artist = cls(
            external_urls=external_urls,
            followers=followers,
            genres=genres,
            href=href,
            id=id,
            images=images,
            name=name,
            popularity=popularity,
            type_=type_,
            uri=uri,
        )

        return spotify_object_artist
