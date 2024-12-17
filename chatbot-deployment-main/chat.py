import random
import json
import torch
import traceback
from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

try:
    with open('intents.json', 'r', encoding='utf-8') as json_data:
        intents = json.load(json_data)
except Exception as e:
    print(f"Error loading intents.json: {str(e)}")
    print(traceback.format_exc())
    raise

try:
    FILE = "data.pth"
    data = torch.load(FILE)

    input_size = data["input_size"]
    hidden_size = data["hidden_size"]
    output_size = data["output_size"]
    all_words = data['all_words']
    tags = data['tags']
    model_state = data["model_state"]

    model = NeuralNet(input_size, hidden_size, output_size).to(device)
    model.load_state_dict(model_state)
    model.eval()
except Exception as e:
    print(f"Error loading model: {str(e)}")
    print(traceback.format_exc())
    raise

bot_name = "Sam"

def get_response(msg):
    try:
        sentence = tokenize(msg)
        X = bag_of_words(sentence, all_words)
        X = X.reshape(1, X.shape[0])
        X = torch.from_numpy(X).to(device)

        output = model(X)
        _, predicted = torch.max(output, dim=1)

        tag = tags[predicted.item()]

        probs = torch.softmax(output, dim=1)
        prob = probs[0][predicted.item()]
        
        if prob.item() > 0.5:
            for intent in intents['intents']:
                if tag == intent["tag"]:
                    return random.choice(intent['responses'])
        
        return "I'm not sure I understand. Could you please rephrase that?"
    except Exception as e:
        print(f"Error in get_response: {str(e)}")
        print(f"Message was: {msg}")
        print(traceback.format_exc())
        raise

if __name__ == "__main__":
    print("Let's chat! (type 'quit' to exit)")
    while True:
        # sentence = "do you use credit cards?"
        sentence = input("You: ")
        if sentence == "quit":
            break

        resp = get_response(sentence)
        print(resp)
