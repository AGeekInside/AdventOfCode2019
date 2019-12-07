from invoke import task

@task
def run(c, day):
    """Runs the specified day program."""

    c.run(f"python {day}/program.py")

@task
def add(c, day):

    c.run(f"mkdir {day} ; touch {day}/program.py ; touch {day}/input.txt")
    c.run(f"git add {day} ; git commit -m 'Adding {day}' ; git push")