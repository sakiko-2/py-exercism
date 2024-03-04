PROTEINS = {"Methionine": ("AUG",), "Phenylalanine": ('UUU', "UUC"), "Leucine": ("UUA", "UUG"), "Serine": ("UCU", "UCC", "UCA", "UCG"), "Tyrosine": ("UAU", "UAC"), "Cysteine": ("UGU", "UGC"), "Tryptophan": ("UGG",), "STOP": ("UAA", "UAG", "UGA")}

def proteins(strand):
    codons = []
    [codons.append(strand[idx:idx+3]) for idx, _ in enumerate(strand) if idx % 3 == 0]

    result = []
    for codon in codons:
        for prt, c in PROTEINS.items():
            if codon in c:
                if prt == "STOP":
                    break
                result.append(prt)
        else:
            continue
        break

    return result
