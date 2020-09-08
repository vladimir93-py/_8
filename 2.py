class NeDelIteNaNull:
    def __init__(self, nif_nif, naf_naf):
        self.nif_nif = nif_nif
        self.naf_naf = naf_naf

    @staticmethod
    def ne_delite_na_null(nif_nif, naf_naf):
        try:
            return (nif_nif / naf_naf)
        except:
            return (f"Нельзя делить на нуль!!!")

ned = NeDelIteNaNull(1, 100)
print(NeDelIteNaNull.ne_delite_na_null(1, 1))
print(NeDelIteNaNull.ne_delite_na_null(9, 1))
print(ned.ne_delite_na_null(50, 0))