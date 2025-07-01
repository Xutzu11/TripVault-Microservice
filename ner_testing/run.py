from calculate_accuracy import process_combined, process_individual
from plot_accuracy import plot_acc
from extract_results import write_extraction_results

write_extraction_results()
process_combined()
process_individual()
plot_acc()