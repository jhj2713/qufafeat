from featuretools.variable_types.variable import (
    Numeric,
    Datetime
)


_typestr_to_mkfeat = {
    "date": "date",
    "datetime": "date",
    "numeric": "number",
    "ordinal": "number",
    "boolean": "bool",
    "categorical": "class",
}


class FeatureHelper:
    def __init__(self, features):
        self._features = features

    def to_array(self):
        arr = []
        for feature in self._features:
            arr.append([feature.get_name(), self._convert_mkfeat_type_string(feature.variable_type)])
        return arr

    @staticmethod
    def _convert_mkfeat_type_string(vartype):
        typestr = vartype.type_string
        if typestr in _typestr_to_mkfeat:
            return _typestr_to_mkfeat[typestr]
        return "string"
