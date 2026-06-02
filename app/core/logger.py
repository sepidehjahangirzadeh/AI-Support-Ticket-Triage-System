"""
Support Triaging Engine

Author: Sepideh Jahangirzadeh
"""

import logging

from app.core.elastic_log_handler import ElasticLogHandler


logger = logging.getLogger("support-triage")

logger.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")

elastic_handler = ElasticLogHandler()

elastic_handler.setFormatter(formatter)

logger.addHandler(elastic_handler)