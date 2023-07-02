import openai

openai.api_key = "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"

models = openai.Model.list()
# print(models)


def handle_input(user_input):
    copletion =openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages= [{"ROLE": "user", "content": user_input}]
    )
    return copletion

handle_input(input()).choices[0].message.content