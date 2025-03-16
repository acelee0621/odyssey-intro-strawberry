from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..models.spotify_object_repeat_mode import SpotifyObjectRepeatMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="SpotifyRequestQueryParamsPUTMeplayerrepeat")


@_attrs_define
class SpotifyRequestQueryParamsPUTMeplayerrepeat:
    """
    Attributes:
        state (SpotifyObjectRepeatMode):
        device_id (Union[Unset, str]):
    """

    state: SpotifyObjectRepeatMode
    device_id: Union[Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        state = self.state.value

        device_id = self.device_id

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "state": state,
            }
        )
        if device_id is not UNSET:
            field_dict["device_id"] = device_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        state = SpotifyObjectRepeatMode(d.pop("state"))

        device_id = d.pop("device_id", UNSET)

        spotify_request_query_params_put_meplayerrepeat = cls(
            state=state,
            device_id=device_id,
        )

        return spotify_request_query_params_put_meplayerrepeat
