LOAD DATA INTO modified-return-436315-b9.ChallengeZen.test_creditcard_transactions
FROM FILES (
    format = 'CSV',
    uris = ['gs://zen_data/batchtestzen.csv']
);

SELECT
    v1,v2,v3,v4, 
    predicted_Class,  -- Predicción realizada por el modelo
    predicted_Class_probs[OFFSET(1)] AS fraud_probability  -- Probabilidad de que sea fraude
FROM
  ML.PREDICT(MODEL `modified-return-436315-b9.ChallengeZen.fraud_detection_model`,
             (SELECT 
                v1,v2,v3,v4
              FROM 
                `modified-return-436315-b9.ChallengeZen.test_creditcard_transactions`));