import openai


def make_question(question):
    print(f'Question: {question}')

    openai.api_key = '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'

    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',  # gpt-4-0314
        messages=[
            {
                'role': 'user',
                'content': f'{question}'
            }
        ]
    )

    print(f' Answer: {response.choices[0].message.content}')


if __name__ == '__main__':
    make_question('Es bueno aprender Python? xd')
