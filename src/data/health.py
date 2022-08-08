from configs.app_configs import get_config_env, app_config
from configs.job_config import job_config


class Health:
    status_dict = None

    def __init__(self, status='Starting', details='Application Starting'):
        self.status_dict = {
            'AppName': app_config.app_name,
            'Version': app_config.version,
            'Environment': get_config_env(),
            'Status': status,
            'Dependency': None,
            'Connector': job_config.connector_type,
            'Details': details,
        }

    def update_status(self, status, details=None, dependency=None):
        self.status_dict['Status'] = status

        if dependency:
            self.status_dict['Dependency'] = dependency
        if details:
            self.status_dict['Details'] = details

    def get_health(self):
        return self.status_dict


health_status = Health()
