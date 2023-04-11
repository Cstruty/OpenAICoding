import openai
OPENAI_API_KEY = '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'
import json
#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
#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
GPT_MODEL_VERSION = 'gpt-3.5-turbo'

openai.api_key = OPENAI_API_KEY

def send_openai_message(message_text: str) -> openai.openai_object.OpenAIObject:

	resp = openai.ChatCompletion.create(    

		model=GPT_MODEL_VERSION,

		messages=[

				{ "role": "user", "content": message_text } 

			]

	)

	return resp


def read_chatgpt_message(message: openai.openai_object.OpenAIObject) -> str:
	choices = message.get('choices')
	content = choices[0].get('message', {}).get('content', '')
	return content

def get_marketing_email_draft(topic: str ,companyname: str, name:str) -> str:
	message_text = f"""
	Draft a marketing email to drive interest in new customers about the following topic: {topic} sign it with the company name {companyname} and my name {name}
	"""
	response = send_openai_message(message_text = message_text)
	message_response = read_chatgpt_message(response)
	return message_response
def gen_z_and_shorten(message: str) -> str:
	message_text = f"""
	shorten this email to 40 words and make it more appealing to the Gen Z audience {message}
	"""
	response = send_openai_message(message_text = message_text)
	message_response = read_chatgpt_message(response)
	return message_response
def remove_non_ascii(message: str) -> str:
    message_text = f"""
    remove all non-ascii characters from this message {message}
    """
    response = send_openai_message(message_text = message_text)
    message_response = read_chatgpt_message(response)
    return message_response
def translate(message: str) -> str:
	message_text = f"""
	translate this message into french {message}
	"""
	response = send_openai_message(message_text = message_text)
	message_response = read_chatgpt_message(response)
	return message_response
