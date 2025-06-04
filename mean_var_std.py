import numpy as np

def calculate(input_array):
    try:
        if len(input_array) != 9:
            raise ValueError("List must contain nine numbers.")
        
        data = np.array(input_array).reshape(3,3)

        calculations = {
            'mean': [data.mean(axis=0).tolist(),data.mean(axis=1).tolist(),data.mean().tolist()],
            'variance': [data.var(axis=0).tolist(),data.var(axis=1).tolist(),data.var().tolist()],
            'standard deviation': [data.std(axis=0).tolist(),data.std(axis=1).tolist(),data.std().tolist()],
            'max': [data.max(axis=0).tolist(),data.max(axis=1).tolist(),data.max().tolist()],
            'min': [data.min(axis=0).tolist(),data.min(axis=1).tolist(),data.min().tolist()],
            'sum': [data.sum(axis=0).tolist(),data.sum(axis=1).tolist(),data.sum().tolist()]
        }
        return calculations
    except Exception as e:
        return str(e)
    
input_array = [0,1,2,3,4,5,6,7,8]

result = calculate(input_array)
for key, value in result.items():
    print(f"{key}:{value}")