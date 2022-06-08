File Details:
1. script.py : script to take a docx path and predict class, probability, inference time, vectorisation time
	1.1 It has four methods:
		1.1.1 clean_text: it takes a string and returns cleaned text.
		1.1.2 load_text: load text from a docx file path
		1.1.3 load_models: loads models from the hardcoded model and vectorizer path in the code
		1.1.4 predict: It takes model, vectoriser and file_path and returns class, probability, inference time, vectorisation time
2. estimator_v4_c_pruned.sav: pickle file of model
3. tfidf_v4_c_min_max_df.sav pickle file of vectorizer

To get prediction, 

STEP1: load models using load_model method by passing model_path and vectorizer path

STEP2: Then pass model, vectoriser and file path in predict method	
