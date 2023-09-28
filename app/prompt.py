import openai
from .config import settings

openai.api_key = settings.openai_api_key

# Summarize document 1
import openai

def summarize_docs1(doc1):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that summarizes text. Summarize the following text to be usable and understandable by a gpt model to create new text from"},
            {"role": "user", "content": doc1}
        ],
        temperature=0.6,
        max_tokens=6000
    )

    summary = response['choices'][0]['message']['content'].strip()
    # print(summary)
    return summary


# Summarize document 2
def summarize_docs2(doc2):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that summarizes text. Summarize the following text to be usable and understandable by a gpt model to create new text from"},
            {"role": "user", "content": doc2}
        ],
        temperature=0.6,
        max_tokens=6000
    )

    summary_2 = response['choices'][0]['message']['content'].strip()
    # print(summary_2)
    return summary_2


def merge_content(topic, content_1_str, content_2_str):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {"role": "system", "content": "You are a seasoned article merger, experienced in merging articles to create (very detailed) up-to-date readable article and where possible in tutorial style."},
            {"role": "user", "content": f"I would give you a topic and two different articles:\n\n{content_1_str}\n\nand\n\n{content_2_str}\n\nCombine these two articles to create a new article based on the topic:\n\n{topic}"}
        ],
        temperature=0.6,
        max_tokens=16000
    )


    response = response['choices'][0]['message']['content'].strip()


    splitted_strings: list[str] = response.split("\n")

    # remove empty strings
    sections = [value for value in splitted_strings if len(value) > 0]

    sections1 = [value for value in sections if value!="```"]

    return sections1