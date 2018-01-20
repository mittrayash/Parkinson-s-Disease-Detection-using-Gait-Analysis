# Parkinson-s-Disease-Detection-using-Gait-Analysis

A research project that aims to detect Parkinson's disease in patients using Gait Analysis data. Subsequently, the project may make use of Gait Data Analysis to make powerful inferences which would help in genralizing the most common groups affected by this disease.
  
Gait Analysis of Parkinson’s Disease (PD) Patients and Control Objects has been analysed to show differences in PD Patients and Control Objects. Using data provided by Phisonet’s Gaitpdb database (in which 8 sensors have been applied to each foot of the subjects to calculate the Vertical Ground Reaction Forces (VGRF)), **data compression has been performed using 7 statistical functions to get a representative image of the data**. The statistical functions namely Minimum, Maximum, Mean, Median, Standard Deviation, Skewness, and Kurtosis have been used **to compress over 3 million tuples into 310 tuples**. Finally, various Machine Learning techniques have been applied to the transformed dataset to perform detection of Parkinson’s Disease.  

Classification has been performed using Logistic Regression, Decision Trees, Random Forest, SVM (Linear Kernel), SVM (RBF Kernel), SVM (Sigmoid Kernel), SVM (Poly Kernel) and k-Nearest Neighbours. The accuracies achieved are 94.81%, 97.40%, 97.40%, 94.81%, 97.40%, 93.51%, 96.10%, 97.40%.
Experiments with Principal Component Analysis for data compression have also been performed and their incompetence (with reasons) has been stated. 

