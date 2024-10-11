# End-to-End-DL-MLflow-DVC-Project


## Workflows

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the dvc.yaml


## MLflow

- [Documentation](https://mlflow.org/docs/latest/index.html)

- [MLflow tutorial](https://youtube.com/playlist?list=PLkz_y24mlSJZrqiZ4_cLUiP0CBN5wFmTb&si=zEp_C8zLHt1DzWKK)

##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/sumanthkalahari/End-to-End-DL-MLflow-DVC-Project.mlflow \
MLFLOW_TRACKING_USERNAME=sumanthkalahari \
MLFLOW_TRACKING_PASSWORD=4445e55343d3a276ac4a6eef7a52e165dde225b8 \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/sumanthkalahari/End-to-End-DL-MLflow-DVC-Project.mlflow

export MLFLOW_TRACKING_USERNAME=sumanthkalahari 

export MLFLOW_TRACKING_PASSWORD=4445e55343d3a276ac4a6eef7a52e165dde225b8

```