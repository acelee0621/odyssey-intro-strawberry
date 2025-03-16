from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.spotify_error_regular_error_error import SpotifyErrorRegularErrorError


T = TypeVar("T", bound="SpotifyErrorRegularError")


@_attrs_define
class SpotifyErrorRegularError:
    """
    Attributes:
        error (SpotifyErrorRegularErrorError):
    """

    error: "SpotifyErrorRegularErrorError"

    def to_dict(self) -> dict[str, Any]:
        error = self.error.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "error": error,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.spotify_error_regular_error_error import (
            SpotifyErrorRegularErrorError,
        )

        d = dict(src_dict)
        error = SpotifyErrorRegularErrorError.from_dict(d.pop("error"))

        spotify_error_regular_error = cls(
            error=error,
        )

        return spotify_error_regular_error
