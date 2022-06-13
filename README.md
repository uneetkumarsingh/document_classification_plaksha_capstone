# document_classification_plaksha_capstone
API
Update script.py
11 minutes ago
Attachments
pushing to git
5 days ago
Data
pushing to git
5 days ago
Notebooks
pushing to git
5 days ago
models
pushing to git
5 days ago
streamlit_app
Update README.md
1 minute ago
Cactus_Capstone_Report.pdf

DOCUMENT CLASSIFICATION APPLICATION 

Below is the explaination for how files are organised:
1. API: This repo includes code and models for functional API's. These API's can be integrated into any downstream applications. Detailed instructions are inside the API repo. 
2. Attachements: This has files/documents/appendix data that has been referenced in the Capstone report
3. Data: This includes processed data in the form of csv files. This data was used for training and testing puposes. 
4. Notebooks: This includes notebooks for Preprocessing, EDA, Training and Benchmarking of Models. 
5. models: This has two pairs of models that we found performed best:
   5.1.1 estimator_v6_rfc_bucket.sav: Model/estimator that was trained on multilabel targets. 
   5.1.2 tfidf_v6_bucket.sav : Vectoriser to be used with the above model. 

   5.2.1 estimator_v3_c_pruned.sav : This is pickle file of Pruned RandomForest Trained on MultiClass-SingleLabel target feature. 
   5.2.2 tfidf_v3_c_min_max_df.sav : This Tfidf vectoriser is to be used with above model. 

6. streamlit_app: This includes files for streamlit app. Models 5.1.1 and 5.1.2 have been used for this application. This app is deployed at 
7. Cactus_Capstone_Report.pdf : This is a complete report of the hypothesis, exploration, experiments, results and learnings while doing the project. 
