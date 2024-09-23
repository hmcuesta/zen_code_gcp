LOAD DATA INTO modified-return-436315-b9.ChallengeZen.creditcard_transactions
FROM FILES (
    format = 'CSV',
    uris = ['gs://zen_data/zFraud_historico.csv']
);

CREATE OR REPLACE MODEL `modified-return-436315-b9.ChallengeZen.fraud_detection_model`
OPTIONS(model_type='logistic_reg', input_label_cols=['class']) AS
SELECT 
    v1,v2,v3,v4,class
FROM 
    `modified-return-436315-b9.ChallengeZen.creditcard_transactions`
WHERE
    Class IS NOT NULL;