all: psqldb redisdb rabbitdb
	docker-compose up -d postgres redis rabbit maildump
psqldb:
	docker volume create --name=psqldb
redisdb:
	docker volume create --name=redisdb
rabbitdb:
	docker volume create --name=rabbitdb
sentrydb:
	docker volume create --name=sentrydb

clean:
	@echo "================================================================================================"
	@echo "This may fail, because postgresql and redis have changed ownership rights. Use su/sudo for this."
	@echo "================================================================================================"
	docker-compose down
	rm -rf psqldb redisdb rabbitdb
	rm -rf flags/*

install: all
	@echo "Waiting for postgresql to be fully operational..."
	# if you know better sollution, please fix this
	sleep 5
	./scripts/init


sentry: all sentrydb flags/init_sentry
	docker-compose run -d sentry sentry run cron
	docker-compose run -d sentry sentry run worker
	docker-compose up -d sentry

flags/init_sentry:
	./scripts/init_sentry
