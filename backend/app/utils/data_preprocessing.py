import re
from typing import List, Dict

def preprocess_text(text: str) -> str:
    """
    Preprocess the input text by removing special characters and extra whitespace.
    
    Args:
    text (str): The input text to preprocess.
    
    Returns:
    str: The preprocessed text.
    """
    # Remove special characters
    text = re.sub(r'[^\w\s]', '', text)
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def truncate_text(text: str, max_length: int = 512) -> str:
    """
    Truncate the input text to a maximum length while preserving whole words.
    
    Args:
    text (str): The input text to truncate.
    max_length (int): The maximum length of the truncated text.
    
    Returns:
    str: The truncated text.
    """
    if len(text) <= max_length:
        return text
    return text[:max_length].rsplit(' ', 1)[0]

def format_ner_results(entities: List[Dict]) -> List[Dict]:
    """
    Format the NER results for consistent output.
    
    Args:
    entities (List[Dict]): The list of entities from the NER model.
    
    Returns:
    List[Dict]: The formatted list of entities.
    """
    formatted_entities = []
    for entity in entities:
        formatted_entity = {
            "text": entity.get("word", ""),
            "label": entity.get("entity_group", ""),
            "start": entity.get("start", 0),
            "end": entity.get("end", 0)
        }
        formatted_entities.append(formatted_entity)
    return formatted_entities

def calculate_model_performance(model_results: List[Dict]) -> Dict:
    """
    Calculate average performance metrics for a model.
    
    Args:
    model_results (List[Dict]): A list of dictionaries containing model results.
    
    Returns:
    Dict: A dictionary containing average performance metrics.
    """
    if not model_results:
        return {"avg_accuracy": 0, "avg_latency": 0}
    
    total_accuracy = sum(result.get("accuracy", 0) for result in model_results)
    total_latency = sum(result.get("latency", 0) for result in model_results)
    count = len(model_results)
    
    return {
        "avg_accuracy": total_accuracy / count,
        "avg_latency": total_latency / count
    }