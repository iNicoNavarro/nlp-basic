#!/usr/bin/env python

from nlp_logic.core import get_phrases
import fire


if __name__ == "__main__":
    TEXT: str = "NBA"
    fire.Fire(get_phrases)
