../src/szeol/static/dist/*: dist/*.js
	@cp dist/* ../src/szeol/static/dist/
	@echo "=========="
	@echo "=  Done  ="
	@echo "=========="
	@echo "JS COMPILED" | osd_cat -p top -A center -s 2 -d 2

dist/*.js: src/*.js *.js
	@webpack
