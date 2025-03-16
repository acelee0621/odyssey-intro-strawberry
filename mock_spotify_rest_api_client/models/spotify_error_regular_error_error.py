from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SpotifyErrorRegularErrorError")


@_attrs_define
class SpotifyErrorRegularErrorError:
    """
    Attributes:
        status (float):
        message (str):
        reason (Union[Unset, str]):
    """

    status: float
    message: str
    reason: Union[Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        message = self.message

        reason = self.reason

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "status": status,
                "message": message,
            }
        )
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = d.pop("status")

        message = d.pop("message")

        reason = d.pop("reason", UNSET)

        spotify_error_regular_error_error = cls(
            status=status,
            message=message,
            reason=reason,
        )

        return spotify_error_regular_error_error
