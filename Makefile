start: ## start all services
	uvicorn api.main:app

dev: ## start the app in dev mode (auto reload)
	uvicorn api.main:app --reload

help: ## Display this help section
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z0-9_-]+:.*?## / {printf "\033[36m%-38s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST) | sort
