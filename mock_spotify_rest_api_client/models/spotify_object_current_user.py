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
    from ..models.spotify_object_explicit_content_settings import (
        SpotifyObjectExplicitContentSettings,
    )
    from ..models.spotify_object_external_url import SpotifyObjectExternalUrl
    from ..models.spotify_object_followers import SpotifyObjectFollowers
    from ..models.spotify_object_image import SpotifyObjectImage


T = TypeVar("T", bound="SpotifyObjectCurrentUser")


@_attrs_define
class SpotifyObjectCurrentUser:
    """
    Attributes:
        country (str):
        display_name (str):
        email (str):
        explicit_content (SpotifyObjectExplicitContentSettings):
        external_urls (SpotifyObjectExternalUrl):
        followers (SpotifyObjectFollowers):
        href (str):
        id (str):
        images (list['SpotifyObjectImage']):
        product (str):
        type_ (Literal['user']):
        uri (str):
    """

    country: str
    display_name: str
    email: str
    explicit_content: "SpotifyObjectExplicitContentSettings"
    external_urls: "SpotifyObjectExternalUrl"
    followers: "SpotifyObjectFollowers"
    href: str
    id: str
    images: list["SpotifyObjectImage"]
    product: str
    type_: Literal["user"]
    uri: str

    def to_dict(self) -> dict[str, Any]:
        country = self.country

        display_name = self.display_name

        email = self.email

        explicit_content = self.explicit_content.to_dict()

        external_urls = self.external_urls.to_dict()

        followers = self.followers.to_dict()

        href = self.href

        id = self.id

        images = []
        for images_item_data in self.images:
            images_item = images_item_data.to_dict()
            images.append(images_item)

        product = self.product

        type_ = self.type_

        uri = self.uri

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "country": country,
                "display_name": display_name,
                "email": email,
                "explicit_content": explicit_content,
                "external_urls": external_urls,
                "followers": followers,
                "href": href,
                "id": id,
                "images": images,
                "product": product,
                "type": type_,
                "uri": uri,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.spotify_object_explicit_content_settings import (
            SpotifyObjectExplicitContentSettings,
        )
        from ..models.spotify_object_external_url import SpotifyObjectExternalUrl
        from ..models.spotify_object_followers import SpotifyObjectFollowers
        from ..models.spotify_object_image import SpotifyObjectImage

        d = dict(src_dict)
        country = d.pop("country")

        display_name = d.pop("display_name")

        email = d.pop("email")

        explicit_content = SpotifyObjectExplicitContentSettings.from_dict(
            d.pop("explicit_content")
        )

        external_urls = SpotifyObjectExternalUrl.from_dict(d.pop("external_urls"))

        followers = SpotifyObjectFollowers.from_dict(d.pop("followers"))

        href = d.pop("href")

        id = d.pop("id")

        images = []
        _images = d.pop("images")
        for images_item_data in _images:
            images_item = SpotifyObjectImage.from_dict(images_item_data)

            images.append(images_item)

        product = d.pop("product")

        type_ = cast(Literal["user"], d.pop("type"))
        if type_ != "user":
            raise ValueError(f"type must match const 'user', got '{type_}'")

        uri = d.pop("uri")

        spotify_object_current_user = cls(
            country=country,
            display_name=display_name,
            email=email,
            explicit_content=explicit_content,
            external_urls=external_urls,
            followers=followers,
            href=href,
            id=id,
            images=images,
            product=product,
            type_=type_,
            uri=uri,
        )

        return spotify_object_current_user
