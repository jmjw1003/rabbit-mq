# Work queues
Quick tutorial to demonstrate distributing (simulated using " . " ) time-consuming tasks among multiple workers.

## Instructions
Open 3 (or more) split terminals

In all but one terminal, run the worker scripts:

`$ python3 worker.py`.

They will await incoming tasks from Rabbit MQ.

Run multiple new tasks in the remaining terminal: </br>
```
python3 new_task.py First message....
python3 new_task.py Second message..
python3 new_task.py Third message.
python3 new_task.py Fourth message....
python3 new_task.py Fifth message......
python3 new_task.py Sixth message...
```

Note that if you kill any worker terminals that any unfinished tasks will be re-routed to running workers.
