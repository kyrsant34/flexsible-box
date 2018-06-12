from apps.common.models import AbstractParameterManager


class CalculationParametersManager(AbstractParameterManager):
    pass


class ResultParametersManager(AbstractParameterManager):
    pass


class ActionParametersManager(AbstractParameterManager):
    pass


__all__ = ['CalculationParametersManager', 'ResultParametersManager']
