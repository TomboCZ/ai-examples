from enum import Enum
from dataclasses import dataclass

@dataclass(frozen=True)
class ModelInfo:
    exact_name: str
    open_source: bool

class Model(Enum):
    GPT_4O = ModelInfo(exact_name="gpt-4o", open_source=False)
    GPT_4O_MINI = ModelInfo(exact_name="gpt-4o-mini", open_source=False)
    LLAMA_32_8B = ModelInfo(exact_name="llama-3.2-3b-instruct", open_source=True)
    DEEP_SEEK_R1_8B = ModelInfo(exact_name="deepseek-r1-distill-llama-8b", open_source=True)

    @property
    def exact_name(self) -> str:
        """Returns the exact name of the model directly from the Model instance."""
        return self.value.exact_name

    @property
    def is_open_source(self) -> bool:
        """Returns the open source flag directly from the Model instance."""
        return self.value.open_source

# Example
if __name__ == "__main__":
    print(f"Model {Model.GPT_4O_MINI.name} has the exact name: {Model.GPT_4O_MINI.exact_name} and open_source={Model.GPT_4O_MINI.is_open_source}")
    print(f"Model {Model.LLAMA_32_8B.name} has the exact name: {Model.LLAMA_32_8B.exact_name} and open_source={Model.LLAMA_32_8B.is_open_source}")
