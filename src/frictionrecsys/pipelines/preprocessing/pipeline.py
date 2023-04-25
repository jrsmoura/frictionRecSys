"""
This is a boilerplate pipeline 'preprocessing'
generated using Kedro 0.18.7
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import pre_processing


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=pre_processing,
            inputs="base_ano",
            outputs="preprocessed_base_ano",
            name="preprocess_ano_base_node"
        )
    ])
