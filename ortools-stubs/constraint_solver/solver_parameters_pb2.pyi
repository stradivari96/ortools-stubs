# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)

from google.protobuf.internal.enum_type_wrapper import (
    _EnumTypeWrapper as google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    NewType as typing___NewType,
    Optional as typing___Optional,
    Text as typing___Text,
    Union as typing___Union,
    cast as typing___cast,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int
if sys.version_info < (3,):
    builtin___buffer = buffer
    builtin___unicode = unicode


DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class ConstraintSolverParameters(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    TrailCompressionValue = typing___NewType('TrailCompressionValue', builtin___int)
    type___TrailCompressionValue = TrailCompressionValue
    TrailCompression: _TrailCompression
    class _TrailCompression(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[ConstraintSolverParameters.TrailCompressionValue]):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        NO_COMPRESSION = typing___cast(ConstraintSolverParameters.TrailCompressionValue, 0)
        COMPRESS_WITH_ZLIB = typing___cast(ConstraintSolverParameters.TrailCompressionValue, 1)
    NO_COMPRESSION = typing___cast(ConstraintSolverParameters.TrailCompressionValue, 0)
    COMPRESS_WITH_ZLIB = typing___cast(ConstraintSolverParameters.TrailCompressionValue, 1)
    type___TrailCompression = TrailCompression

    compress_trail: type___ConstraintSolverParameters.TrailCompressionValue = ...
    trail_block_size: builtin___int = ...
    array_split_size: builtin___int = ...
    store_names: builtin___bool = ...
    name_cast_variables: builtin___bool = ...
    name_all_variables: builtin___bool = ...
    profile_propagation: builtin___bool = ...
    profile_file: typing___Text = ...
    profile_local_search: builtin___bool = ...
    print_local_search_profile: builtin___bool = ...
    trace_propagation: builtin___bool = ...
    trace_search: builtin___bool = ...
    print_model: builtin___bool = ...
    print_model_stats: builtin___bool = ...
    print_added_constraints: builtin___bool = ...
    disable_solve: builtin___bool = ...
    use_small_table: builtin___bool = ...
    use_cumulative_edge_finder: builtin___bool = ...
    use_cumulative_time_table: builtin___bool = ...
    use_cumulative_time_table_sync: builtin___bool = ...
    use_sequence_high_demand_tasks: builtin___bool = ...
    use_all_possible_disjunctions: builtin___bool = ...
    max_edge_finder_size: builtin___int = ...
    diffn_use_cumulative: builtin___bool = ...
    use_element_rmq: builtin___bool = ...
    skip_locally_optimal_paths: builtin___bool = ...
    check_solution_period: builtin___int = ...

    def __init__(self,
        *,
        compress_trail : typing___Optional[type___ConstraintSolverParameters.TrailCompressionValue] = None,
        trail_block_size : typing___Optional[builtin___int] = None,
        array_split_size : typing___Optional[builtin___int] = None,
        store_names : typing___Optional[builtin___bool] = None,
        name_cast_variables : typing___Optional[builtin___bool] = None,
        name_all_variables : typing___Optional[builtin___bool] = None,
        profile_propagation : typing___Optional[builtin___bool] = None,
        profile_file : typing___Optional[typing___Text] = None,
        profile_local_search : typing___Optional[builtin___bool] = None,
        print_local_search_profile : typing___Optional[builtin___bool] = None,
        trace_propagation : typing___Optional[builtin___bool] = None,
        trace_search : typing___Optional[builtin___bool] = None,
        print_model : typing___Optional[builtin___bool] = None,
        print_model_stats : typing___Optional[builtin___bool] = None,
        print_added_constraints : typing___Optional[builtin___bool] = None,
        disable_solve : typing___Optional[builtin___bool] = None,
        use_small_table : typing___Optional[builtin___bool] = None,
        use_cumulative_edge_finder : typing___Optional[builtin___bool] = None,
        use_cumulative_time_table : typing___Optional[builtin___bool] = None,
        use_cumulative_time_table_sync : typing___Optional[builtin___bool] = None,
        use_sequence_high_demand_tasks : typing___Optional[builtin___bool] = None,
        use_all_possible_disjunctions : typing___Optional[builtin___bool] = None,
        max_edge_finder_size : typing___Optional[builtin___int] = None,
        diffn_use_cumulative : typing___Optional[builtin___bool] = None,
        use_element_rmq : typing___Optional[builtin___bool] = None,
        skip_locally_optimal_paths : typing___Optional[builtin___bool] = None,
        check_solution_period : typing___Optional[builtin___int] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ConstraintSolverParameters: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ConstraintSolverParameters: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"array_split_size",b"array_split_size",u"check_solution_period",b"check_solution_period",u"compress_trail",b"compress_trail",u"diffn_use_cumulative",b"diffn_use_cumulative",u"disable_solve",b"disable_solve",u"max_edge_finder_size",b"max_edge_finder_size",u"name_all_variables",b"name_all_variables",u"name_cast_variables",b"name_cast_variables",u"print_added_constraints",b"print_added_constraints",u"print_local_search_profile",b"print_local_search_profile",u"print_model",b"print_model",u"print_model_stats",b"print_model_stats",u"profile_file",b"profile_file",u"profile_local_search",b"profile_local_search",u"profile_propagation",b"profile_propagation",u"skip_locally_optimal_paths",b"skip_locally_optimal_paths",u"store_names",b"store_names",u"trace_propagation",b"trace_propagation",u"trace_search",b"trace_search",u"trail_block_size",b"trail_block_size",u"use_all_possible_disjunctions",b"use_all_possible_disjunctions",u"use_cumulative_edge_finder",b"use_cumulative_edge_finder",u"use_cumulative_time_table",b"use_cumulative_time_table",u"use_cumulative_time_table_sync",b"use_cumulative_time_table_sync",u"use_element_rmq",b"use_element_rmq",u"use_sequence_high_demand_tasks",b"use_sequence_high_demand_tasks",u"use_small_table",b"use_small_table"]) -> None: ...
type___ConstraintSolverParameters = ConstraintSolverParameters
