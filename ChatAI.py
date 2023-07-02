import openai

openai.api_key = "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"

models = openai.Model.list()
# print(models)


def handle_input(user_input):
    copletion =openai.ChatCompletion.create(
        model="gpt-3.5-turb", messages= [{"ROLE": "user", "content": user_input}]
    )
    return copletion