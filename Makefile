CONDA_ENV_NAME = genai-note-companion

# https://make.mad-scientist.net/deferred-simple-variable-expansion/
# https://www.chiark.greenend.org.uk/doc/make-doc/make.html/Using-Variables.html

activate:
	@ echo conda activate $(CONDA_ENV_NAME)

clean:
	conda remove -n $(CONDA_ENV_NAME) --all

setup:
	(conda env list --json | jq -r '.envs | map(select(contains("/envs/"))) | .[]' | xargs basename | grep -q $(CONDA_ENV_NAME) ) \
		|| conda create -y -n $(CONDA_ENV_NAME) python=3.13 pip

install: setup
	conda run -n $(CONDA_ENV_NAME) pip install -r requirements.txt

echo: OPENAI_API_KEY = $(shell ./bin/get-openai-api-key)
echo:
	echo $(OPENAI_API_SECRET_ID)
	echo $(OPEN_API_KEY)


openai-models: OPENAI_API_KEY = $(shell ./bin/get-openai-api-key)
openai-models: 
	# https://platform.openai.com/docs/api-reference/models/list
	curl https://api.openai.com/v1/models \
		-H "Authorization: Bearer $(OPENAI_API_KEY)" | jq 


serve: OPENAI_API_KEY = $(shell ./bin/get-openai-api-key)
serve:
	( sleep 2; open -a "Google Chrome" http://localhost:8501/) &
	@ OPENAI_API_KEY=$(OPENAI_API_KEY) conda run -n $(CONDA_ENV_NAME) streamlit run frontend.py --server.headless true

serve-hello:
	( sleep 2; open -a "Google Chrome" http://localhost:8501/) &
	@ conda run -n $(CONDA_ENV_NAME) streamlit hello

serve-hello-world:
	( sleep 2; open -a "Google Chrome" http://localhost:8501/) &
	@ conda run -n $(CONDA_ENV_NAME) streamlit run frontend-hello-world.py --server.headless true
	@ # conda run -n $(CONDA_ENV_NAME) streamlit hello
