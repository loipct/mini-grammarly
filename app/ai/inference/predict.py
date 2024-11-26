
import sys
import os
import torch

# Add the current directory (where model.py is) to the sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

# Importing directly from the same directory
from model import model, tokenizer, scaler


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
def predict_essay_score(essay_text, task_type :int ):
    """Predicts the score of an essay.

    Args:
        essay_text: The text of the essay.
        numerical_features: A list or array of numerical features (e.g., essay length).
        binary_features: A list or array of binary features (e.g., task type).

    Returns:
        The predicted score of the essay.
    """
    
    essay_length = len(essay_text.split(" "))
    numerical_features = scaler.transform([[essay_length]])[0]
    if task_type == 1:
        binary_type = [1,0]
    else:
        binary_type = [0,1]
    # Tokenize the essay text
    input_ids = tokenizer(essay_text, padding=True, truncation=True, return_tensors='pt', max_length=512)['input_ids'].to(device)

    # Convert numerical and binary features to tensors and move to device
    numerical_features = torch.tensor(numerical_features, dtype=torch.float32).unsqueeze(0).to(device)  # Add batch dimension
    binary_features = torch.tensor(binary_type, dtype=torch.float32).unsqueeze(0).to(device)  # Add batch dimension

    # Make prediction
    model.eval()
    with torch.no_grad():
        output = model(input_ids, numerical_features, binary_features)
        predicted_score = output.item()

    return round(float(predicted_score),2)


if __name__ == "__main__":
    essay_text = """Information about the thousands of visits from overseas to three different European natural places during 1987 and 2007 is provided in the given line chart.
    Overall, it can be seen that the number of visitors increased significantly in the three places compared to the initial year. Although, visits to Europeans lakes demostrated more changes over the 20 years than its counterparts.
    In more detail, the most steady growth was experienced by the visits to Europeans mountains. For example, from 1987 the number of visitors grew from 20,000 to almost the double 20 years later. Similarly, visits to the coast also rose after a slight fall in 1992, reaching almost twice as much since 1987, with 75,000.
    Those visiting Europeans lakes subtantially increased over the years from 10 thousand to a peak of 75 thousand in 2002. Despite falling for about 25 thousand in 2007, the visitis to this place remained higher compared to 1987, with 50,000 at the end of the period."""  # Replace with your essay text
    task_type = [1, 0]  # Example: [Task_Type_0, Task_Type_1], adjust based on your encoding
    print(predict_essay_score(essay_text, task_type))