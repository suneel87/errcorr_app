import pickle, torch
from transformers import *

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

model = BertForMaskedLM.from_pretrained('bert-base-uncased').to(device)

with open(f'./model/tok.pickle', 'rb') as tok:
    tokenizer = pickle.load(tok)

model.load_state_dict(torch.load(f'./model/med_corr.pt', map_location=torch.device('cpu')))

def predict(sent):
    erroneous_sentence = sent
    tokenized_sentence = tokenizer.encode_plus(erroneous_sentence, add_special_tokens=True, return_tensors="pt")

    model.eval()
    with torch.no_grad():
        outputs = model(input_ids=tokenized_sentence['input_ids'].to(device), 
                        attention_mask=tokenized_sentence['attention_mask'].to(device))
        
    predicted_tokens = torch.argmax(outputs.logits, dim=-1)
    predicted_tokens = predicted_tokens.squeeze()

    predicted_sentence = tokenizer.decode(predicted_tokens.tolist(), skip_special_tokens=True)

    return predicted_sentence