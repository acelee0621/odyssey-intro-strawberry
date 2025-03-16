from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    Literal,
    TypeVar,
    cast,
)

from attrs import define as _attrs_define

from ..models.spotify_object_album_type import SpotifyObjectAlbumType
from ..models.spotify_object_release_date_precision import (
    SpotifyObjectReleaseDatePrecision,
)

if TYPE_CHECKING:
    from ..models.spotify_object_artist_simplified import SpotifyObjectArtistSimplified
    from ..models.spotify_object_copyright import SpotifyObjectCopyright
    from ..models.spotify_object_external_id import SpotifyObjectExternalId
    from ..models.spotify_object_external_url import SpotifyObjectExternalUrl
    from ..models.spotify_object_image import SpotifyObjectImage
    from ..models.spotify_object_paginated_spotify_object_track_simplified import (
        SpotifyObjectPaginatedSpotifyObjectTrackSimplified,
    )


T = TypeVar("T", bound="SpotifyObjectAlbum")


@_attrs_define
class SpotifyObjectAlbum:
    """
    Attributes:
        album_type (SpotifyObjectAlbumType):
        artists (list['SpotifyObjectArtistSimplified']):
        available_markets (list[str]):
        copyrights (list['SpotifyObjectCopyright']):
        external_ids (SpotifyObjectExternalId):
        external_urls (SpotifyObjectExternalUrl):
        genres (list[str]):
        href (str):
        id (str):
        images (list['SpotifyObjectImage']):
        label (str):
        name (str):
        popularity (float):
        release_date (str):
        release_date_precision (SpotifyObjectReleaseDatePrecision):
        total_tracks (float):
        tracks (SpotifyObjectPaginatedSpotifyObjectTrackSimplified):
        type_ (Literal['album']):
        uri (str):
    """

    album_type: SpotifyObjectAlbumType
    artists: list["SpotifyObjectArtistSimplified"]
    available_markets: list[str]
    copyrights: list["SpotifyObjectCopyright"]
    external_ids: "SpotifyObjectExternalId"
    external_urls: "SpotifyObjectExternalUrl"
    genres: list[str]
    href: str
    id: str
    images: list["SpotifyObjectImage"]
    label: str
    name: str
    popularity: float
    release_date: str
    release_date_precision: SpotifyObjectReleaseDatePrecision
    total_tracks: float
    tracks: "SpotifyObjectPaginatedSpotifyObjectTrackSimplified"
    type_: Literal["album"]
    uri: str

    def to_dict(self) -> dict[str, Any]:
        album_type = self.album_type.value

        artists = []
        for artists_item_data in self.artists:
            artists_item = artists_item_data.to_dict()
            artists.append(artists_item)

        available_markets = self.available_markets

        copyrights = []
        for copyrights_item_data in self.copyrights:
            copyrights_item = copyrights_item_data.to_dict()
            copyrights.append(copyrights_item)

        external_ids = self.external_ids.to_dict()

        external_urls = self.external_urls.to_dict()

        genres = self.genres

        href = self.href

        id = self.id

        images = []
        for images_item_data in self.images:
            images_item = images_item_data.to_dict()
            images.append(images_item)

        label = self.label

        name = self.name

        popularity = self.popularity

        release_date = self.release_date

        release_date_precision = self.release_date_precision.value

        total_tracks = self.total_tracks

        tracks = self.tracks.to_dict()

        type_ = self.type_

        uri = self.uri

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "album_type": album_type,
                "artists": artists,
                "available_markets": available_markets,
                "copyrights": copyrights,
                "external_ids": external_ids,
                "external_urls": external_urls,
                "genres": genres,
                "href": href,
                "id": id,
                "images": images,
                "label": label,
                "name": name,
                "popularity": popularity,
                "release_date": release_date,
                "release_date_precision": release_date_precision,
                "total_tracks": total_tracks,
                "tracks": tracks,
                "type": type_,
                "uri": uri,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.spotify_object_artist_simplified import (
            SpotifyObjectArtistSimplified,
        )
        from ..models.spotify_object_copyright import SpotifyObjectCopyright
        from ..models.spotify_object_external_id import SpotifyObjectExternalId
        from ..models.spotify_object_external_url import SpotifyObjectExternalUrl
        from ..models.spotify_object_image import SpotifyObjectImage
        from ..models.spotify_object_paginated_spotify_object_track_simplified import (
            SpotifyObjectPaginatedSpotifyObjectTrackSimplified,
        )

        d = dict(src_dict)
        album_type = SpotifyObjectAlbumType(d.pop("album_type"))

        artists = []
        _artists = d.pop("artists")
        for artists_item_data in _artists:
            artists_item = SpotifyObjectArtistSimplified.from_dict(artists_item_data)

            artists.append(artists_item)

        available_markets = cast(list[str], d.pop("available_markets"))

        copyrights = []
        _copyrights = d.pop("copyrights")
        for copyrights_item_data in _copyrights:
            copyrights_item = SpotifyObjectCopyright.from_dict(copyrights_item_data)

            copyrights.append(copyrights_item)

        external_ids = SpotifyObjectExternalId.from_dict(d.pop("external_ids"))

        external_urls = SpotifyObjectExternalUrl.from_dict(d.pop("external_urls"))

        genres = cast(list[str], d.pop("genres"))

        href = d.pop("href")

        id = d.pop("id")

        images = []
        _images = d.pop("images")
        for images_item_data in _images:
            images_item = SpotifyObjectImage.from_dict(images_item_data)

            images.append(images_item)

        label = d.pop("label")

        name = d.pop("name")

        popularity = d.pop("popularity")

        release_date = d.pop("release_date")

        release_date_precision = SpotifyObjectReleaseDatePrecision(
            d.pop("release_date_precision")
        )

        total_tracks = d.pop("total_tracks")

        tracks = SpotifyObjectPaginatedSpotifyObjectTrackSimplified.from_dict(
            d.pop("tracks")
        )

        type_ = cast(Literal["album"], d.pop("type"))
        if type_ != "album":
            raise ValueError(f"type must match const 'album', got '{type_}'")

        uri = d.pop("uri")

        spotify_object_album = cls(
            album_type=album_type,
            artists=artists,
            available_markets=available_markets,
            copyrights=copyrights,
            external_ids=external_ids,
            external_urls=external_urls,
            genres=genres,
            href=href,
            id=id,
            images=images,
            label=label,
            name=name,
            popularity=popularity,
            release_date=release_date,
            release_date_precision=release_date_precision,
            total_tracks=total_tracks,
            tracks=tracks,
            type_=type_,
            uri=uri,
        )

        return spotify_object_album
