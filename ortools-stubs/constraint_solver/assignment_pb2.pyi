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


class IntVarAssignment(google___protobuf___message___Message):
    var_id = ... # type: typing___Text
    min = ... # type: int
    max = ... # type: int
    active = ... # type: bool

    def __init__(self,
        *,
        var_id : typing___Optional[typing___Text] = None,
        min : typing___Optional[int] = None,
        max : typing___Optional[int] = None,
        active : typing___Optional[bool] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> IntVarAssignment: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"active",u"max",u"min",u"var_id"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"active",b"active",u"max",b"max",u"min",b"min",u"var_id",b"var_id"]) -> None: ...

class IntervalVarAssignment(google___protobuf___message___Message):
    var_id = ... # type: typing___Text
    start_min = ... # type: int
    start_max = ... # type: int
    duration_min = ... # type: int
    duration_max = ... # type: int
    end_min = ... # type: int
    end_max = ... # type: int
    performed_min = ... # type: int
    performed_max = ... # type: int
    active = ... # type: bool

    def __init__(self,
        *,
        var_id : typing___Optional[typing___Text] = None,
        start_min : typing___Optional[int] = None,
        start_max : typing___Optional[int] = None,
        duration_min : typing___Optional[int] = None,
        duration_max : typing___Optional[int] = None,
        end_min : typing___Optional[int] = None,
        end_max : typing___Optional[int] = None,
        performed_min : typing___Optional[int] = None,
        performed_max : typing___Optional[int] = None,
        active : typing___Optional[bool] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> IntervalVarAssignment: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"active",u"duration_max",u"duration_min",u"end_max",u"end_min",u"performed_max",u"performed_min",u"start_max",u"start_min",u"var_id"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"active",b"active",u"duration_max",b"duration_max",u"duration_min",b"duration_min",u"end_max",b"end_max",u"end_min",b"end_min",u"performed_max",b"performed_max",u"performed_min",b"performed_min",u"start_max",b"start_max",u"start_min",b"start_min",u"var_id",b"var_id"]) -> None: ...

class SequenceVarAssignment(google___protobuf___message___Message):
    var_id = ... # type: typing___Text
    forward_sequence = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[int]
    backward_sequence = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[int]
    unperformed = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[int]
    active = ... # type: bool

    def __init__(self,
        *,
        var_id : typing___Optional[typing___Text] = None,
        forward_sequence : typing___Optional[typing___Iterable[int]] = None,
        backward_sequence : typing___Optional[typing___Iterable[int]] = None,
        unperformed : typing___Optional[typing___Iterable[int]] = None,
        active : typing___Optional[bool] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> SequenceVarAssignment: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"active",u"backward_sequence",u"forward_sequence",u"unperformed",u"var_id"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"active",b"active",u"backward_sequence",b"backward_sequence",u"forward_sequence",b"forward_sequence",u"unperformed",b"unperformed",u"var_id",b"var_id"]) -> None: ...

class WorkerInfo(google___protobuf___message___Message):
    worker_id = ... # type: int
    bns = ... # type: typing___Text

    def __init__(self,
        *,
        worker_id : typing___Optional[int] = None,
        bns : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> WorkerInfo: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"bns",u"worker_id"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"bns",b"bns",u"worker_id",b"worker_id"]) -> None: ...

class AssignmentProto(google___protobuf___message___Message):
    is_valid = ... # type: bool

    @property
    def int_var_assignment(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[IntVarAssignment]: ...

    @property
    def interval_var_assignment(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[IntervalVarAssignment]: ...

    @property
    def sequence_var_assignment(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[SequenceVarAssignment]: ...

    @property
    def objective(self) -> IntVarAssignment: ...

    @property
    def worker_info(self) -> WorkerInfo: ...

    def __init__(self,
        *,
        int_var_assignment : typing___Optional[typing___Iterable[IntVarAssignment]] = None,
        interval_var_assignment : typing___Optional[typing___Iterable[IntervalVarAssignment]] = None,
        sequence_var_assignment : typing___Optional[typing___Iterable[SequenceVarAssignment]] = None,
        objective : typing___Optional[IntVarAssignment] = None,
        worker_info : typing___Optional[WorkerInfo] = None,
        is_valid : typing___Optional[bool] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> AssignmentProto: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"objective",u"worker_info"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"int_var_assignment",u"interval_var_assignment",u"is_valid",u"objective",u"sequence_var_assignment",u"worker_info"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"objective",b"objective",u"worker_info",b"worker_info"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"int_var_assignment",b"int_var_assignment",u"interval_var_assignment",b"interval_var_assignment",u"is_valid",b"is_valid",u"objective",b"objective",u"sequence_var_assignment",b"sequence_var_assignment",u"worker_info",b"worker_info"]) -> None: ...
