VENV = .venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip3
STREAMLIT= $(VENV)/bin/streamlit


# Need to use python 3.9 for aws lambda
$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt

init: $(VENV)/bin/activate

app: $(VENV)/bin/activate
	$(STREAMLIT) run app.py --server.port 1808 


clean:
	rm -rf __pycache__
	rm -rf $(VENV)
