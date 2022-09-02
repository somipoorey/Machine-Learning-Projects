docker run -p 8500:8500 -p 8501:8501 --name="Gender_Detection" --mount type=bind,source=/c/Users/anura/Desktop/model/saved_model,target=/models/gender_model --mount type=bind,source=/c/Users/anura/Desktop/model/models_config,target=/models/ -t tensorflow/serving --model_config_file=/models/models_config.c --allow_version_labels_for_unavailable_models=true --model_config_file_poll_wait_seconds=120

rest url : 
http://127.0.0.1:8501/v1/models/gender_model

http://127.0.0.1:8501/v1/models/gender_model/versions/1

http://127.0.0.1:8501/v1/models/gender_model/labels/production


curl http://127.0.0.1:8501/v1/models/gender_model



# Use https://jsonformatter.org/json-parser

curl -f @parsedinstance.txt -X POST http://127.0.0.1:8501/v1/models/gender_model:predict

curl -d @raw.txt -X POST http://127.0.0.1:8501/v1/models/gender_model:predict
