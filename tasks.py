from invoke import task
import src.database as db

@task
def start(ctx):
    ctx.run("python3 src/index.py")

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest")

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html")

@task
def build():
    db.start()
