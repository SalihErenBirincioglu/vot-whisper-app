import re
from snowballstemmer import TurkishStemmer
from exceptions import TranscribeException
from utils.stopwords import STOPWORDS

_stemmer = TurkishStemmer()

def normalize(text: str) -> str:
    try:
        text = text.lower()
        text = re.sub(r"[^a-zçğıöşü\s]", "", text)

        words = text.split()
        processed = []

        for w in words:
            if w in STOPWORDS:
                continue
            stem = _stemmer.stemWord(w)
            processed.append(stem)

        return " ".join(processed)

    except Exception:
        raise TranscribeException(
            "NLP_FAILED",
            "Text normalization failed"
        )
