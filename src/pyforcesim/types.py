from typing import NewType, TypeAlias, Literal, Final

from plotly.graph_objs._figure import Figure

# ** common
LoggingLevels: TypeAlias = Literal[
    'DEBUG',
    'INFO',
    'WARNING',
    'ERROR',
    'CRITICAL',
]
PlotlyFigure: TypeAlias = Figure

# ** simulation
SystemID = NewType('SystemID', int)
CustomID = NewType('CustomID', str)
LoadID = NewType('LoadID', int)
Infinite: TypeAlias = float

# infinity
INF: Final[Infinite] = float('inf')



