"""Helper utility to determine which model variant templates and rewards to use."""

def get_model_variant(model_path: str) -> str:
    """
    Determine which model variant to use based on model path.
    
    Args:
        model_path: The model path (e.g., "deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B")
    
    Returns:
        "deepseek" if model is DeepSeek-R1-Distill-Qwen-1.5B
        "default" for Qwen2.5-Math-1.5B, Qwen3-1.7B and others
    """
    if model_path and "DeepSeek-R1-Distill-Qwen-1.5B" in str(model_path):
        return "deepseek"
    return "default"


def should_use_deepseek_variant(model_path: str) -> bool:
    """
    Check if the model should use DeepSeek variant templates and rewards.
    
    Args:
        model_path: The model path string to check
        
    Returns:
        True if DeepSeek-R1-Distill-Qwen-1.5B should be used, False otherwise
    """
    return get_model_variant(model_path) == "deepseek"
