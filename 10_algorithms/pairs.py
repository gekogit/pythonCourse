obj_list = ['dom', 'szkoła', 'kosciol', 'bar', 'szpital', 'kino', 'teatr']

graph = [
    [0, 1, 1, 1, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 1, 0, 1, 1],
    [0, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 1, 0]
]

for row in range(0, len(obj_list)):
    for col in range(0, len(obj_list)):
        if graph[row][col] == 1:
            print(obj_list[row], '---', obj_list[col])
