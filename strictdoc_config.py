from strictdoc.core.project_config import ProjectConfig


def create_config() -> ProjectConfig:
    config = ProjectConfig(
        project_title="ScanBrother",
        include_doc_paths=[
            "/spec/**",
        ],
        project_features=[
            "TRACEABILITY_SCREEN",
            "DEEP_TRACEABILITY_SCREEN",
            "TABLE_SCREEN",
        ],
    )
    return config