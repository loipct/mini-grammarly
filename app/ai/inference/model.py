import torch
import torch.nn as nn
import torch.optim as optim
from transformers import BertModel, BertTokenizer
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

import os
# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(script_dir)

# Define the BERT regression model
class BERTRegressionModel(nn.Module):
    def __init__(self, bert_model_name, num_numerical_features, num_binary_features):
        super(BERTRegressionModel, self).__init__()
        self.bert = BertModel.from_pretrained(bert_model_name)
        self.regression_head = nn.Sequential(
            nn.Linear(self.bert.config.hidden_size + num_numerical_features + num_binary_features, 128),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(64, 1)
        )

    def forward(self, input_ids, numerical_features, binary_features):
        bert_output = self.bert(input_ids=input_ids).last_hidden_state
        pooler_output = bert_output[:, 0, :]  # Pooler output
        concatenated_features = torch.cat([pooler_output, numerical_features, binary_features], dim=1)
        regression_output = self.regression_head(concatenated_features)
        return regression_output
    
    
# Load the saved model
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BERTRegressionModel( "bert-base-uncased", num_numerical_features=1, num_binary_features=2)  # Instantiate the model
model.load_state_dict(torch.load(os.path.join(parent_dir, 'models','bert_regression_model.pth'),map_location=device, weights_only=True))  # Load the state dictionary
model.to(device)  # Move the model to the device


# Standardize numerical features using the saved scaler
with open(os.path.join(parent_dir, 'models','scaler_config.pkl'), 'rb') as file:
    scaler = pickle.load(file)



