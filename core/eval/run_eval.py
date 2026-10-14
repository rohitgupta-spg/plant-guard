import time

import pandas as pd, logging
from core.util.config import settings
from core.eval.adapter import pipeline
from core.util.logging import setup_custom_logger


# First thing, Setup logging
log = setup_custom_logger(__name__, log_level=logging.DEBUG)


def run():
    log.debug(f"Kick starting the evaluation of golden set to validate application behaviour")

    gold = pd.read_json(settings.evaluation_set)
    rows = []

    for _, g in gold.iterrows():
        log.debug(f"Now running pipeline for question: {g['question']}")
        out = pipeline(g.question)                      # includes answer, route, citations

        log.debug(f"Here is the response received from the pipeline run: {str(out)}")
        rows.append({"id": g.id,
                     "category": g.category,
                     "actual_route": out["result"],
                     "expected_route": g.expected_route,
                     "route_ok": out["result"] == g.expected_route,
                     "citations": out["recommendation"]["citations"],
                     "cite_ok": all(c in out["recommendation"]["citations"] for c in str(g.must_cite).split(";") if c and c != "nan"),
                     # "clean": str(g.must_not_contain) not in out["recommendation"]["action"] if pd.notna(g.must_not_contain) else True
                     })
        time.sleep(3)   # ToDo: Hardcoded rate limiting; Update with back-off and conditional (upon 429 failures)

    df = pd.DataFrame(rows)
    print(df.to_markdown())
    df["pass"] = df.route_ok & df.cite_ok #& df.clean
    print(df.groupby("category")["pass"].mean())
    return df
