#################### PACKAGE ACTIONS ###################
install_requirements:
	@pip install -r requirements.txt

run_api:
	uvicorn skin_detection.api.api:app --reload
