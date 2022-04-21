elif self.path.startswith("/gene?"):
name = self.path.split("?name=")[1]
# esto se podría hacer con la read_fasta function
gene_seq = open("./seq_dna/" + name + ".txt", "r").read()
gene_seq = gene_seq[gene_seq.find("\n") + 1:].replace("\n", "")
contents = Path('gene.html').read_text().format(name, gene_seq)