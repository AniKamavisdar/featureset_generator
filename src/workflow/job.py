import datetime

from configs.job_config import job_config
from configs.app_configs import app_config


def initialize(config=job_config):
    connector = config.connector
    transformer = config.transformer
    extractor = config.extractor
    connector.connect()
    transformer.load_transformer()
    return connector, extractor, transformer


def extract(config=job_config):
    connector, extractor, transformer = initialize(config)
    return get_features(connector, extractor, transformer)


def extract_and_save(config=job_config):
    file_name = (app_config.app_name + "_" +
                 app_config.version + "_" +
                 datetime.datetime.strftime(datetime.datetime.today(), '%Y%m%d_%H%M%S')+ ".csv")
    connector, extractor, transformer = initialize(config)
    data = get_features(connector, extractor, transformer)
    print(f"Saving to file {file_name}")
    data.to_csv(job_config.PATH+f"/{file_name}")
    return {"Total Data Extracted": data.shape}

def get_features(connector, extractor, transformer):
    """
    Function puts together all the individual components and extracts data in one go.
    :param connector: A Connector type object to be passed, which can be used to connect to source of data
    :param extractor: Extractor type object to be passed, which holds to logic to fetch data from source
    :param transformer: Transformer type object to be passed, which holds logic to transform data into feature.
    :return: Feature Set Extract / Saves to file and returns status code.
    """
    return transformer.transformer_object.transform(connector.run(extractor.ext_logic))
