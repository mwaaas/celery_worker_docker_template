from python:3.5-onbuild

ENV  C_FORCE_ROOT=1

CMD celery -A tasks worker --loglevel=info