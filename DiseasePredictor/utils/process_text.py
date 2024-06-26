import re

import inflect
import pandas as pd
from spellchecker import SpellChecker
from utils.cosine_similarity_calculation import cosine_similarity_calc
from utils.vector_generation import generate_similarity_based_vector

from .stop_words import stop_words

df = pd.read_csv("./datasets/Training.csv")


columns = df.columns[:-2]


def remove_duplicate_words(sentence):
    unique_sentence = []
    for word in sentence.split():
        if word not in unique_sentence:
            unique_sentence.append(word)
    new_sentence = " ".join(unique_sentence)
    return new_sentence


def remove_stop_words(sentence):
    new_word_list = []
    p = inflect.engine()
    unique_sentence = remove_duplicate_words(sentence)
    sentence = fix_wrong_words(unique_sentence)
    # split if the , or space is found in the sentence
    splitted_words = re.split(r"[,\s]+", sentence.strip().lower())
    # splitted_words = sentence.strip().lower().split()
    for word_ in splitted_words:
        if word_ not in stop_words:
            word = p.singular_noun(word_)
            if word:
                cleaned_word = remove_numbers_specials(word)
                new_word_list.append(cleaned_word)
            else:
                new_word_list.append(
                    remove_numbers_specials(word_))
    return [i for i in new_word_list if i]


def convert_to_verb1(word):
    pattern = r"ing$"
    base_verb = re.sub(pattern, "", word)
    return base_verb


def remove_numbers_specials(word):
    pattern = r"[^a-zA-Z]"
    if re.match(pattern, word):
        formatted_word = re.sub(pattern, "", word)
        return formatted_word
    return word


def create_vector_from_input(formatted_input_list):
    column_list = [" ".join(col.split("_")) for col in columns]
    vector = [0] * len(column_list)

    for i in range(len(column_list)):
        for keyword in column_list[i].split():
            if keyword in formatted_input_list:
                vector[i] = 1
                # print(i)
                break
    return vector


def sort_similarities(similarities):
    sorted_scores = sorted(similarities, key=lambda x: x[1], reverse=True)
    return sorted_scores


def find_diseases(text_input):
    disease_result = []
    formatted_list = remove_stop_words(text_input)
    print(formatted_list)
    vec2 = create_vector_from_input(formatted_list)
    if all(val == 0 for val in vec2):
        return None
    similarities = cosine_similarity(vec2)
    results = sort_similarities(similarities)
    for res in results:
        if res[1] > 0.1:
            disease_result.append(df.iloc[res[0]]["prognosis"])
    return list(disease_result)


def check_input_validity(text_input):
    regex = r"[a-zA-Z]+"
    return re.match(regex, text_input)


def fix_wrong_words(text):
    spell = SpellChecker()
    corrected_sentence = []
    for word in text.split():
        word = spell.correction(word)
        if word:
            corrected_sentence.append(word)

    new_fixed_text = " ".join(corrected_sentence)
    return new_fixed_text



def remove_special_characters_from_word(word):
    pattern = r"[^a-zA-Z]"
    words = re.split(pattern, word)
    return words



def clean_extra_words(sentence):
    result = []
    splitted_words = re.split(r"[,\s]+", sentence.lower())
    for word in splitted_words:
        if word not in stop_words:
            result.append(remove_numbers_specials(word))
    final_result = " ".join(result)
    return final_result


def find_diseases_detailed(text_input):
    diseases_list = []
    sentence = clean_extra_words(text_input)
    vec2 = generate_similarity_based_vector(sentence)
    if all(val == 0 for val in vec2):
        return None
    similarities = cosine_similarity_calc(vec2)
    sorted_similarities = sort_similarities(similarities)
    for res in sorted_similarities:
        if res[1] > 0.05:
            diseases_list.append(df.iloc[res[0]]["prognosis"])
    return diseases_list
