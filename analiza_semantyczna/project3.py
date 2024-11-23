from verbs_table import verbs, zaimki, verbs_irregular

with open('swannsway.txt', 'r', encoding='utf-8') as file:
    text = file.read()

words = text.split()
irregular_verb_forms = {form for sublist in verbs_irregular for form in sublist}
verb_noun_dict = {}


def get_base_form(word, regular_verbs, irregular_verbs):
    base_form = word.rstrip('s').rstrip('ed').rstrip('ing')
    if base_form in regular_verbs:
        return base_form
    for sublist in irregular_verbs:
        if word in sublist:
            return sublist[0] 
    return None


def is_noun(word):
    return word.lower() not in zaimki and word.isalpha()

for i, word in enumerate(words):
    base_form = get_base_form(word.lower(), verbs, verbs_irregular)

    if base_form:
        if i + 1 < len(words):
            next_word = words[i + 1]
            if next_word.lower() in zaimki and i + 2 < len(words):
                next_word = words[i + 2]
            if is_noun(next_word):
                if base_form not in verb_noun_dict:
                    verb_noun_dict[base_form] = set() 
                verb_noun_dict[base_form].add(next_word) 

for verb, nouns in verb_noun_dict.items():
    print(f"{verb}: {list(nouns)}")  
