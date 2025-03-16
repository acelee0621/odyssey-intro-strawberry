from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="SpotifyObjectDevice")


@_attrs_define
class SpotifyObjectDevice:
    """
    Attributes:
        id (str):
        is_active (bool):
        is_private_session (bool):
        is_restricted (bool):
        name (str):
        type_ (str):
        volume_percent (float):
    """

    id: str
    is_active: bool
    is_private_session: bool
    is_restricted: bool
    name: str
    type_: str
    volume_percent: float

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        is_active = self.is_active

        is_private_session = self.is_private_session

        is_restricted = self.is_restricted

        name = self.name

        type_ = self.type_

        volume_percent = self.volume_percent

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "is_active": is_active,
                "is_private_session": is_private_session,
                "is_restricted": is_restricted,
                "name": name,
                "type": type_,
                "volume_percent": volume_percent,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        is_active = d.pop("is_active")

        is_private_session = d.pop("is_private_session")

        is_restricted = d.pop("is_restricted")

        name = d.pop("name")

        type_ = d.pop("type")

        volume_percent = d.pop("volume_percent")

        spotify_object_device = cls(
            id=id,
            is_active=is_active,
            is_private_session=is_private_session,
            is_restricted=is_restricted,
            name=name,
            type_=type_,
            volume_percent=volume_percent,
        )

        return spotify_object_device
