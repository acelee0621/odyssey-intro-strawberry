from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="SpotifyErrorAuthenticationError")


@_attrs_define
class SpotifyErrorAuthenticationError:
    """
    Attributes:
        error (str):
        error_description (str):
    """

    error: str
    error_description: str

    def to_dict(self) -> dict[str, Any]:
        error = self.error

        error_description = self.error_description

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "error": error,
                "error_description": error_description,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        error = d.pop("error")

        error_description = d.pop("error_description")

        spotify_error_authentication_error = cls(
            error=error,
            error_description=error_description,
        )

        return spotify_error_authentication_error
