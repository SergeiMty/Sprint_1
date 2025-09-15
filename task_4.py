new_tasks = ['task_001', 'task_011', 'task_007', 'task_015', 'task_005']
completed_tasks = ['task_002', 'task_012', 'task_006']

#убираем таску 'task_005' из списка 'new_tasks' и добавляем в 'completed_tasks'
completed_tasks.append(new_tasks.pop())

#убираем таску 'task_007' из списка 'new_tasks'
new_tasks.remove('task_007')

print(new_tasks[-1])
