"""
AgentFlight — Spec Schemas
Pydantic v2 models for OpenAPI / Swagger / JSON / YAML spec upload and analysis.
"""

from __future__ import annotations

from pydantic import BaseModel, Field


class NormalizedTool(BaseModel):
    """
    A single tool/operation extracted from an uploaded API spec,
    normalised to AgentFlight's internal tool representation.
    """

    name: str = Field(..., description="Tool / operation name.")
    description: str = Field(
        default="",
        description="Human-readable description of what the tool does.",
    )
    parameters: dict = Field(
        default_factory=dict,
        description="JSON-Schema compatible parameter definitions for the tool.",
    )


class SpecUploadResponse(BaseModel):
    """
    Response returned after a spec file is successfully uploaded and analysed.
    """

    spec_id: str = Field(..., description="Unique spec identifier (e.g. 'spec_7c3b5a2d0e1f').")
    filename: str = Field(..., description="Original filename of the uploaded spec.")
    extracted_tools: list[NormalizedTool] = Field(
        default_factory=list,
        description="Tools/operations extracted and normalised from the spec.",
    )
    raw_endpoints_count: int = Field(
        default=0,
        description="Total number of raw endpoints/paths found in the spec before normalisation.",
    )
