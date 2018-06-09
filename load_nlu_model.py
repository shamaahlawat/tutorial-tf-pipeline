from rasa_nlu.model import Metadata, Interpreter

def load_model():
	# where `model_directory points to the folder the model is persisted in`
	interpreter = Interpreter.load('models/current/nlu_model')
	print(interpreter.parse("I have just arrived in Berlin. Can you suggest any cool meetups I could attend?"))
	
if __name__ == '__main__':
	load_model()


