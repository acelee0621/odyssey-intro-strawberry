from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.spotify_object_device import SpotifyObjectDevice


T = TypeVar("T", bound="SpotifyObjectListdevicesSpotifyObjectDevice")


@_attrs_define
class SpotifyObjectListdevicesSpotifyObjectDevice:
    """
    Attributes:
        devices (list['SpotifyObjectDevice']):
    """

    devices: list["SpotifyObjectDevice"]

    def to_dict(self) -> dict[str, Any]:
        devices = []
        for devices_item_data in self.devices:
            devices_item = devices_item_data.to_dict()
            devices.append(devices_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "devices": devices,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.spotify_object_device import SpotifyObjectDevice

        d = dict(src_dict)
        devices = []
        _devices = d.pop("devices")
        for devices_item_data in _devices:
            devices_item = SpotifyObjectDevice.from_dict(devices_item_data)

            devices.append(devices_item)

        spotify_object_listdevices_spotify_object_device = cls(
            devices=devices,
        )

        return spotify_object_listdevices_spotify_object_device
