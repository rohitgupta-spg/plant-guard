import litellm, json, logging
from pydantic import ValidationError
from core.util.config import settings
from core.util.logging import setup_custom_logger


# First thing, Setup logging
log = setup_custom_logger(__name__, log_level=logging.DEBUG)


SYSTEM = """Extract a MaintenanceEvent from the alarm/log text.
Never invent values. If something is not stated, leave it null and list it in missing_fields.
If the operator's words contradict the numeric readings, keep both and note it in missing_fields."""

def extract(model_cls, text: str, model: str = settings.llm_model, retries: int = 2):
    log.debug("Now extracting maintenance log from event received")

    messages = [{"role": "system", "content": SYSTEM},
                {"role": "user", "content": text}]

    for _ in range(retries + 1):
        resp = litellm.completion(model=model,
                                  messages=messages,
                                  response_format=model_cls,
                                  temperature=0)
        raw = resp.choices[0].message.content
        try:
            return model_cls.model_validate_json(raw)
        except ValidationError as e:   # feed the error back to the model
            messages += [{"role": "assistant", "content": raw},
                         {"role": "user", "content": f"Invalid: {e}. Return corrected JSON only."}]
            log.error(f"Invalid JSON: {raw}")
    raise ValueError(f"Extraction failed after {retries} retries")