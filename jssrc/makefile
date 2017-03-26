../src/szeol/static/dist/*: dist/*.js
	@cp dist/* ../src/szeol/static/dist/
	@echo "=========="
	@echo "=  Done  ="
	@echo "=========="

dist/*.js: src/*.js src/*.vue
	@webpack
