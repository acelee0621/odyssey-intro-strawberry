from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="SpotifyRequestQueryParamsGETArtistsidtopTracks")


@_attrs_define
class SpotifyRequestQueryParamsGETArtistsidtopTracks:
    """
    Attributes:
        market (str):
    """

    market: str

    def to_dict(self) -> dict[str, Any]:
        market = self.market

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "market": market,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        market = d.pop("market")

        spotify_request_query_params_get_artistsidtop_tracks = cls(
            market=market,
        )

        return spotify_request_query_params_get_artistsidtop_tracks
