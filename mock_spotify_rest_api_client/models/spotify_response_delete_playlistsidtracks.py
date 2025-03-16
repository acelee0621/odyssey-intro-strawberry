from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="SpotifyResponseDELETEPlaylistsidtracks")


@_attrs_define
class SpotifyResponseDELETEPlaylistsidtracks:
    """
    Attributes:
        snapshot_id (str):
    """

    snapshot_id: str

    def to_dict(self) -> dict[str, Any]:
        snapshot_id = self.snapshot_id

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "snapshot_id": snapshot_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        snapshot_id = d.pop("snapshot_id")

        spotify_response_delete_playlistsidtracks = cls(
            snapshot_id=snapshot_id,
        )

        return spotify_response_delete_playlistsidtracks
