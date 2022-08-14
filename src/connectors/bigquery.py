from connectors.base import DBConnector

from google.cloud import bigquery as bq


class BigQuery(DBConnector):

    def __init__(self):
        try:
            super().__init__('big_query')
        except Exception as err:
            raise Exception(f"Error while creating connection string for Bigquery, following is the error\n{str(err)}")

    def __make_connection_string(self):
        pass

    def __create_connection_object(self):
        pass

    def connect(self):
        try:
            if not self.connection_obj:
                self.connection_obj = bq.Client()
        except Exception as err:
            raise err

    def disconnect(self):
        self.connection_obj = self.connection_obj.close()

    def run(self, query_):
        return self.connection_obj.query(query_).to_dataframe()

    # Connecting via individual params
    # def connect(self, params):
    #     self.logger.info(f"Connect: Connecting...")
    #     self.client = bigquery.Client(
    #         project=params.get(Input.PROJECT_ID),
    #         credentials=service_account.Credentials.from_service_account_info({
    #             "type": "service_account",
    #             "project_id": params.get(Input.PROJECT_ID),
    #             "private_key_id": params.get(Input.PRIVATE_KEY_ID),
    #             "private_key": params.get(Input.PRIVATE_KEY).get("privateKey").replace('\\n', "\n", -1),
    #             "client_email": params.get(Input.CLIENT_EMAIL),
    #             "client_id": params.get(Input.CLIENT_ID),
    #             "auth_uri": params.get(Input.AUTH_URI),
    #             "client_x509_cert_url": params.get(Input.CLIENT_X509_CERT_URL),
    #             "token_uri": params.get(Input.TOKEN_URI, "https://oauth2.googleapis.com/token"),
    #             "auth_provider_x509_cert_url": params.get(Input.AUTH_PROVIDER_X509_CERT_URL,
    #                                                       "https://www.googleapis.com/oauth2/v1/certs")
    #         })
    #     )
