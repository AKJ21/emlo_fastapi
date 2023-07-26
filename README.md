# FASTAPI

Experiment requirements was to use a trained GPT and a ViT model and deploy inside a container with fastapi.  
Both the models api were called one by one and made to run on sample data 100 times. Response time was calculated at each run and final average time was calculated.

## GPT Lightning Model
- Model used was trained on Harry Potter datasets for 10 epochs. 
- Model is deployed on docker using fastapi.

To run this experiment on local or any cloud instance:

1. Get the gpt folder to your work environemnts.
2. Open terminal and build your docker image by running "`docker build --tag gpt .`"
3. Run the gpt image: "`docker run -it -p 8080:8080 gpt`"
4. Open < ip >:8080/docs in your browser to test the api.

If running locally, open "`localhost:8080/docs`"

## ViT (Vision Transformer) Model
- Model was trained on MNIST datasets for 10 epochs. 
- Model is deployed on docker using fastapi.

To run this experiment on local or any cloud instance:

1. Get the vit folder to your work environemnts.
2. Open terminal and build your docker image by running "`docker build --tag vit .`"
3. Run the vit image: "`docker run -it -p 8081:8081 vit`"
4. Open < ip >:8081/docs in your browser to test the api.

If running locally, open "`localhost:8081/docs`"

## Test results of this experiment
```
Average response time for GPT model:  1.1211067581176757 secs
Average response time for VIT model:  0.023972949981689452 secs
```

## Team Members:
- Aman Jaipuria
- Anurag Mittal