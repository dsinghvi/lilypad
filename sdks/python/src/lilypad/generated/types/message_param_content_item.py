# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.unchecked_base_model import UncheckedBaseModel, UnionMetadata


class MessageParamContentItem_Audio(UncheckedBaseModel):
    type: typing.Literal["audio"] = "audio"
    media_type: str
    audio: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class MessageParamContentItem_Text(UncheckedBaseModel):
    type: typing.Literal["text"] = "text"
    text: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class MessageParamContentItem_Image(UncheckedBaseModel):
    type: typing.Literal["image"] = "image"
    media_type: str
    image: str
    detail: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class MessageParamContentItem_ToolCall(UncheckedBaseModel):
    type: typing.Literal["tool_call"] = "tool_call"
    name: str
    arguments: typing.Dict[str, typing.Optional[typing.Any]]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


MessageParamContentItem = typing_extensions.Annotated[
    typing.Union[
        MessageParamContentItem_Audio,
        MessageParamContentItem_Text,
        MessageParamContentItem_Image,
        MessageParamContentItem_ToolCall,
    ],
    UnionMetadata(discriminant="type"),
]
