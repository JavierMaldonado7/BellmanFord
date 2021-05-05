#CIIC4025-066

#Javier Maldonado Rivera

#Assignment #4 Bellman Ford

#tester variable

graph = {
    's' : {'t':6, 'y':7},
    't' : {'x':5, 'z':-4, 'y':8 },
    'y' : {'z':9, 'x':-3},
    'z' : {'x':7, 's': 2},
    'x' : {'t':-2}
}

def get_distances(graph, source):
    result = dict()

    for node in graph:
        result[node]= float('inf')

    result[source] = 0

    for mod in range(len(graph) - 1):

        for node in graph:

            for edge in graph[node]:

                if (  result[node] + graph[node][edge] < result[edge]):

                    result[edge]= result[node] + graph[node][edge]

    return result

print(get_distances(graph,'s'))