from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="SpotifyRequestBodyParamsDELETEPlaylistsidtracksTracksItem")


@_attrs_define
class SpotifyRequestBodyParamsDELETEPlaylistsidtracksTracksItem:
    """
    Attributes:
        uri (str):
    """

    uri: str

    def to_dict(self) -> dict[str, Any]:
        uri = self.uri

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "uri": uri,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uri = d.pop("uri")

        spotify_request_body_params_delete_playlistsidtracks_tracks_item = cls(
            uri=uri,
        )

        return spotify_request_body_params_delete_playlistsidtracks_tracks_item
