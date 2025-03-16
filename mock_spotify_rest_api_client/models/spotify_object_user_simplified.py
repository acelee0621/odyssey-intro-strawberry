from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    Literal,
    TypeVar,
    Union,
    cast,
)

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.spotify_object_external_url import SpotifyObjectExternalUrl


T = TypeVar("T", bound="SpotifyObjectUserSimplified")


@_attrs_define
class SpotifyObjectUserSimplified:
    """
    Attributes:
        external_urls (SpotifyObjectExternalUrl):
        href (str):
        id (str):
        type_ (Literal['user']):
        uri (str):
        display_name (Union[Unset, str]):
    """

    external_urls: "SpotifyObjectExternalUrl"
    href: str
    id: str
    type_: Literal["user"]
    uri: str
    display_name: Union[Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        external_urls = self.external_urls.to_dict()

        href = self.href

        id = self.id

        type_ = self.type_

        uri = self.uri

        display_name = self.display_name

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
        if display_name is not UNSET:
            field_dict["display_name"] = display_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.spotify_object_external_url import SpotifyObjectExternalUrl

        d = dict(src_dict)
        external_urls = SpotifyObjectExternalUrl.from_dict(d.pop("external_urls"))

        href = d.pop("href")

        id = d.pop("id")

        type_ = cast(Literal["user"], d.pop("type"))
        if type_ != "user":
            raise ValueError(f"type must match const 'user', got '{type_}'")

        uri = d.pop("uri")

        display_name = d.pop("display_name", UNSET)

        spotify_object_user_simplified = cls(
            external_urls=external_urls,
            href=href,
            id=id,
            type_=type_,
            uri=uri,
            display_name=display_name,
        )

        return spotify_object_user_simplified
