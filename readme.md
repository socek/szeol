# 1. About Szeol

Szeol is a simple CRM for wine store.

# 2. Dependencies

1. python 3
2. virtualenv
3. docker 1.13.1
4. GNU make 4.2.1

# 3. Start developing

First you need to create virtualenv. We use makefile for this.

```bash
make
```

After that you can use local commands to start the server.

```bash
. ./venv_szeol/bin/activate
serv
```

# 4. List of commands to use

1. serv - start development server
2. shell - start development shell
3. manage - django manage script
4. tests - run all tests suite
5. testscov - run all tests suite with coverage report
