import datetime
import dataclasses
import pandera as pa


class Table(pa.typing.DataFrame):
    
    start_time: pa.typing.Series[datetime.datetime]
    stop_time: pa.typing.Series[datetime.datetime]
    is_aud_go: pa.typing.Series[bool]
    is_aud_catch: pa.typing.Series[bool]


@dataclass
class Row:
    
    start_time: datetime.datetime
    stop_time: datetime.datetime
    is_aud_go: bool
    is_aud_catch: bool