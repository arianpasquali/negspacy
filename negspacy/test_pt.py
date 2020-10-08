import pytest
import spacy
from negation import Negex
from spacy.pipeline import EntityRuler


def build_docs():
    docs = list()
    docs.append(
        (
            "Paciente nega a Apple Computers, mas tem Steve Jobs. Ele gosta dos EUA.",
            [("Apple Computers", True), ("Steve Jobs", False), ("EUA", False)],
        )
    )
    docs.append(
        (
            "Sem história dos EUA, Alemanha, Itália, Canadá ou Brasil",
            [
                ("EUA", True),
                ("Alemanha", True),
                ("Itália", True),
                ("Canadá", True),
                ("Brasil", True),
            ],
        )
    )

    docs.append(("Esse pode não ser Barack Obama.", [("Barack Obama", False)]))

    return docs    


def build_med_docs():
    docs = list()
    docs.append(
        (
            "O paciente nega doença cardiovascular, mas tem dores de cabeça. Sem história de tabagismo. Alcoolismo improvável. Fumar não está descartado.",
            [
                ("paciente nega", False),
                ("doença cardiovascular", True),
                ("dores de cabeça", False),
                ("Sem história", True),
                ("tabagismo", True),
                ("Alcoolismo", True),
                ("Fumar", False),
            ],
        )
    )
    docs.append(
        (
            "Sem histórico de cefaleias, prbc, tabagismo, refluxo ácido ou DRGE.",
            [
                ("Sem histórico", True),
                ("cefaleias", True),
                ("prbc", True),
                ("tabagismo", True),
                ("refluxo ácido", True),
                ("DRGE", True),
            ],
        )
    )

    docs.append(
        (
            "O alcoolismo não foi a causa da doença hepática.",
            [("alcoolismo", True), ("causa", False), ("doença hepática", False)],
        )
    )

    docs.append(
        (
            "Não houve dor de cabeça para este paciente.",
            [("Não houve dor de cabeça", True), ("paciente", True)],
        )
    )
    return docs


def test_pt():
    nlp = spacy.load("pt_core_news_sm")
    negex = Negex(nlp, language= "en")
    nlp.add_pipe(negex, last=True)
    docs = build_docs()
    for d in docs:
        doc = nlp(d[0])
        for i, e in enumerate(doc.ents):
            print(e.text, e._.negex)
            assert (e.text, e._.negex) == d[1][i]


def test_umls():
    nlp = spacy.load("pt_core_news_sm")
    negex = Negex(
        nlp, language="pt_clinical", ent_types=["ENTITY"], chunk_prefix=["não"]
    )
    nlp.add_pipe(negex, last=True)
    docs = build_med_docs()
    for d in docs:
        doc = nlp(d[0])
        for i, e in enumerate(doc.ents):
            print(e.text, e._.negex)
            assert (e.text, e._.negex) == d[1][i]


# def test_umls2():
#     # TODO pt_core_sci_sm
#     nlp = spacy.load("pt_core_sci_sm")
#     negex = Negex(
#         nlp, language="pt_clinical_sensitive", ent_types=["ENTITY"], chunk_prefix=["não"]
#     )
#     nlp.add_pipe(negex, last=True)
#     docs = build_med_docs()
#     for d in docs:
#         doc = nlp(d[0])
#         for i, e in enumerate(doc.ents):
#             print(e.text, e._.negex)
#             assert (e.text, e._.negex) == d[1][i]


# blocked by spacy 2.1.8 issue. Adding back after spacy 2.2.
# def test_no_ner():
#     nlp = spacy.load("en_core_web_sm", disable=["ner"])
#     negex = Negex(nlp)
#     nlp.add_pipe(negex, last=True)
#     with pytest.raises(ValueError):
#         doc = nlp("this doc has not been NERed")


def test_own_terminology():
    nlp = spacy.load("pt_core_news_sm")
    negex = Negex(nlp, language="pt", termination=["por causa do que"])
    nlp.add_pipe(negex, last=True)
    doc = nlp("Ele não gosta do que Steve Jobs por causa do que diz sobre Barack Obama.")
    assert doc.ents[1]._.negex == False


def test_get_patterns():
    nlp = spacy.load("pt_core_news_sm")
    negex = Negex(nlp, language="pt")
    patterns = negex.get_patterns()
    assert type(patterns) == dict
    assert len(patterns) == 4


def test_issue7():
    nlp = spacy.load("pt_core_news_sm")
    negex = Negex(nlp, language="pt")
    nlp.add_pipe(negex, last=True)
    ruler = EntityRuler(nlp)
    patterns = [{"label": "SOFTWARE", "pattern": "spacy"}]
    doc = nlp("fgfgdghgdh")


if __name__ == "__main__":
    test_pt()
    test_umls()
    test_own_terminology()
    test_get_patterns()
    test_issue7()
