from modules import *


DATA_PATH = os.path.join('Feature_Extraction') 

actions = np.array(['hello', 'thanks', 'iloveyou','please','house'])

number_sequences = 50
sequence_length = 30

for action in actions: 
    for sequence in range(number_sequences):
        try: 
            os.makedirs(os.path.join(DATA_PATH, action, str(sequence)))
        except:
            pass