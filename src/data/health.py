from configs.app_configs import get_config_env, app_config

class Health:
    status_dict = None

    def __init__(self,status='Starting',details='Application Starting'):
        self.status_dict = {
            'AppName': app_config.app_name,
            'Version': app_config.version,
            'Environment' : get_config_env(),
            # 'Model': model_config.get_model_file_name(),
            # 'Model_Version': model_config.model_version,
            'Status': status,
            'Dependency': None,
            'Details': details,
            # 'Prev_model': model_config.model_version
        }

    def update_status(self,status,details=None,dependency=None):
        self.status_dict['Status'] = status

        if dependency:
            self.status_dict['Dependency'] = dependency
        if details:
            self.status_dict['Details'] = details

    def get_health(self):
        return self.status_dict


health_status = Health()
