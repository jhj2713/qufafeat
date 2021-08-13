import pandas as pd

from .error import Error


_mkfeat_typestr_to_converter = {
    "number": pd.to_numeric,
    "date": pd.to_datetime
}


class ColumnSpec:
    """
    컬럼명이나 유형과 관련된 정보를 처리하는 목적의 클래스. 현재는 컬럼명에 대한 정보를 처리하는 기능만 구현됨
    """
    def __init__(self, columns):
        self.columns = columns

    def validate(self):
        """
        Column 정의에 대한 검증. 모든 컬럼에 name, type이 정의되어 있는지, key가 전체 컬럼에 1개 정의, label이 정의된 컬럼이 1개
        혹은 정의되지 않았는지를 확인함
        Returns:
            :class:.Error: column 정의가 문제 없는 경우 OK반환. 그렇지 않으면 해당하는 오류값 반환.
        """
        has_key = False
        has_label = False
        for colinfo in self.columns:
            if 'name' not in colinfo or 'type' not in colinfo:
                return Error.ERR_COLUMN_HAS_NO_NAME_OR_TYPE
            if 'key' in colinfo:
                if colinfo['key']:
                    if has_key:
                        return Error.ERR_COLUMN_MULTI_KEY
                    if 'label' in colinfo and colinfo['label']:
                        return Error.ERR_COLUMN_KEY_AND_LABEL
                    has_key = True
            if 'label' in colinfo:
                if colinfo['label']:
                    if has_label:
                        return Error.ERR_COLUMN_MULTI_LABEL
                    has_label = True
        if not has_key:
            return Error.ERR_COLUMN_NO_KEY
        return Error.OK

    def get_colnames(self):
        """
        컬럼명 배열을 반환. pandas의 read_csv() 함수 전달 인자를 쉽게 생성하기 위함

        Returns:
            컬럼명으로 구성된 배열
        """
        colnames = []
        for colinfo in self.columns:
            colnames.append(colinfo['name'])
        return colnames

    def get_converters(self):
        converters = {}
        for colinfo in self.columns:
            converter = self._get_converter_from_strtype(colinfo['type'])
            if converter is not None:
                converters[colinfo['name']] = converter
        return converters

    def get_key_colname(self):
        """
        특징 추출시 id로 지정가능한 컬럼명 반환. key로 지정된 column명이 없는 경우 첫번째 컬럼명 반환

        Returns:
            id로 지정 가능한 column name.
        """
        for colinfo in self.columns:
            if 'key' in colinfo and colinfo['key']:
                return colinfo['name']
        return self.columns[0]['name']

    def get_label_colname(self):
        for colinfo in self.columns:
            if 'label' in colinfo and colinfo['label']:
                return colinfo['name']
        return None

    @staticmethod
    def _get_converter_from_strtype(typestr):
        if typestr in _mkfeat_typestr_to_converter:
            return _mkfeat_typestr_to_converter[typestr]
        return None