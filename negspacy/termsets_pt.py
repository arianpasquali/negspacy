"""
Default termsets for various languages
"""



# portuguese termset dictionary
pt = dict()
pseudo = [
'não mais',
'não é capaz de ser',
'não está certo se',
'não necessariamente',
'sem mais',
'sem dificuldade',
'talvez não',
'não só',
'sem aumento',
'sem alterações significativas',
'sem alterações',
'sem alterações definitivas',
'não alargar',
'não causa',
'não está certo se'
]
pt["pseudo_negations"] = pseudo

preceding = [
    "inexistência de",
    "ausência de",
    'declinado',
    'negado',
    'nega',
    'negação',
    'nenhum sinal de',
    'sem sinais de',
    'não',
    'não demonstrar',
    'sintomas atípicos',
    'dúvida',
    'negativo para',
    'sem',
    'não faz isso.',
    'não',
    'não faças isso',
    'não estava',
    'não estavam',
    'não é',
    'não estão',
    'não pode',
    'não posso.',
    'não pode',
    'não podia',
    'não foi possível',
    'nunca'
]
pt["preceding_negations"] = preceding

following = [
    'declinado',
    'improvável',
    'não foi',
    'não foram',
    'não estava',
    'não estavam'
]
pt["following_negations"] = following

termination = [
    'embora',
    'com excepção de',
    'tal como existem',
    'para além de',
    'mas',
    'excepto',
    'entretanto',
    'que envolvem',
    'apesar disso',
    'ainda',
    'apesar de',
    'ainda'
]
pt["termination"] = termination


# pt_clinical builds upon en
pt_clinical = dict()
pseudo_clinical = pseudo + [
    'negativo',
    'não descartar',
    'não excluído',
    'não foram excluídos',
    'não drenar',
    'sem alterações suspeitas',
    'sem alteração do intervalo',
    'sem alteração significativa do intervalo',
]
pt_clinical["pseudo_negations"] = pseudo_clinical

preceding_clinical = preceding + [
    'o paciente não foi',
    'sem indicação de',
    'sem sinal de',
    'sem sinais de',
    'sem quaisquer reacções ou sinais de',
    'sem queixas de',
    'não há provas de',
    'nenhuma causa de',
    'avaliar para',
    'não consegue revelar',
    'isentos de',
    'nunca desenvolvidos',
    'nunca tive',
    'não expôs',
    'exclui',
    'descartar',
    'descarta-o',
    'descarte-a',
    'descartar o paciente',
    'descartar o paciente',
    'excluídos',
    'rejeitou-o rejeitou-a',
    'doentes excluídos do tratamento',
    'rejeitou o paciente',
]
pt_clinical["preceding_negations"] = preceding_clinical

following_clinical = following + ["foi descartado", "foram descartados", "livre"]
pt_clinical["following_negations"] = following_clinical

termination_clinical = termination + [
    'causa de',
'causa de',
'causas de',
'causas de',
'etiologia para',
'etiologia da',
'origem para',
'Origem da',
'originárias para',
'originárias de',
'outras possibilidades de',
'razão para',
'razão de',
'Razões de',
'razões de',
'secundária a',
'fonte para',
'fontes para',
'fontes de',
'evento de desencadeamento para',
]
pt_clinical["termination"] = termination_clinical



pt_clinical_sensitive = dict()

preceding_clinical_sensitive = preceding_clinical + [
    'preocupação com',
    'suposto',
    'que causam',
    'leva a',
    'h/o',
    'histórico de',
    'em vez de',
    'se sentir',
    'se tiver',
    'ensino do paciente',
    'ensinou ao paciente',
    'ensinar ao paciente',
    'educado o paciente',
    'educar o paciente',
    'monitorizado para',
    'monitorar para',
    'ensaio de',
    'ensaios para',
]
pt_clinical_sensitive["pseudo_negations"] = pseudo_clinical
pt_clinical_sensitive["preceding_negations"] = preceding_clinical_sensitive
pt_clinical_sensitive["following_negations"] = following_clinical
pt_clinical_sensitive["termination"] = termination_clinical

LANGUAGES = dict()
LANGUAGES["pt"] = pt
LANGUAGES["pt_clinical"] = pt_clinical
LANGUAGES["pt_clinical_sensitive"] = pt_clinical_sensitive
