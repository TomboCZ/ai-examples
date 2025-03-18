from enum import Enum
from dataclasses import dataclass

@dataclass(frozen=True)
class ModelInfo:
    """
    Holds information about an AI model.
    
    Attributes:
        exact_name (str): The precise name used for API calls
        open_source (bool): Whether the model is open source
    """
    exact_name: str
    open_source: bool

class Model(Enum):
    """
    Enumeration of available AI models.
    
    Each model is configured with its exact API name and open source status.
    """
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

    @classmethod
    def get_model_by_name(cls, name: str) -> 'Model':
        """
        Get a Model instance by its name or exact_name.
        
        Args:
            name (str): The name to look up
            
        Returns:
            Model: The matching Model instance
            
        Raises:
            ValueError: If no matching model is found
        """
        for model in cls:
            if name.lower() in (model.name.lower(), model.exact_name.lower()):
                return model
        raise ValueError(f"No model found for name: {name}")

    @classmethod
    def get_open_source_models(cls) -> list['Model']:
        """Returns a list of all open source models."""
        return [model for model in cls if model.is_open_source]

    @classmethod
    def get_closed_source_models(cls) -> list['Model']:
        """Returns a list of all closed source models."""
        return [model for model in cls if not model.is_open_source]

# Example
if __name__ == "__main__":
    # Print all models
    print("\nAvailable Models:")
    for model in Model:
        print(f"- {model.name}: {model.exact_name} (Open Source: {model.is_open_source})")
    
    # Print model groups
    print("\nOpen Source Models:")
    for model in Model.get_open_source_models():
        print(f"- {model.name}")
    
    # Test model lookup
    try:
        model = Model.get_model_by_name("gpt-4o")
        print(f"\nFound model: {model.name}")
    except ValueError as e:
        print(f"\nError: {e}")
