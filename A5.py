import numpy as np

def page_rank(graph, damping_factor=0.85, max_iterations=100, tol=1e-6):
    # Number of pages
    num_pages = len(graph)

    # Initialize the PageRank values
    pagerank = np.ones(num_pages) / num_pages

    for _ in range(max_iterations):
        new_pagerank = np.zeros(num_pages)
        for i in range(num_pages):
            for j in range(num_pages):
                if graph[j][i]:
                    new_pagerank[i] += pagerank[j] / sum(graph[j])

        # Apply damping factor and update PageRank
        new_pagerank = (1 - damping_factor) / num_pages + damping_factor * new_pagerank

        # Check for convergence
        if np.linalg.norm(new_pagerank - pagerank) < tol:
            return new_pagerank

        pagerank = new_pagerank

    return pagerank

# Example graph representing web page connections
# Replace this with your own graph
web_graph = [
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 1],
    [0, 0, 1, 0]
]

pagerank_values = page_rank(web_graph)
print("PageRank values:", pagerank_values)
