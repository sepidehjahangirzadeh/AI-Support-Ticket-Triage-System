"""
Support Triaging Engine
 
Author: Sepideh Jahangirzadeh
"""

import re
import pandas as pd

from pathlib import Path

from app.core import logger


BASE_DIR = Path(__file__).resolve().parent.parent

RULES_PATH = (BASE_DIR/"data"/"preprocessing_rules.xlsx")


class TextCleaner:

    """
    Cleans and normalizes raw support ticket text.
    """

    def __init__(self):

        """
        Load preprocessing rules from Excel file.
        """

        try:
            self.df = pd.read_excel(RULES_PATH)

            self.df = self.df[self.df["enabled"] == 1]

            self.df = self.df.sort_values(by="priority")

            logger.info("Preprocessing rules loaded")

        except Exception as e:

            logger.exception("Failed loading rules")

            raise e

    def clean(self, text: str):
        """
        Remove noise and unwanted patterns from text.

        Args:
            text (str):
                Raw support ticket text.

        Returns:
            str:
                Cleaned ticket text.
        """

        try:
            text = text.lower()

            for _, row in self.df.iterrows():

                phrase = str(row["phrase"]).lower()

                is_regex = row["regex"]

                if is_regex:
                    text = re.sub(phrase, " ", text,)
                else:
                    pattern = (rf"\\b"
                               f"{re.escape(phrase)}"
                               rf"\\b")

                    text = re.sub(pattern, " ", text,)

            text = re.sub(r"\\s+", " ", text,)

            return text.strip()

        except Exception as e:

            logger.exception(
                "Preprocessing failed")

            raise e