import matplotlib.pyplot as plt
from data.combined.accuracy import combined_acc
from data.individual.accuracy import individual_acc


def plot_acc():
    labels = ['LOCATION', 'ADDRESS', 'ATTRACTIONS_COUNT', 'TRANSPORT', 'MAX_DISTANCE', 'MAX_PRICE', 'MIN_RATING']

    x = range(len(labels))
    width = 0.35

    plt.figure(figsize=(10, 6))
    plt.bar([i - width/2 for i in x], combined_acc, width=width, label='Combined Prompts')
    plt.bar([i + width/2 for i in x], individual_acc, width=width, label='Individual Prompts')

    plt.xticks(x, labels, rotation=45)
    plt.ylabel("Accuracy")
    plt.ylim(0, 1.1)
    plt.title("NER Trait Accuracy Comparison")
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.savefig("data/ner_accuracy_comparison.png")
    plt.show()
