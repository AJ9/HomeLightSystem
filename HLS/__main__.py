import sys
import core
import sched, time

from lib import Project

def do_something(sc): 
    print project.date()
    s.enter(1, 1, do_something, (sc,))

if __name__ == '__main__':
    project = Project()
    s = sched.scheduler(time.time, time.sleep)
    s.enter(1, 1, do_something, (s,))
    s.run()