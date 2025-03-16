from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SpotifyRequestBodyParamsPUTPlaylistsidfollowers")


@_attrs_define
class SpotifyRequestBodyParamsPUTPlaylistsidfollowers:
    """
    Attributes:
        public (Union[Unset, bool]):
    """

    public: Union[Unset, bool] = UNSET

    def to_dict(self) -> dict[str, Any]:
        public = self.public

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if public is not UNSET:
            field_dict["public"] = public

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        public = d.pop("public", UNSET)

        spotify_request_body_params_put_playlistsidfollowers = cls(
            public=public,
        )

        return spotify_request_body_params_put_playlistsidfollowers
