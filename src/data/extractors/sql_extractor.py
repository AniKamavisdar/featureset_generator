from data.extractors.base import Extractor


class SQLExtractor(Extractor):
    def __init__(self):
        super().__init__('sql_extractor')
        self.ext_logic = None

    def set_sql(self, query):
        self.ext_logic = query

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
