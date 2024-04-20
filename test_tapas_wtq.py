import numpy as np
import pandas as pd
import torch
from transformers import pipeline, AutoTokenizer, AutoModelForTableQuestionAnswering
from datetime import datetime

def load_tapas_model():
  model_tapas = "google/tapas-large-finetuned-wtq"
  tokenizer_tapas = AutoTokenizer.from_pretrained("google/tapas-large-finetuned-wtq")
  model = AutoModelForTableQuestionAnswering.from_pretrained("google/tapas-large-finetuned-wtq")
  pipe_taps = pipeline("table-question-answering", model=model_tapas, tokenizer=tokenizer_tapas)
  return pipe_taps

pipe = load_tapas_model()

# def dataframe_to_string(table):
#     # Convert DataFrame to a list of dictionaries
#     table_data = table.to_dict(orient='records')
#     # Convert list of dictionaries to a string format
#     table_str = ""
#     for row in table_data:
#         row_str = "\t".join(str(value) for value in row.values())
#         table_str += row_str + "\n"
#     return table_str
dataset = pd.read_csv('/Users/vimalvatsa/Downloads/heart.csv')
dataset_dict = dataset.to_dict(orient='records')
# Debugging: Print the type of each value in the first row of dataset_dict
if dataset_dict:  # Ensure dataset_dict is not empty
    print({key: type(value) for key, value in dataset_dict[0].items()})

# Convert integers to strings in dataset_dict, if necessary
for row in dataset_dict:
    for key, value in row.items():
        # Check for numeric types (int, float)
        if isinstance(value, (int, float)):
            row[key] = str(value)

# Now, you can pass dataset_dict to your get_answer function correctly
# Ensure get_answer is designed to handle dataset_dict appropriately
input_str = str('Calculate the average age from the dataset.')
print("Enter the question")
question = str(input())
# Before calling pipe in get_answer, ensure all data is in a correct format
def get_answer(dataset_dict, input_str):
    # Ensure input_str is indeed a string
    query_str = str(input_str)
    # Format the input correctly for the TAPAS model
    results = pipe({"table": dataset_dict, "query": query_str})
    return results




dataset_str = dataset


ans = get_answer(dataset_dict, input_str)

print(ans)


def convert_answer(answer):
    if answer['aggregator'] == 'SUM':
      cells = answer['cells']
      converted = sum(float(value.replace(',', '')) for value in cells)
      return converted

    if answer['aggregator'] == 'AVERAGE':
      cells = answer['cells']
      values = [float(value.replace(',', '')) for value in cells]
      converted = sum(values) / len(values)
      return converted

    if answer['aggregator'] == 'COUNT':
      cells = answer['cells']
      converted = sum(int(value.replace(',', '')) for value in cells)
      return converted

    else:

      return answer['answer']
new_ans = convert_answer(ans)

def get_converted_answer(table, query):
    converted_answer = convert_answer(get_answer(table, query))
    return converted_answer

new = get_converted_answer(dataset_dict, input_str)
print(new)

# def google_tapas_wtq_llm_mode(data, query):
#     """
#     Implement Google TAPAS WTQ (WikiTable Questions) LLM mode.
#     This function takes a dataset and a query from the user, processes it accordingly, and returns the output.
#     """
#     # Initialize TapasUse instance
#     tapas_instance = TapasUse()
    
#     # Prepare inputs using the provided data and query
#     table, inputs = tapas_instance.prepare_inputs(data, query)
    
#     # Generate predictions based on the prepared inputs
#     predicted_table_cell_coords, predicted_aggregation_operators = tapas_instance.generate_predictions(inputs)
    
#     # Postprocess the predictions to get human-readable answers
#     aggregation_predictions_string, answers = tapas_instance.postprocess_predictions(
#         predicted_aggregation_operators, predicted_table_cell_coords, table
#     )
    
#     # Return the processed answers and aggregation predictions
#     return answers, aggregation_predictions_string
