import numpy as np
from sagittal_brain import run_averages

def test_run_averages():
    # Create a sample input CSV file
    input_data = np.array([[1, 2, 3],
                           [4, 5, 6],
                           [7, 8, 9]])
    np.savetxt('test.csv', input_data, fmt='%d', delimiter=',')

    # Run the function to calculate averages
    run_averages(file_input='test.csv', file_output='test_row_average.csv')

    # Load the output CSV file and check the result
    output_data = np.loadtxt('test_row_average.csv', delimiter=',')
    expected_output = np.array([[2.0, 5.0, 8.0]])  
    # Expected average for each column

    assert np.allclose(output_data, expected_output), "The calculated averages are incorrect."