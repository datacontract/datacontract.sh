import re

from ..lint import Linter, LinterResult
from datacontract.model.data_contract_specification import DataContractSpecification

class FieldPatternLinter(Linter):

    @property
    def name(self):
        return "Field pattern is correct regex"

    def lint_implementation(
        self,
        contract: DataContractSpecification
    ) -> LinterResult:
        result = LinterResult()
        for (model_name, model) in contract.models.items():
            for (field_name, field) in model.fields.items():
                if field.pattern:
                    try:
                        re.compile(field.pattern)
                    except re.error as e:
                        result = result.with_error(
                            f"Failed to compile pattern regex '{field.pattern}' for "
                            f"field '{field_name}' in model '{model_name}': {e.msg}"
                        )
        return result
