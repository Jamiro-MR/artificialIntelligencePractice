import openai
import config
openai.api_key = config.api_key

context = [{"role":"system","content": "You are a programming assistant of python language"}]
while True:
	prompt = input("Write something: ")
	if prompt == "exit":
		break
	context.append({"role":"user","content":prompt})
	response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=context)
	response_content = response.choices[0].message.content
	context.append({"role":"assistant","content":response_content})
	print(response_content)