PROTOC = protoc --mypy_out=../tmp-mypy/

clone:
	git clone --depth 1 https://github.com/google/or-tools.git -b stable

pull:
	cd or-tools; git pull

mypy:
	rm -rf tmp-mypy
	rm -rf ortools-stubs
	mkdir tmp-mypy
	pip3 install mypy-protobuf

	cd or-tools; \
	$(PROTOC) ortools/constraint_solver/assignment.proto; \
	$(PROTOC) ortools/constraint_solver/routing_enums.proto; \
	$(PROTOC) ortools/constraint_solver/routing_parameters.proto; \
	$(PROTOC) ortools/constraint_solver/search_limit.proto; \
	$(PROTOC) ortools/constraint_solver/solver_parameters.proto; \
	$(PROTOC) ortools/data/rcpsp.proto; \
	$(PROTOC) ortools/linear_solver/linear_solver.proto; \
	$(PROTOC) ortools/sat/cp_model.proto; \
	$(PROTOC) ortools/sat/sat_parameters.proto; \
	$(PROTOC) ortools/util/optional_boolean.proto

	mv ./tmp-mypy/ortools ./ortools-stubs
	rm -r ./tmp-mypy
	python3 run.py
