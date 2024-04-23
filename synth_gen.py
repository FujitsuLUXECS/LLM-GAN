import synthcity
from synthcity.utils.serialization import load_from_file

# Load model from file
path_to_model = "./model.pkl"
model = load_from_file(path_to_model)

# Get the name of the model
model_name = model.name()
print(model_name)

# Generate a synthetic dataset of size 500
synth_size = 500
synth_data = model.generate(count=synth_size).dataframe()
print(synth_data.head(10))

# Get the list of columns of the generated dataset
columns = list(synth_data.columns)
print(f"\n{columns}\n")

# Drop some columns of the generated dataset
cols_to_drop = ["age", "race", "sex", "native-country"]
synth_data_drop = synth_data.drop(columns=cols_to_drop)
print(synth_data_drop.head(10))

# Keep only some columns of the generated dataset
cols_to_keep = ["age", "race", "sex", "native-country"]
synth_data_keep = synth_data[cols_to_keep]
print(synth_data_keep.head(10))