"""
Default termsets for various languages
"""

from .termsets_en import en, en_clinical, en_clinical_sensitive
from .termsets_pt import pt, pt_clinical, pt_clinical_sensitive

LANGUAGES = dict()

LANGUAGES["en"] = en
LANGUAGES["en_clinical"] = en_clinical
LANGUAGES["en_clinical_sensitive"] = en_clinical_sensitive

LANGUAGES["pt"] = pt
LANGUAGES["pt_clinical"] = pt_clinical
LANGUAGES["pt_clinical_sensitive"] = pt_clinical_sensitive
