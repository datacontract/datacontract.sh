from abc import ABC, abstractmethod
from enum import Enum
import typing

from datacontract.model.data_contract_specification import DataContractSpecification
from datacontract.export.avro_idl_converter import AvroIDLExporter, AvroIdlExporter
from datacontract.export.bigquery_converter import BigQueryExporter
from datacontract.export.dbml_converter import DBMLExporter, DbmlExporter
from datacontract.export.dbt_converter import DBTExporter, DBTSourceExporter, DBTStageExporter, DbtExporter, DbtSourceExporter, DbtStageExporter
from datacontract.export.exporter import ExportFormat, FactoryExporter
from datacontract.export.avro_converter import AvroExporter
from datacontract.export.go_converter import GOExporter, GoExporter
from datacontract.export.great_expectations_converter import GreateExpectationsExporter
from datacontract.export.html_export import HtmlExporter
from datacontract.export.jsonschema_converter import JsonSchemaExporter
from datacontract.export.odcs_converter import ODCSExporter, OdcsExporter
from datacontract.export.protobuf_converter import ProtoBufExporter
from datacontract.export.pydantic_converter import PydanticExporter
from datacontract.export.rdf_converter import RDFExporter, RdfExporter
from datacontract.export.sodacl_converter import SodaExporter
from datacontract.export.sql_converter import SqlExporter, SqlQueryExporter
from datacontract.export.terraform_converter import TerraformExporter


class Exporter(ABC):
    @abstractmethod
    def export(self, export_args) -> dict:
        pass


class ExportFormat(str, Enum):
    jsonschema = "jsonschema"
    pydantic_model = "pydantic-model"
    sodacl = "sodacl"
    dbt = "dbt"
    dbt_sources = "dbt-sources"
    dbt_staging_sql = "dbt-staging-sql"
    odcs = "odcs"
    rdf = "rdf"
    avro = "avro"
    protobuf = "protobuf"
    great_expectations = "great-expectations"
    terraform = "terraform"
    avro_idl = "avro-idl"
    sql = "sql"
    sql_query = "sql-query"
    html = "html"
    go = "go"
    bigquery = "bigquery"
    dbml = "dbml"


class ExporterFactory:
    def __init__(self):
        self.dict_exporters = {}

    def register_exporter(self, name, exporter):
        self.dict_exporters.update({name: exporter})

    def create(self, name) -> Exporter:
        try:
            return self.dict_exporters[name]()
        except:
            raise Exception(f"Export format {name} not supported.")



exporter_factory = ExporterFactory()
exporter_factory.register_exporter(ExportFormat.avro, AvroExporter)
exporter_factory.register_exporter(ExportFormat.avro_idl, AvroIdlExporter)
exporter_factory.register_exporter(ExportFormat.bigquery, BigQueryExporter)
exporter_factory.register_exporter(ExportFormat.dbml, DbmlExporter)
exporter_factory.register_exporter(ExportFormat.rdf, RdfExporter)
exporter_factory.register_exporter(ExportFormat.dbt, DbtExporter)
exporter_factory.register_exporter(ExportFormat.dbt_sources, DbtSourceExporter)
exporter_factory.register_exporter(ExportFormat.dbt_staging_sql, DbtStageExporter)
exporter_factory.register_exporter(ExportFormat.jsonschema, JsonSchemaExporter)
exporter_factory.register_exporter(ExportFormat.odcs, OdcsExporter)
exporter_factory.register_exporter(ExportFormat.go, GoExporter)
exporter_factory.register_exporter(ExportFormat.great_expectations, GreateExpectationsExporter)
exporter_factory.register_exporter(ExportFormat.html, HtmlExporter)
exporter_factory.register_exporter(ExportFormat.protobuf, ProtoBufExporter)
exporter_factory.register_exporter(ExportFormat.pydantic_model, PydanticExporter)
exporter_factory.register_exporter(ExportFormat.sodacl, SodaExporter)
exporter_factory.register_exporter(ExportFormat.sql, SqlExporter)
exporter_factory.register_exporter(ExportFormat.sql_query, SqlQueryExporter)
exporter_factory.register_exporter(ExportFormat.terraform, TerraformExporter)
 
