import matplotlib.pyplot as plt
import numpy as np


# Подсчет количества нуклеотидов в каждой позиции
def nuc_pos_counts(seqs: list) -> dict:
	nucleotide_counts = {'A': [], 'T': [], 'G': [], 'C': []}
	alignment_length = len(seqs[0])

	for i in range(alignment_length):
		column = [seq[i] for seq in seqs]
		for nucleotide in nucleotide_counts:
			count = column.count(nucleotide)
			nucleotide_counts[nucleotide].append(count)
	return nucleotide_counts


# Отрисовка графика
def bar_plot(nucleotide_counts: dict):
	position = range(len(nucleotide_counts['A']))
	bottom = np.zeros(len(position))

	for nucleotide in ['A', 'T', 'G', 'C']:
		counts = nucleotide_counts[nucleotide]
		plt.bar(position, counts, label=nucleotide, alpha=0.8, bottom=bottom)
		bottom = [sum(x) for x in zip(bottom, counts)]
	plt.xlabel('Position')
	plt.ylabel('Frequency')
	plt.legend()
	plt.show()


# Вызов графика
def paint_plot(seq):
	nucleotide_count = nuc_pos_counts(seq)
	bar_plot(nucleotide_count)


if __name__ == '__main__':
	def alignment_file_reading(directory: str) -> list:
		alignment_file = directory
		seqs = []

		with open(alignment_file, 'r') as file:
			lines = file.readlines()
			for line in lines:
				seqs.append(line.strip())
			return seqs


	def paint_plot(seq):
		nucleotide_count = nuc_pos_counts(seq)
		bar_plot(nucleotide_count)


	sequences = alignment_file_reading('5.1_MSA.txt')
	paint_plot(sequences)
