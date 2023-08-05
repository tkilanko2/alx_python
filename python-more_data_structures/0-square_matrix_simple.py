'''def square_matrix_simple(matrix=[]):
    new_matrix = [row[:] for row in matrix]
    for idx, row in enumerate(new_matrix):
        for idx2, col in enumerate(new_matrix):
            new_matrix[idx][idx2] = row[idx2] ** 2
    return new_matrix '''
    
def square_matrix_simple(matrix=[]):
    squared_matrix = []
    for row in matrix:
        squared_row = [num ** 2 for num in row]
        squared_matrix.append(squared_row)
    return squared_matrix


