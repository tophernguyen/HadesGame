import json
import pandas as pd

# Load the JSON data
with open('output.json') as f:
    data = json.load(f)

# Extract and transform data
runs = data['runs']
formatted_data = []

for run in runs:
    sub_traits = ", ".join([f"{trait['traitName']} (Level {trait['traitLevel']})" for trait in run['trait']])
    sub_heat = ", ".join([f"{h['darknessName']} (Level {h['darknessLevel']})" for h in run.get('darkness', [])])
    
    formatted_data.append({
        'index': run['index'],
        'result': run['result'],
        'time': run['time'],
        'clearMessage': run['clearMessage'],
        'weapon': run['weapon'],
        'aspect': run['aspect'],
        'keepsake': run['keepsake'],
        'companion': run['companion'],
        'trait (sub-traits)': sub_traits,
        'heatPoints': run['heatPoints'],
        'heat (sub-heat)': sub_heat
    })

# Create DataFrame
df = pd.DataFrame(formatted_data)

df.to_csv('output.csv', index = False)


