import matplotlib.pyplot as plt

degenerate_dict = {
		('C', 'T'): 'Y',
		('A', 'G'): 'R',
		('A', 'T'): 'W',
		('G', 'C'): 'S',
		('G', 'T'): 'K',
		('C', 'A'): 'M',
		('A', 'G', 'T'): 'D',
		('A', 'C', 'G'): 'V',
		('A', 'C', 'T'): 'H',
		('C', 'T', 'G'): 'B',
		('A', 'C', 'T', 'G'): 'X'
	}


# Консенсус
def consensus_with_degenerate_alphabet(seq_list: list) -> list:
	seq_length = len(seq_list[0])
	nucl_freq = [{nucl: 0 for nucl in 'ATGC'} for _ in range(seq_length)]

	for seq in seq_list:
		for pos, base in enumerate(seq):
			nucl_freq[pos][base] += 1

	cons = []
	for pos in nucl_freq:
		max_base = [key for key, value in pos.items() if value == max(pos.values())]
		for key_tuple, degenerate_symbol in degenerate_dict.items():
			if set(max_base) == set(key_tuple):
				cons.append(degenerate_symbol)
				break
		else:
			cons.append(max_base[0])
	return cons


# Отрисовка графика
def pie_plot(bases_count: dict, consensus: list):
	labels = list(bases_count.keys())
	sizes = list(bases_count.values())
	plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
	plt.axis('equal')
	plt.title('Процентное соотношение нуклеотидов')

	for i, label in enumerate(labels):
		percentage = sizes[i]
		annotation = f'{label}: {percentage}%'
		x = sizes[i] / 2
		y = sizes[i] / 2
		plt.annotate(annotation, (x, y), fontsize=12, ha='center', va='center')

	cons = ''.join(consensus)
	plt.text(-1.5, -1.1, 'Консенсус:', fontsize=10)
	plt.text(-1.5, -1.2, cons, fontsize=10)

	plt.show()


# Сумма букав для вывода на график
def nucleotide_sum_for_plot(sequences_list):
	nucleotide_frequencies = {'A': 0, 'T': 0, 'G': 0, 'C': 0}

	for sequence in sequences_list:
		for nucleotide in sequence:
			if nucleotide in nucleotide_frequencies:
				nucleotide_frequencies[nucleotide] += 1
	return nucleotide_frequencies


# Вызов отрисовки графика
def paint_plot(seq: list):
	base_count = consensus_with_degenerate_alphabet(seq)
	sum_of_bases = nucleotide_sum_for_plot(seq)
	pie_plot(sum_of_bases, base_count)


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
		base_count = consensus_with_degenerate_alphabet(seq)
		pie_plot(nucleotide_sum_for_plot(seq), base_count)


	sequences = alignment_file_reading('5.1_MSA.txt')
	paint_plot(sequences)
