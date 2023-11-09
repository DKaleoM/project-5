# Makefile for the simple page server.
#

# Nothing to install for this project.
install:
	@(echo 'nothing to install')

restart:
	@(make clean; make install; make start)

start:
	@(docker compose up -d --build)

stop:
	@(docker compose down)

terminal:
	@(docker exec -it "project-5-brevets-1" /bin/bash)

test:
	@(docker exec -it "project-5-brevets-1" ./run_tests.sh)

run:
	@(make restart)

logs:
	@(docker logs "project-5-brevets-1")

clean:
	@(docker stop $$(docker ps -a -q); docker rm $$(docker ps -a -q))


