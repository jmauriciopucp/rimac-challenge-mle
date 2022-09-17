# rimac-challenge-mle

## An API to predict heart disease with LGBM and MLOPS with Vertex AI

### API
    
To build the API, launch the next command:

```sh
uvicorn app:app --reload
```

Then, you go to the next URL, with the documented API's endpoint: 
http://127.0.0.1:8000/docs

Select 'Try Out' in the /classifier Enpoint and execute the example request. Your output will be the probability to dead by a heart disease.

For example:

##### Input:
```json
{
  "age": 41,
  "sex": "M",
  "chessPainType": "ATA",
  "restingBP": 140,
  "cholesterol": 289,
  "fastingBS": "0",
  "restingECG": "Normal",
  "maxHR": "123",
  "exerciseAngina": "N",
  "oldpeak": "1.5",
  "sTSlope": "Flat"
}
```

##### Output:
```json
{
  "prob": 0.899603
}

```



### Dockerize

For Dockerize the API, use the follow command:

```sh
docker build -t predict-app:v1 .
```
your output will be a Dockerize file with the rules to build the API Docker image.

### Vertex AI Pipelines

You need some steps to deply this note book to Workbench service of Vertex AI:

1. Auth to GCP Console.
2. Create your Proyect and save your PROJECT_ID.
3. Create a Bucket and upload your dataset. In the example 'data.csv' CSV dataset.
4. Create a Notebook with the Tensorflow Enterprise 2.3 Environment(4 vCPUs, 15GB RAM)
5. Upload your notebook tf-chll-mle-hearts in folder 'vertexai_pipelines'.
6. Select Run and Run all cells.
7. In the last cell, in the output you'll see the link to the Pipeline dashboard.

Note: It's probably to get an error in the deploy pipe, because we don't active the billing of project. 

![alt text](http://url/to/img.png)
