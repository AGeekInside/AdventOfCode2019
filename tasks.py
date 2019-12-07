from invoke import task

@task
def run(c, day):
    """Runs the specified day program."""

    c.run(f"python {day}/program.py")