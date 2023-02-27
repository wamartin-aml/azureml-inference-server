import os
import sys

DEFAULT_APP_ROOT = "/var/azureml-app"
PACKAGE_ROOT = os.path.dirname(os.path.realpath(sys.modules[__package__].__file__))
SERVER_ROOT = os.path.join(PACKAGE_ROOT, "server")

DEFAULT_PORT = 5001
DEFAULT_HOST = "0.0.0.0"
DEFAULT_WORKER_COUNT = 1
DEFAULT_APPINSIGHTS_ENABLED = "false"
DEFAULT_WORKER_TIMEOUT_SECONDS = "300"
DEFAULT_WORKER_PRELOAD = "false"


# Environment Variables

ENV_AML_APP_ROOT = "AML_APP_ROOT"
ENV_AZUREML_ENTRY_SCRIPT = "AZUREML_ENTRY_SCRIPT"
ENV_AZUREML_MODEL_DIR = "AZUREML_MODEL_DIR"
ENV_AML_APP_INSIGHTS_ENABLED = "AML_APP_INSIGHTS_ENABLED"
ENV_AML_APP_INSIGHTS_KEY = "AML_APP_INSIGHTS_KEY"
ENV_WORKER_COUNT = "WORKER_COUNT"
ENV_WORKER_TIMEOUT = "WORKER_TIMEOUT"
ENV_WORKER_PRELOAD = "WORKER_PRELOAD"
ENV_PORT = "SERVER_PORT"
ENV_PREPOST = "PREPOST_SERVER"
ENV_BACKEND_TRANSPORT_PROTOCOL = "TRANSPORT_PROTOCOL"
ENV_AZUREML_SERVER_VERSION = "HTTP_X_MS_SERVER_VERSION"
ENV_AZUREML_SERVER_VERSION_ENABLED = "SERVER_VERSION_LOG_RESPONSE_ENABLED"
ENV_AML_CORS_ORIGINS = "AML_CORS_ORIGINS"
ENV_AZUREML_CONFIG_FILE = "AZUREML_CONFIG_FILE"
