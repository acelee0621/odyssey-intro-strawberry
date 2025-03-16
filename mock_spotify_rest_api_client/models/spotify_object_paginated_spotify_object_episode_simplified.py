from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.spotify_object_episode_simplified import (
        SpotifyObjectEpisodeSimplified,
    )


T = TypeVar("T", bound="SpotifyObjectPaginatedSpotifyObjectEpisodeSimplified")


@_attrs_define
class SpotifyObjectPaginatedSpotifyObjectEpisodeSimplified:
    """
    Attributes:
        items (list['SpotifyObjectEpisodeSimplified']):
        href (str):
        limit (float):
        next_ (Union[None, str]):
        offset (float):
        previous (Union[None, str]):
        total (float):
    """

    items: list["SpotifyObjectEpisodeSimplified"]
    href: str
    limit: float
    next_: Union[None, str]
    offset: float
    previous: Union[None, str]
    total: float

    def to_dict(self) -> dict[str, Any]:
        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        href = self.href

        limit = self.limit

        next_: Union[None, str]
        next_ = self.next_

        offset = self.offset

        previous: Union[None, str]
        previous = self.previous

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "items": items,
                "href": href,
                "limit": limit,
                "next": next_,
                "offset": offset,
                "previous": previous,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.spotify_object_episode_simplified import (
            SpotifyObjectEpisodeSimplified,
        )

        d = dict(src_dict)
        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = SpotifyObjectEpisodeSimplified.from_dict(items_item_data)

            items.append(items_item)

        href = d.pop("href")

        limit = d.pop("limit")

        def _parse_next_(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        next_ = _parse_next_(d.pop("next"))

        offset = d.pop("offset")

        def _parse_previous(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        previous = _parse_previous(d.pop("previous"))

        total = d.pop("total")

        spotify_object_paginated_spotify_object_episode_simplified = cls(
            items=items,
            href=href,
            limit=limit,
            next_=next_,
            offset=offset,
            previous=previous,
            total=total,
        )

        return spotify_object_paginated_spotify_object_episode_simplified
