from wbpy.climate import ClimateAPI
from wbpy.climate import InstrumentalDataset
from wbpy.climate import ModelledDataset
from wbpy.indicators import IndicatorAPI
from wbpy.indicators import IndicatorDataset

__name__ = "wbpy"
__version__ = "2.0.1"
__email__ = "matt@mattduck.com"
__maintainer__ = "Matthew Duck"
__license__ = "MIT"

__all__ = [
    IndicatorAPI,
    IndicatorDataset,
    ClimateAPI,
    InstrumentalDataset,
    ModelledDataset,
]
