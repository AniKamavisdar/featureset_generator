from data.extractors.base import Extractor


class SQLExtractor(Extractor):
    def __init__(self):
        super().__init__('sql_extractor')

    def set_ext_logic(self, file_name):
        with open(file_name, 'r') as f:
            self.ext_logic = f.read()

    def create_sql(self, params_dict):
        """
        This Method will create SQL based on the params dictionary that is passed

        Dictionary structure:
        {
        'cols': columns, 'tables': {'primary': tablename, 'inner' tablename},
        'joins': joins_lists, 'filter': filter_dict, 'sort': sort_values,
        'aggregator': aggregator_columns, 'aggregates': {column: agg_type... }
        'aggregate_filter' : filter_dict
        }

        :param params_dict:
        :return:
        """
        pass
