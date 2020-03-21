# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class Resource(google___protobuf___message___Message):
    max_capacity = ... # type: int
    min_capacity = ... # type: int
    renewable = ... # type: bool
    unit_cost = ... # type: int

    def __init__(self,
        *,
        max_capacity : typing___Optional[int] = None,
        min_capacity : typing___Optional[int] = None,
        renewable : typing___Optional[bool] = None,
        unit_cost : typing___Optional[int] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> Resource: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"max_capacity",u"min_capacity",u"renewable",u"unit_cost"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"max_capacity",b"max_capacity",u"min_capacity",b"min_capacity",u"renewable",b"renewable",u"unit_cost",b"unit_cost"]) -> None: ...

class Recipe(google___protobuf___message___Message):
    duration = ... # type: int
    demands = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[int]
    resources = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[int]

    def __init__(self,
        *,
        duration : typing___Optional[int] = None,
        demands : typing___Optional[typing___Iterable[int]] = None,
        resources : typing___Optional[typing___Iterable[int]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> Recipe: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"demands",u"duration",u"resources"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"demands",b"demands",u"duration",b"duration",u"resources",b"resources"]) -> None: ...

class PerRecipeDelays(google___protobuf___message___Message):
    min_delays = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[int]

    def __init__(self,
        *,
        min_delays : typing___Optional[typing___Iterable[int]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> PerRecipeDelays: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"min_delays"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"min_delays",b"min_delays"]) -> None: ...

class PerSuccessorDelays(google___protobuf___message___Message):

    @property
    def recipe_delays(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[PerRecipeDelays]: ...

    def __init__(self,
        *,
        recipe_delays : typing___Optional[typing___Iterable[PerRecipeDelays]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> PerSuccessorDelays: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"recipe_delays"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"recipe_delays",b"recipe_delays"]) -> None: ...

class Task(google___protobuf___message___Message):
    successors = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[int]

    @property
    def recipes(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[Recipe]: ...

    @property
    def successor_delays(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[PerSuccessorDelays]: ...

    def __init__(self,
        *,
        successors : typing___Optional[typing___Iterable[int]] = None,
        recipes : typing___Optional[typing___Iterable[Recipe]] = None,
        successor_delays : typing___Optional[typing___Iterable[PerSuccessorDelays]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> Task: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"recipes",u"successor_delays",u"successors"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"recipes",b"recipes",u"successor_delays",b"successor_delays",u"successors",b"successors"]) -> None: ...

class RcpspProblem(google___protobuf___message___Message):
    is_consumer_producer = ... # type: bool
    is_resource_investment = ... # type: bool
    is_rcpsp_max = ... # type: bool
    deadline = ... # type: int
    horizon = ... # type: int
    release_date = ... # type: int
    tardiness_cost = ... # type: int
    mpm_time = ... # type: int
    seed = ... # type: int
    basedata = ... # type: typing___Text
    due_date = ... # type: int
    name = ... # type: typing___Text

    @property
    def resources(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[Resource]: ...

    @property
    def tasks(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[Task]: ...

    def __init__(self,
        *,
        resources : typing___Optional[typing___Iterable[Resource]] = None,
        tasks : typing___Optional[typing___Iterable[Task]] = None,
        is_consumer_producer : typing___Optional[bool] = None,
        is_resource_investment : typing___Optional[bool] = None,
        is_rcpsp_max : typing___Optional[bool] = None,
        deadline : typing___Optional[int] = None,
        horizon : typing___Optional[int] = None,
        release_date : typing___Optional[int] = None,
        tardiness_cost : typing___Optional[int] = None,
        mpm_time : typing___Optional[int] = None,
        seed : typing___Optional[int] = None,
        basedata : typing___Optional[typing___Text] = None,
        due_date : typing___Optional[int] = None,
        name : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> RcpspProblem: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"basedata",u"deadline",u"due_date",u"horizon",u"is_consumer_producer",u"is_rcpsp_max",u"is_resource_investment",u"mpm_time",u"name",u"release_date",u"resources",u"seed",u"tardiness_cost",u"tasks"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"basedata",b"basedata",u"deadline",b"deadline",u"due_date",b"due_date",u"horizon",b"horizon",u"is_consumer_producer",b"is_consumer_producer",u"is_rcpsp_max",b"is_rcpsp_max",u"is_resource_investment",b"is_resource_investment",u"mpm_time",b"mpm_time",u"name",b"name",u"release_date",b"release_date",u"resources",b"resources",u"seed",b"seed",u"tardiness_cost",b"tardiness_cost",u"tasks",b"tasks"]) -> None: ...
